from urllib.parse import unquote
import html
import json
import random

import requests
from bs4 import BeautifulSoup

# url = 'https://www.instagram.com/stories/evgen_10_n/3347273781465142918?igsh=MXhjZDQ3Y3FoOWZsZw=='
proxy_list = [
    'http://LJ64PB:2FeTxb@94.131.19.56:9701',
    'http://LJ64PB:2FeTxb@95.164.201.179:9911',
    'http://LJ64PB:2FeTxb@95.164.202.85:9327',
    'http://LJ64PB:2FeTxb@94.131.54.35:9085',
    'http://LJ64PB:2FeTxb@186.179.61.133:9579',
    'http://LJ64PB:2FeTxb@91.218.50.161:9997',
    'http://LJ64PB:2FeTxb@38.153.57.53:9190',
    'http://LJ64PB:2FeTxb@38.152.246.128:9310',
    'http://LJ64PB:2FeTxb@94.131.87.20:9548',
    'http://LJ64PB:2FeTxb@94.131.89.115:9108',
]

def get_random_proxy():
    proxy = random.choice(proxy_list)
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    return proxies

def save_source_to_file(text):
    with open('source.html', 'w') as file:
        file.write(text)

def save_json(response, file='data.json'):
    with open(f'{file}', 'w', encoding='utf-8') as f:
        json.dump(response, f, ensure_ascii=False)


def get_stories(url):
    headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://saveig.app',
    'referer': 'https://saveig.app/',
    'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

    data = {
        'q': f'{url}',
        't': 'media',
        'lang': 'en',
    }

    proxies = get_random_proxy()
    response = requests.post('https://v3.saveig.app/api/ajaxSearch', proxies==proxies, data=data)
    if response.status_code == 200:
        # source = html.unescape(response.text)
        json_source = response.json()
        # save_json(json_source)
        html_data = json_source['data']
        unesqaped_html_data = html.unescape(html_data)
        # save_source_to_file(unesqaped_html_data)
        soup = BeautifulSoup(unesqaped_html_data, 'lxml')
        downloads_ul = soup.find('ul', class_='download-box')
        download_divs = downloads_ul.find_all('div', class_='download-items__btn')
        download_links = [div.find('a')['href'] for div in download_divs]
        return download_links
    else:
        print(f'Request error: {response.status_code}')
        return False
