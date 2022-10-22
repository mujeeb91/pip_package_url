from bs4 import BeautifulSoup
import requests


BASE_URL = 'https://pypi.org/project/'
BASE_URL_SUFFIX = '/#files'
INPUT_FILENAME = 'input.txt'


def get_download_url(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    content = response.content
    soup = BeautifulSoup(content, 'html.parser')
    download_url = soup.find('div', class_='card file__card')\
        .a.get('href')
    return download_url

def get_filename(url):
    return url.rsplit('/')[-1]

def main():
    urls = []
    with open(INPUT_FILENAME) as f:
        for line in f:
            pkg_name, version = line.strip().split('==')
            url = f'{BASE_URL}{pkg_name}/{version}{BASE_URL_SUFFIX}'
            urls.append(url)
    for url in urls:
        download_url = get_download_url(url)
        print(download_url)

if __name__ == "__main__":
    main()
