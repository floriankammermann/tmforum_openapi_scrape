# Scrape all resources from the tmforum OpenAPI Directory

You can directly startet with "download all content", since the file generated from "get the OpenAPI TMF relative paths" is commited.

## get the OpenAPI TMF relative paths
1. go to https://www.tmforum.org/oda/open-apis/directory
1. open the dev tools
1. go to Elements -> select `<html lang="en" style>` -> right click -> copy
1. save the copied content in a file named `output/open_api.html`
1. format `output/open_api.html` with e.g. visual code formatter. We need linebreaks for the next step
1. extract the relevant path with `cat output/open_api.html | grep href | grep '/oda/open-apis/directory' | grep TMF | sed 's/.*href="\/oda\/open-apis\/directory\///g' | sed 's/"//g' > output/open_api_path.txt`

## download all content
1. install [python3](https://www.python.org/downloads/)
1. execute `python3 source/fetch_tmf_api_content.py`
1. content will be fetched to `output/TMF<number>`

# browsing the content

For efficiently browsing the content use this setup.

1. Install [Visual Studio Code](https://code.visualstudio.com/)
1. Install [vscode-pdf](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf)
1. Install [OpenAPI (Swagger) Editor](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi)

## additional sources for slicing through the content
* https://danaepp.com/how-to-extract-artifacts-from-openapi-docs-to-help-attack-apis
* https://github.com/manchenkoff/openapi3-parser
