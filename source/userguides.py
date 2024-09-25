from urllib.parse import urlparse
import re
import requests

def extract_name(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    name = path.split('/')[0]  # Extract the first element
    return name

def extract_version(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    version = path.split('/')[1] 
    version_without_v = version[1:]
    version_tokens = version_without_v.split('.')
    if version_tokens[2] != "0":
        version_without_v = version_tokens[0] + "." + version_tokens[1] + "." + "0"
    return version_without_v

def tokenize_string(input_string):
    tokens = input_string.split('-')
    return tokens  

def prepare_name_tokens(name_tokens):
    prepared_name_tokens = []
    for token in name_tokens:
        if len(token) <= 3:
            prepared_name_tokens.append(token.upper())
        else:
            prepared_name_tokens.append(token.capitalize())
    return prepared_name_tokens



def create_user_guide_url(name_tokens, tm_number, version):
    # TMF620_Product_Catalog/5.0.0/user_guides/TMF620_Product_Catalog_userguide.pdf
    url = "https://tmf-open-api-table-documents.s3.eu-west-1.amazonaws.com/OpenApiTable/"     
    if len(name_tokens) >= 3:
        url = url + tm_number
        url = url + "_" + name_tokens[0]
        url = url + "/" + version
        url = url + "/user_guides/"
        url = url + tm_number
        url = url + "_" + name_tokens[0]
        url = url + "_userguide.pdf"
    return url

def create_user_guide_url_management(name_tokens, tm_number, version):
    print(name_tokens)
    # TMF620_Product_Catalog/5.0.0/user_guides/TMF620_Product_Catalog_userguide.pdf
    url = "https://tmf-open-api-table-documents.s3.eu-west-1.amazonaws.com/OpenApiTable/"     
    if len(name_tokens) >= 3:
        url = url + tm_number
        url = url + "_" + name_tokens[0]
        url = url + "/" + version
        url = url + "/user_guides/"
        url = url + tm_number
        url = url + "_" + name_tokens[0]
        url = url + "_" + name_tokens[1]
        url = url + "_API_v" + version + "_specification.pdf"
    return url

def create_user_guide_url_management_path_and_name(name_tokens, tm_number, version):
    print(name_tokens)
    # TMF620_Product_Catalog/5.0.0/user_guides/TMF620_Product_Catalog_userguide.pdf
    url = "https://tmf-open-api-table-documents.s3.eu-west-1.amazonaws.com/OpenApiTable/"     
    if len(name_tokens) >= 3:
        url = url + tm_number
        url = url + "_" + name_tokens[0]
        url = url + "_" + name_tokens[1]
        url = url + "/" + version
        url = url + "/user_guides/"
        url = url + tm_number
        url = url + "_" + name_tokens[0]
        url = url + "_" + name_tokens[1]
        url = url + "_API_v" + version + "_specification.pdf"
    return url

def get_tm_number(name_tokens):
    for token in name_tokens: 
        if token.startswith("TM"):
            return token
    return ""

def tm_number_matches_format(token):
    pattern = re.compile("^TMF[0-9]{3}$")
    return pattern.match(token)

def read_openapi_path():
    lines = []
    with open('output/open_api_path.txt', 'r') as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

def check_if_resource_exists(url):
    response = requests.get(url)
    return response.status_code == 200

openapi_paths = read_openapi_path()
f = open("output/userguides.txt", "w")

for path in openapi_paths:
    print(path)

    # e.g. account-management-TMF666
    name = extract_name(path)

    # e.g. 4.0.0
    version = extract_version(path)
    
    tokens = tokenize_string(name)

    # e.g. TMF666
    tm_number = get_tm_number(tokens)

    if not tm_number_matches_format(tm_number):
        continue

    name_tokens = prepare_name_tokens(tokens)
    url = create_user_guide_url(name_tokens, tm_number, version)
    print(url)
    if check_if_resource_exists(url):
        f.write(url + "\n")
        continue

    url = create_user_guide_url_management(name_tokens, tm_number, version)
    print(url)
    if check_if_resource_exists(url):
        f.write(url + "\n")
        continue

    url = create_user_guide_url_management_path_and_name(name_tokens, tm_number, version)
    print(url)
    if check_if_resource_exists(url):
        f.write(url + "\n")
        continue

    f.write("missed: " + path + "\n")

f.close()
