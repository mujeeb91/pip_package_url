from bs4 import BeautifulSoup
import requests


BASE_URL = 'https://pypi.org/project/'
BASE_URL_SUFFIX = '/#files'

urls = []
with open('requirements.txt') as f:
    for line in f:
        pkg_name, version = line.strip().split('==')
        url = f'{BASE_URL}{pkg_name}/{version}{BASE_URL_SUFFIX}'
        urls.append(url)


def get_download_url(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    download_url = soup.find('table', class_='table--downloads')\
        .tbody.find_all('tr', recursive=False)[-1].th.a.get('href')
    return download_url

def get_filename(url):
    return url.rsplit('/')[-1]

for url in urls:
    download_url = get_download_url(url)
    print(download_url)
