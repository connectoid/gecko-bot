import requests

hikerapi_token = 'DG9WS2FN7Ft6L6ua20dDyXwxFSZi1bSa'

def get_story_hikerapi(url):
    headers = {
        'accept': 'application/json',
        'x-access-key': f'{hikerapi_token}',
    }

    params = {
        'url': f'{url}',
    }

    response = requests.get('https://api.hikerapi.com/v1/story/by/url', params=params, headers=headers).json()

    return response['video_url']