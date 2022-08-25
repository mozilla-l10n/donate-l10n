# UI translations for donate.mozilla.org and give.thunderbird.net

[![Build Status](https://github.com/mozilla-l10n/donate-l10n/workflows/Continuous%20Integration/badge.svg)](https://github.com/mozilla-l10n/donate-l10n/actions?query=workflow%3A%22Continuous+Integration%22)

Process UI translations for donate.mozilla.org and give.thunderbird.net and upload them to S3.

## Contributing
Visit https://pontoon.mozilla.org/projects/mozilla-donate-website/ to contribute to translations.

CMS translations are stored in different repositories for [Mozilla](https://github.com/mozilla-l10n/mozilla-donate-content) and [Thunderbird](https://github.com/mozilla-l10n/thunderbird-donate-content).

## Updating dependencies for this project
*Django's version must be the same as the foundation site.*
Use [pip-tools](https://github.com/jazzband/pip-tools) to update dependencies:
- Create a virtual-env: `python3 -m venv venv `
- Install pip-tools: `pip install pip-tools`
- Edit the `requirements.in` file
- Run `pip compile`
- Open a PR with both `requirements.in` and `requirements.txt`


## License

Translations in this repository are available under the terms of the [Mozilla Public License v2.0](http://www.mozilla.org/MPL/2.0/).
