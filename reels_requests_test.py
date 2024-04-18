import requests
import random
from time import sleep
from datetime import datetime
from datetime import timedelta

from config_data.config import proxy_list

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
    'https://www.instagram.com/reel/C5tbAv_I9uR/?igsh=MTZoZmdndnZxZWJ0bQ==',
    'https://www.instagram.com/reel/C2Sb310oe5q/?igsh=azRlYWd1MnZ0dXRt',
    'https://www.instagram.com/reel/C5PLxkfPnBM/?igsh=dDVwaGx3OTZoMXdz',
    'https://www.instagram.com/reel/C5QhP1qulXE/?igsh=MXcxZG56bmM0YnB5Zw==',
    'https://www.instagram.com/reel/C5l4dWzrGD0/?igsh=MTd2MTczYzExYWgwMA==',
    'https://www.instagram.com/reel/C5vSVt_L6pA/?igsh=Y3Frcno2aTM5cG5u',
    'https://www.instagram.com/reel/C5vSVt_L6pA/?igsh=Y3Frcno2aTM5cG5u',
    'https://www.instagram.com/reel/C3HdUU-t_Bb/?igsh=ZW9mMXNoYzN5dDk0',
    'https://www.instagram.com/reel/C5G-hC8P1M4/?igsh=MTB6NmR2MXFhZ2t1YQ==',
    'https://www.instagram.com/reel/C4D0pIJtqWI/?igsh=MWJ3bWJqajlyOXZrZg==',
    'https://www.instagram.com/reel/C20P8tTOri2/?igsh=Z3RzYmFmM2g1aDh3',
    'https://www.instagram.com/reel/C5h1wPQCKeK/?igsh=YTV1Z3Q3a2d5anhk',
    'https://www.instagram.com/reel/C5uVe3FpVU7/?igsh=aGh3OGhmeDQzaHN3',
    'https://www.instagram.com/reel/C5i0yN5trnu/?igsh=MTgzcHEwbHVsNnZtag==',
    'https://www.instagram.com/reel/C45nBIZy22e/?igsh=aDBkNGs1c2c1NGN4',
    'https://www.instagram.com/reel/C4_fCNGvwVW/?igsh=MThjazRmYml4OHdyeQ==',
    'https://www.instagram.com/reel/C2mBk0qLTqR/?igsh=dzFjM2llMGJ6MGkz',
    'https://www.instagram.com/reel/C2xq_V0s8Di/?igsh=MWp0dGJpa3I4dDExbw==',
    'https://www.instagram.com/reel/C4ylFifITPV/?igsh=MW9janoxMWc3c3FxbQ==',
    'https://www.instagram.com/reel/C4RsCB5p87L/?igsh=MTkyZHJub2kwZWo3dg==',
    'https://www.instagram.com/reel/C2c1FU-rDN_/?igsh=cmN5d3BneHhnN3Bx',
    'https://www.instagram.com/reel/C5RdS4Zv11r/?igsh=MTh2YTNnaTZ5eWJnNw==',
    'https://www.instagram.com/reel/C4-QjdlxsrZ/?igsh=a3N5ZjR6b3Rnem40',
    'https://www.instagram.com/reel/C5dfNWFsHME/?igsh=MTh3YTI3OHc3MXU1Yg==',
    'https://www.instagram.com/reel/C4gIsYXIENE/?igsh=M2Nva2UxaGg3bG95',
    'https://www.instagram.com/reel/C3m-GW6sa8I/?igsh=MXZoaWZpNG41czdseQ==',
    'https://www.instagram.com/reel/C4eXD-AJJkn/?igsh=bXJ0MW5sY3NyN3J3',
    'https://www.instagram.com/reel/C4icygCMoXM/?igsh=MTJxbmZ6ZDFycDdzZw==',
    'https://www.instagram.com/reel/C4ibU3mI43U/?igsh=MWlsaW9sdWp3YWhiZg==',
    'https://www.instagram.com/reel/C5W-ESlI3MZ/?igsh=YnUyZTJpNjRoczJj',
    'https://www.instagram.com/reel/C2QNGCAopKO/?igsh=MWw2NjU2NjB4a3pvcA==',
    'https://www.instagram.com/reel/C5SXjgOsb7j/?igsh=ZnR6dG5jbTUwYnU0',
    'https://www.instagram.com/reel/C2XaLbJoDkk/?igsh=MTMxNGMyNDJuMnZqYQ==',
    'https://www.instagram.com/reel/C4v-AaNNIIj/?igsh=a244aXJhOWNybTZh',
    'https://www.instagram.com/reel/C3nKe6atvkQ/?igsh=MWprNmpkM250a3U5eg==',
    'https://www.instagram.com/reel/C5WJIEAqOg3/?igsh=dnd1cG96MmNpbW55',
    'https://www.instagram.com/reel/C5g9gSTAfXb/?igsh=eG9rNGY0aWo3cTR2',
    'https://www.instagram.com/reel/C5TT1mOrrT-/?igsh=N3c2bmc5OW5tczRs',
    'https://www.instagram.com/reel/C20ur76ydSH/?igsh=MXRzdDZ0dGExNTdjZw==',
    'https://www.instagram.com/reel/C5bVvZMtvbf/?igsh=MW5kanAwM3QxZXE2dA==',
    'https://www.instagram.com/reel/C5vXafiK753/?igsh=MzR1Z3kyOTYyeDJ5',
    'https://www.instagram.com/reel/C5S1k4yozK9/?igsh=MTJlYnFqdzB5NnQ4MQ==',
    'https://www.instagram.com/reel/C2kY4_XtoC-/?igsh=YWIzdXF0dXZpY2Fv',
    'https://www.instagram.com/reel/C4y1PMhv3hB/?igsh=MTBsc2JtZnZ4MHJ4Yw==',
    'https://www.instagram.com/reel/C35R-hmNCDy/?igsh=MWlsN2VwZXhxbmlzZw==',
    'https://www.instagram.com/reel/C2hjGRLMSuF/?igsh=MTdvYnNseHV6Y2s4Zw==',
    'https://www.instagram.com/reel/C5CaZ_DyF3W/?igsh=MWxvZnRyYjhwZjJnZA==',
    'https://www.instagram.com/reel/C40QgjSLn7m/?igsh=emQyNHJpNGtyYnhz',
    'https://www.instagram.com/reel/C4q3da9LjVS/?igsh=emtobWdwZzN2cGF1',
    'https://www.instagram.com/reel/C4-0liRMD0B/?igsh=N3c4Nzg5amx5bXRr',
]


