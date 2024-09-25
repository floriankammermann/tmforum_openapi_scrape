from lxml import html
import requests
import re
import wget
from urllib.parse import urlparse
from pathlib import Path

def extract_urls(string):
    # Regular expression pattern to match URLs
    url_pattern = re.compile(r'https://tmf-open-api-table-documents.s3.eu-west-1.amazonaws.com/[a-zA-Z0-9/_\-\.]*[pdf|yaml|json]')

    # Find all matches in the string
    urls = re.findall(url_pattern, string)
    
    return urls

def get_tm_number(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    name = path.split('/')[0]
    tokens = name.split('-')
    for token in tokens: 
        if token.startswith("TM"):
            return token
    return ""

def read_openapi_path():
    lines = []
    with open('output/open_api_path.txt', 'r') as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

def create_tmf_directories(pathes):
    for path in pathes:
        tm_number = get_tm_number(path)
        Path("output/" + tm_number).mkdir(parents=True, exist_ok=True)

def fetch_content(uniqurls, tm_number):
    for url in uniqurls:
        last = url.split('/')[-1] 
        print("download: " + url)
        try:
            wget.download(url, 'output/' + tm_number + "/" + last)        
        except:
            print("download failed for: " + url)


pathes = read_openapi_path()
create_tmf_directories(pathes)

baseUrl = "https://www.tmforum.org/oda/open-apis/directory/"

for path in pathes:
    url = baseUrl + path
    tm_number = get_tm_number(path)
    r = requests.get(url)
    source = r.content
    #print(source)
    page_source = html.fromstring(source)
    target_urls = extract_urls(str(source))
    target_uniqurls = set(target_urls)
    print(target_uniqurls)
    fetch_content(target_uniqurls, tm_number)

