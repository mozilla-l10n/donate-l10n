"""Management command running on CI: Send a message on Slack if an error is found while running compilemessages."""
import io

from django.core.management import call_command
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
import requests


class DoubleOutput:
    """
    A file object that write to two file objects
    """

    def __init__(self, file1, file2):
        self.file1 = file1
        self.file2 = file2

    def write(self, msg):
        self.file1.write(msg)
        self.file2.write(msg)


class Command(BaseCommand):
    help = 'Run compilemessages and send a message to Slack if it returns an error.'

    def handle(self, *args, **options):
        output = io.StringIO()
        try:
            call_command("compilemessages", verbosity=1, stderr=DoubleOutput(self.stderr, output))
        except CommandError as err:
            travis_job_web_url = settings.TRAVIS_JOB_WEB_URL
            slack_webhook = settings.SLACK_WEBHOOK_PONTOON

            slack_payload = {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "<!here> An error occurred while compiling `.po` files for "
                                    "donate-wagtail on Travis:\n"
                                    f"```{err}\n{output.getvalue()}```\n"
                        }
                    },
                    {
                        "type": "actions",
                        "elements": [
                            {
                                "type": "button",
                                "text": {
                                    "type": "plain_text",
                                    "text": "View logs"
                                },
                                "url": f"{travis_job_web_url}"
                            }
                        ]
                    }
                ]
            }

            r = requests.post(f'{slack_webhook}',
                              json=slack_payload,
                              headers={'Content-Type': 'application/json'}
                              )

            # Raise if post request was a 4xx or 5xx
            r.raise_for_status()

            # Raise exception to make travis run fail
            raise err
