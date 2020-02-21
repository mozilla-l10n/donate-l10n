#!/usr/bin/env bash

set -euo pipefail

# Keep the commit hash
touch translations_github_commit_${TRAVIS_COMMIT}

# Selecting only a file in travis doesn't seem to work, using a dir instead
mkdir -p to_upload

# Move the pt_BR files to pt so Django can find them
# Foundation site
rm -rf ./foundation/translations/locale/pt/
mv ./foundation/translations/locale/pt_BR/ ./foundation/translations/locale/pt/
# Buyers' guide
rm -rf ./foundation/translations/networkapi/buyersguide/locale/pt/
mv ./foundation/translations/networkapi/buyersguide/locale/pt_BR/ ./foundation/translations/networkapi/buyersguide/locale/pt/
rm -rf ./foundation/translations/networkapi/buyersguide/templates/about/locale/pt/
mv ./foundation/translations/networkapi/buyersguide/templates/about/locale/pt_BR/ ./foundation/translations/networkapi/buyersguide/templates/about/locale/pt/
# Mozfest
rm -rf ./foundation/translations/networkapi/mozfest/locale/pt/
mv ./foundation/translations/networkapi/mozfest/locale/pt_BR/ ./foundation/translations/networkapi/mozfest/locale/pt/

echo "Archiving files"
tar -C foundation/translations -cvf ./to_upload/translations.tar ./locale ./networkapi
tar rvf ./to_upload/translations.tar ./translations_github_commit_${TRAVIS_COMMIT}
echo "Done!"
