from urllib.parse import unquote
import html
import json
import random
from time import sleep

import requests
from bs4 import BeautifulSoup

from config_data.config import proxy_list

stories_list = [
    'https://www.instagram.com/stories/m_galustyan/3347459925515336431?igsh=MWloc2Nyb20xZmw5cg==',
    'https://www.instagram.com/stories/zhanna_baybakova/3347414385355279132?igsh=NWxwNGgweGg5YzE3',
    'https://www.instagram.com/stories/video_positivo/3347310065365455440?igsh=eHI0NGZnOTNlbjZv',
    'https://www.instagram.com/stories/amocucinare/3347535227843930565?igsh=a3FudHo2bWxsZjQ0',
    'https://www.instagram.com/stories/hideo_kojima/3347568644770709475?igsh=Yzl1eXNpNGI0N3Rm',
    'https://www.instagram.com/stories/kaliningradru/3347285678625082096?igsh=MWwzdHBrZTFrZHFpZg==',
    'https://www.instagram.com/stories/svinto4ek/3347651887459934594?igsh=YXNjOHpzcThvZ2Zx',
    'https://www.instagram.com/stories/igor_birdsandwhales/3347424286581534293?igsh=cHBiMXhoajF6ano5',
    'https://www.instagram.com/stories/newredko/3347562155736520789?igsh=eXcxcDVnMWl6dGt3',
    'https://www.instagram.com/stories/evgeny_kulik/3347354978811278805?igsh=ZWJza2NzNDlmMW12',
    'https://www.instagram.com/stories/tri_taranki/3347565942814099893?igsh=dm82czMwZ29nNGQ0',
    ]


proxy_waiting_list = []

def get_random_proxy():
    proxy = random.choice(proxy_list)
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    return proxies

def get_random_story():
    story = random.choice(stories_list)
    return story


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
    response = requests.post('https://v3.saveig.app/api/ajaxSearch', proxies=proxies, data=data)
    if response.status_code == 200:
        json_source = response.json()
        try:
            html_data = json_source['data']
            unesqaped_html_data = html.unescape(html_data)
            soup = BeautifulSoup(unesqaped_html_data, 'lxml')
            downloads_ul = soup.find('ul', class_='download-box')
            download_divs = downloads_ul.find_all('div', class_='download-items__btn')
            download_links = [div.find('a')['href'] for div in download_divs]
            return download_links
        except Exception as e:
            print(f'Ошибка получения JSON в сторис, возможно неверная ссылка: {e}')
            return False
    else:
        print(f'Request error: {response.status_code}')
        return False


def main():
    success_count = fail_count = 0
    for count in range(1, 101):
        url = random.choice(stories_list)
        interval = random.randint(1, 2)
        download_links = get_stories(url)
        if download_links:
            print(f'{count}. Сторис {download_links[0][:50]} получены удачно. Ждем {interval} сек.')
            sleep(interval)
            success_count += 1
        else:
            print(f'{count}. Сторис не получены. Ждем {interval} сек.')
            sleep(interval)
            fail_count += 1

    print(f'Удачных: {success_count} Неудачных: {fail_count}')
    print(f'Список живых прокси: {proxy_list}')
    print(f'Список ожидаемых прокси: {proxy_waiting_list}')


if __name__ == '__main__':
    main()