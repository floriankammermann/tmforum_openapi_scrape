# Scrape all resources from the tmforum OpenAPI Directory

## get the OpenAPI urls
1. go to https://www.tmforum.org/oda/open-apis/directory
2. open the dev tools
3. go to Elements -> select `<html lang="en" style>` -> right click -> copy
4. save the copied content in a file named `open_api.html`
5. extract the relevant path with `cat open_api.html | grep href | grep '/oda/open-apis/directory' | grep TMF | sed 's/.*href="\/oda\/open-apis\/directory\///g' | sed 's/"//g' > open_api_path.txt`

## construct the OpenAPI user guide urls
