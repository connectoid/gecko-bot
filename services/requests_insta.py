import requests
from datetime import datetime


headers = {
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
    'content-type': 'application/x-www-form-urlencoded',
    # 'cookie': 'ig_did=324D1CF6-320E-49EE-9BF6-9F79129601B1; ig_nrcb=1; mid=ZhuJ1gAEAAG3I4ncj-FoWgGxbfU1; datr=1okbZkbUX7GqFZJjxPcPIf8P; ps_n=0; ps_l=0; rur="LDC\\05465705895864\\0541744633721:01f71800c136d5b83e2bb17971c6bec6ccd93a399023782e8f8080a3e1e5f6a76615c036"; csrftoken=h9WVZwuIpfEKXZ0hdqgFqeLJglBGP6WO',
    'dpr': '2',
    'origin': 'https://www.instagram.com',
    'referer': 'https://www.instagram.com/reel/C5lwbPYIzMs/?igsh=MTNiNml5bGV2aXk3ZA%3D%3D',
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
    'x-fb-lsd': 'AVqCy1FV4kI',
    'x-ig-app-id': '936619743392459',
}

data = {
    'av': '0',
    '__d': 'www',
    '__user': '0',
    '__a': '1',
    '__req': '3',
    '__hs': '19827.HYP:instagram_web_pkg.2.1..0.0',
    'dpr': '2',
    '__ccg': 'UNKNOWN',
    '__rev': '1012770895',
    '__s': 'cao99y:of8cgv:bflvvz',
    '__hsi': '7357700027941409069',
    '__dyn': '7xeUjG1mxu1syUbFp40NonwgU29zEdF8aUco2qwJw5ux609vCwjE1xoswaq0yE7i0n24oaEd86a3a1YwBgao6C0Mo2iyo2Ixe0EUjwGzEaE7622362W2K0zK5o4q3y1Sx-0iS2Sq2-azo7u1xwIwbS1LwTwKG1pg2Xwr86C1mwrd6goK68jxe6V89F8uxK3Oq',
    '__csr': 'g8AnP4RbIJFkiIQyRqy4CRJ9aA_GAjBRg-9mVkicAy9VeK9yUReHAx3CzqAgyAi4KHyFWFuczFHCykmBFpJeqcCFoSJ3bBUryVpSbiqxd3uiEO4oC9xlfyoych989ecyEO00l6wyx5380GCawXg6Ovg0iEw1KYg5821BsWx68ze1cxS0AUa80Nu0c7yx00l5xK0zIU02khw',
    '__comet_req': '7',
    'lsd': 'AVqCy1FV4kI',
    'jazoest': '2889',
    '__spin_r': '1012770895',
    '__spin_b': 'trunk',
    '__spin_t': '1713098033',
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'PolarisPostActionLoadPostQueryQuery',
    'variables': '{"shortcode":"C5lwbPYIzMs","fetch_comment_count":40,"parent_comment_count":24,"child_comment_count":3,"fetch_like_count":10,"fetch_tagged_user_count":null,"fetch_preview_comment_count":2,"has_threaded_comments":true,"hoisted_comment_id":null,"hoisted_reply_id":null}',
    'server_timestamps': 'true',
    'doc_id': '24852649951017035',
}

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

for url in urls:
    time1 = datetime.now()
    response = requests.post(url='https://www.instagram.com/graphql/query', headers=headers, data=data)
    time2 = datetime.now()
    print(response.json())
    video_url = response.json()['data']['xdt_shortcode_media']['video_url']
    print(f'Video url: {video_url}\nDownloaded by {time2 - time1} sec')
