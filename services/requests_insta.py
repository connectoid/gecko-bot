import requests
import random
from datetime import datetime
from pprint import pprint

from utils.utils import save_json

urls = [
    'https://www.instagram.com/reel/C5lwbPYIzMs/?igsh=MTNiNml5bGV2aXk3ZA==',
    'https://www.instagram.com/reel/C4WiPb3vNX3/?igsh=N2ZsdXhob25vbmh6',
    'https://www.instagram.com/reel/C5Gy7-ANVKy/?igsh=MTRxNDV6b21hdWU4Yw==',
    'https://www.instagram.com/reel/C3PjaTXseE8/?igsh=MXJ2c2s4b2x2am1nYQ==',
    'https://www.instagram.com/reel/C23dhF3PtDR/?igsh=MWp2MHJzMDA5dmxvOA==',
    'https://www.instagram.com/reel/C4iOAtroTD6/?igsh=MTlhM2FmYjFja2R4bQ==',
    'https://www.instagram.com/reel/C5nNnLuMNxN/?igsh=MXNkN2lxMTFmZzJs',
    'https://www.instagram.com/reel/C3KzmC7vY38/?igsh=cTRuMjFwY2lkdDMz',
    'https://www.instagram.com/reel/C4TQ_dso068/?igsh=NjZ5YWU2Mnh1cWZs',
    'https://www.instagram.com/reel/C5n47AcRZDf/?igsh=a3JqNmdybzRwZW9n',
    'https://www.instagram.com/reel/C4pOp6LoWOA/?igsh=MTU0NnIzNWdpdGVwZg==',
]


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
    'http://zuQ205:Khmw7T@147.45.93.10:8000',
]

def get_random_proxy():
    proxy = random.choice(proxy_list)
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    return proxies

def send_request_for_reel(shortcode):
    max_retries = 3
    retry_number = 0
    endpoint = 'https://www.instagram.com/graphql/query'
    url = f'https://www.instagram.com/reel/{shortcode}/'
    if 'reel' in url:
        try:
            print(shortcode)
            headers = {
            'accept': '*/*',
            'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '2',
            'origin': 'https://www.instagram.com',
            'referer': f'{url}',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
            'sec-ch-ua-full-version-list': '"Google Chrome";v="123.0.6312.58", "Not:A-Brand";v="8.0.0.0", "Chromium";v="123.0.6312.58"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"macOS"',
            'sec-ch-ua-platform-version': '"14.2.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
            'viewport-width': '830',
            'x-asbd-id': '129477',
            'x-bloks-version-id': '2c91cd96c82784f84faaa4f7ee527407cd84c826a2d53f6e3ab87e8e69502b86',
            'x-csrftoken': 'h9WVZwuIpfEKXZ0hdqgFqeLJglBGP6WO',
            'x-fb-friendly-name': 'PolarisPostActionLoadPostQueryQuery',
            'x-fb-lsd': 'AVqCy1FViKw',
            'x-ig-app-id': '936619743392459',
            }
            data = {
                'av': '0',
                '__d': 'www',
                '__user': '0',
                '__a': '1',
                '__req': '5',
                '__hs': '19827.HYP:instagram_web_pkg.2.1..0.0',
                'dpr': '2',
                '__ccg': 'UNKNOWN',
                '__rev': '1012773657',
                '__s': '::027l1c',
                # '__hsi': '7357850965805043412',
                # '__dyn': '7xeUjG1mxu1syUbFp40NonwgU29zEdF8aUco2qwJw5ux609vCwjE1xoswaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2iyo2Ixe0EUjwGzEaE7622362W2K0zK5o4q3y1Sx-0iS2Sq2-azo7u1xwIwbS1LwTwKG1pg2Xwr86C1mwrd6goK68jxe6V89F8uxK3Oq',
                # '__csr': 'g8iNcn8ADiHquDbQWpqJkKil8F4_yt4V-XhbJeKezqBDLV8zxiuqaDhHAJeXCBXKiu4VaHxeJprUx2qgGaFBjzkXLBx1osh8Cifz_ybperz9ESvzVrGWy8lyVqgy74GwzCw05iXa5E4S1rw23oG4JwBg0c69VQajpE4C2Czj0befg0UC0cJCkM0gg8it2E11EO00wH80VC',
                '__comet_req': '7',
                'lsd': 'AVqCy1FViKw',
                'jazoest': '2956',
                '__spin_r': '1012773657',
                '__spin_b': 'trunk',
                '__spin_t': '1713133176',
                'fb_api_caller_class': 'RelayModern',
                'fb_api_req_friendly_name': 'PolarisPostActionLoadPostQueryQuery',
                'variables': f'{{"shortcode":"{shortcode}","fetch_comment_count":40,"parent_comment_count":24,"child_comment_count":3,"fetch_like_count":10,"fetch_tagged_user_count":null,"fetch_preview_comment_count":2,"has_threaded_comments":true,"hoisted_comment_id":null,"hoisted_reply_id":null}}',
                'server_timestamps': 'true',
                'doc_id': '24852649951017035',
            }
            proxies = get_random_proxy()
            print(proxies)
            response = requests.post(endpoint, proxies=proxies, headers=headers, data=data)
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    return response_json
                except Exception as e:
                    print(f'* * * Ошибка получения json из ответа: {e}')
                    return False
            else:
                print(f'* * * Ошибка получения ответа, статус код: {response.status_code}')
                return False
        except Exception as e:
            print(f'* * * Ошибка получения shortcode из ссылки: {e}')
            return False
    else:
        print(f'* * * Ссылка непраильная (не Reel)')
        return False


def get_caption_from_json(json_data):
    try:
        caption = json_data['data']['xdt_shortcode_media']['edge_media_to_caption']['edges'][0]['node']['text']
        return caption
    except Exception as e:
        print(f'* * * Ошибка получения заголовка из json: {e}')
        return 'No caption'



def get_video_requests(shortcode):
    print(f'Запрошено видео по ссылке {shortcode}')
    response_json = send_request_for_reel(shortcode)
    if response_json:
        try:
            save_json(response_json)
            caption = get_caption_from_json(response_json)
            print(caption)
            video_url = response_json['data']['xdt_shortcode_media']['video_url']
            if video_url:
                return video_url
            else:
                print(f'* * * Неизвестная ошибка получения ссылки на видео')
                return None
        except Exception as e:
            print(f'* * * Ошибка получения ссылки на видео из ответа: {e}')
            return False
    else:
        print(f'* * * json не получен')
        return False

# for url in urls:
#     time1 = datetime.now()
#     video_url = get_video_url(url)
#     time2 = datetime.now()
#     print(f'Video {video_url} downloaded by {time2 - time1} sec')