proxy_waiting_list = []

def get_random_proxy():
    proxy = random.choice(proxy_list)
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    return proxies

def send_request_for_reel(shortcode):
    endpoint = 'https://www.instagram.com/graphql/query'
    url = f'https://www.instagram.com/reel/{shortcode}/'
    if 'reel' in url:
        try:
            # print(shortcode)
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
            proxy = proxies['http']
            proxy_ip = proxy.split(':')[-2].split('@')[-1]
            print(f'Выбран прокси {proxy_ip}')
            response = requests.post(endpoint, proxies=proxies, headers=headers, data=data)
            if response.status_code == 200:
                try:
                    response_json = response.json()
                    return response_json
                except Exception as e:
                    print(f'* * * Ошибка получения json из ответа: {e}')
                    return False
            elif response.status_code == 401:
                print(f'* * * Ошибка, требуется авторизация, возможно прокси забанен, статус код: {response.status_code}')
                proxy_waiting_list.append(proxy)
                proxy_list.remove(proxy)
                print(f'Прокси {proxy_ip} исключен из списка доступныз прокси и добавлен в список ожидания')
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

def main():
    success_count = fail_count = 0
    count = 1
    time_start = datetime.now()
    while (datetime.now() - time_start) < timedelta(minutes=60):
    # for count in range(1, 101):
        print(f'Time Delta: {datetime.now() - time_start}')
        url = random.choice(urls)
        shortcode = url.split('/reel/')[1].split('/')[0]
        interval = random.randint(1, 10)
        json_data = send_request_for_reel(shortcode)
        if json_data:
            video_url = json_data['data']['xdt_shortcode_media']['video_url']
            print(f'{count}. Ссылка {video_url[:50]} получена удачно. Ждем {interval} сек.')
            sleep(interval)
            success_count += 1
            count += 1
        else:
            print(f'{count}. Ссылка не получена. Ждем {interval} сек.')
            sleep(interval)
            fail_count += 1
            count += 1

    print(f'Удачных: {success_count} Неудачных: {fail_count}')
    print(f'Список живых прокси: {proxy_list}')
    print(f'Список ожидаемых прокси: {proxy_waiting_list}')


if __name__ == '__main__':
    main()