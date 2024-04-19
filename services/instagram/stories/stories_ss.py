import requests
import json


url = 'https://www.instagram.com/stories/kaliningradru/3348828695814066731?igsh=N3o1YXhxZXV2bXV4'
url = 'https://www.instagram.com/stories/kaliningradru/3348722759725308850?igsh=MWo5bHZzamFkZnVqMg=='
endpoint = 'https://sssinstagram.com/api/ig/story'

def get_stories_ss(url):
    import requests

    cookies = {
        '_ga': 'GA1.1.1568532580.1713236283',
        'uid': '8dc438cd9947003d',
        'adsAfterSearch': '60',
        'adsPopupClick': '36',
        'adsForm': '16',
        '__gads': 'ID=762cca1847dd2383:T=1713236292:RT=1713501731:S=ALNI_MaeaxAVeHJZQzhXw_QpRvxdPuy-Pw',
        '__gpi': 'UID=00000df1fcbe9f40:T=1713236292:RT=1713501731:S=ALNI_MZMM63fc41NtuaUfZvvEmwpBdH0Ug',
        '__eoi': 'ID=eb8815a1d80a5c0c:T=1713236292:RT=1713501731:S=AA-AfjbBnQ3JMcgqCsGkikYk8eAj',
        'XSRF-TOKEN': 'eyJpdiI6Imw5RGQxd3pHLzBIVnJLV0h2S1d2OUE9PSIsInZhbHVlIjoiVkNiNUpOYjBpNHFLZVQzeXJSVU1iWHB4QWhlVlFqaVRNOTh0dEVUckRVQmh2MzI3Tm5iY1dxckxFMEhOMm9ZNU9uS0VYNkl6ZzVuTjBjZWF1M3Q0c2VsVTNDb0VnZHZkcCtHTzlJdkRlUi9Ka2NkRTNpNWQrN2gwWHZRMFFJYnUiLCJtYWMiOiIwMWQ1NDcwN2JhMzJkZjgzYWVlNmM4YzI5ZDE4NmUyMDJiNDZkYWY5NzIwOWM0NTM2NGU2NGUwM2M2NjAxMThhIiwidGFnIjoiIn0%3D',
        'sssinstagram_session': 'eyJpdiI6IjdsbHplSHdoL3lsZGlKbGRJSzg1a1E9PSIsInZhbHVlIjoiaVZrNHNYZ0syN20zQ3h1ZW0vMi9yVi9rYnBESzkweGx4UU0yMXowZUhKcU9TbGZrOFFPVDRvQWg5SGxkVFZ1cXJmeGladHZZTXlqUU5HQk9WWldpclQ2blZJMHl2bEptaUIzY2ZXcGxwYkRnbWkydFN0TDQ1dGlhNkNaSTZhK3EiLCJtYWMiOiI0MTMzNjFjZWI3ZjBhN2Q2NGEyNTU0NmFjZGRkOTQwYWMwMWI3OWU4MGMzZWYxZmNjOTIxN2MwZGIzYzU2YTIyIiwidGFnIjoiIn0%3D',
        '_ga_KDHKH4GDQE': 'GS1.1.1713501724.3.1.1713501795.0.0.0',
    }

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6,zh;q=0.5',
        # 'cookie': '_ga=GA1.1.1568532580.1713236283; uid=8dc438cd9947003d; adsAfterSearch=60; adsPopupClick=36; adsForm=16; __gads=ID=762cca1847dd2383:T=1713236292:RT=1713501731:S=ALNI_MaeaxAVeHJZQzhXw_QpRvxdPuy-Pw; __gpi=UID=00000df1fcbe9f40:T=1713236292:RT=1713501731:S=ALNI_MZMM63fc41NtuaUfZvvEmwpBdH0Ug; __eoi=ID=eb8815a1d80a5c0c:T=1713236292:RT=1713501731:S=AA-AfjbBnQ3JMcgqCsGkikYk8eAj; XSRF-TOKEN=eyJpdiI6Imw5RGQxd3pHLzBIVnJLV0h2S1d2OUE9PSIsInZhbHVlIjoiVkNiNUpOYjBpNHFLZVQzeXJSVU1iWHB4QWhlVlFqaVRNOTh0dEVUckRVQmh2MzI3Tm5iY1dxckxFMEhOMm9ZNU9uS0VYNkl6ZzVuTjBjZWF1M3Q0c2VsVTNDb0VnZHZkcCtHTzlJdkRlUi9Ka2NkRTNpNWQrN2gwWHZRMFFJYnUiLCJtYWMiOiIwMWQ1NDcwN2JhMzJkZjgzYWVlNmM4YzI5ZDE4NmUyMDJiNDZkYWY5NzIwOWM0NTM2NGU2NGUwM2M2NjAxMThhIiwidGFnIjoiIn0%3D; sssinstagram_session=eyJpdiI6IjdsbHplSHdoL3lsZGlKbGRJSzg1a1E9PSIsInZhbHVlIjoiaVZrNHNYZ0syN20zQ3h1ZW0vMi9yVi9rYnBESzkweGx4UU0yMXowZUhKcU9TbGZrOFFPVDRvQWg5SGxkVFZ1cXJmeGladHZZTXlqUU5HQk9WWldpclQ2blZJMHl2bEptaUIzY2ZXcGxwYkRnbWkydFN0TDQ1dGlhNkNaSTZhK3EiLCJtYWMiOiI0MTMzNjFjZWI3ZjBhN2Q2NGEyNTU0NmFjZGRkOTQwYWMwMWI3OWU4MGMzZWYxZmNjOTIxN2MwZGIzYzU2YTIyIiwidGFnIjoiIn0%3D; _ga_KDHKH4GDQE=GS1.1.1713501724.3.1.1713501795.0.0.0',
        'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'x-xsrf-token': 'eyJpdiI6Imw5RGQxd3pHLzBIVnJLV0h2S1d2OUE9PSIsInZhbHVlIjoiVkNiNUpOYjBpNHFLZVQzeXJSVU1iWHB4QWhlVlFqaVRNOTh0dEVUckRVQmh2MzI3Tm5iY1dxckxFMEhOMm9ZNU9uS0VYNkl6ZzVuTjBjZWF1M3Q0c2VsVTNDb0VnZHZkcCtHTzlJdkRlUi9Ka2NkRTNpNWQrN2gwWHZRMFFJYnUiLCJtYWMiOiIwMWQ1NDcwN2JhMzJkZjgzYWVlNmM4YzI5ZDE4NmUyMDJiNDZkYWY5NzIwOWM0NTM2NGU2NGUwM2M2NjAxMThhIiwidGFnIjoiIn0=',
    }

    params = {
        'url': f'{url}',
    }

    response = requests.get(endpoint, params=params, cookies=cookies, headers=headers)
    if response.status_code == 200:
        json_data = response.json()
        if 'video_versions' in json_data['result'][0]:
            video_url = json_data['result'][0]['video_versions'][0]['url']
        else:
            video_url = json_data['result'][0]['image_versions2']['candidates'][0]['url']
        return video_url
    else:
        print(f'Request error, status code: {response.status_code}')
        return False
