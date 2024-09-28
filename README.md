# Scrape all resources from the tmforum OpenAPI Directory

You can directly start with "download all content", since the file generated from "get the OpenAPI TMF relative paths" is commited.

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

## Visual Studio Code
For efficiently browsing the content use this setup.

1. Install [Visual Studio Code](https://code.visualstudio.com/)
1. Install [vscode-pdf](https://marketplace.visualstudio.com/items?itemName=tomoki1207.pdf)
1. Install [OpenAPI (Swagger) Editor](https://marketplace.visualstudio.com/items?itemName=42Crunch.vscode-openapi)

## OpenAPI Specs on command line
In the cli folder you find `extract_definitions_from_apispec`
You can use this command line tool to browse the OpenAPI schemas and extract them.
It only works on OpenAPI specs and not swagger.
Use `cli/extract_definitions_from_apispec -h` to explore the options.

## additional sources for slicing through the content
* https://danaepp.com/how-to-extract-artifacts-from-openapi-docs-to-help-attack-apis
* https://github.com/manchenkoff/openapi3-parser

# creating diagrams from the OpenAPI TMF Specifications
1. Install java
1. Download https://github.com/knutaa/oas2puml/releases/tag/Release_1.3.0
1. Generate the plantuml files for a OpenAPI TMF Specification: `java -jar apidiagram-1.3.0-SNAPSHOT.jar diagrams -f TMF620-Product_Catalog_Management-v5.0.0.oas.yaml`
1. Download https://plantuml.com/download
1. Generate a diagram from the plantuml files: `java -Djava.awt.headless=true -jar plantuml.jar Resource_ProductSpecification.puml`