import requests

hikerapi_token = 'DG9WS2FN7Ft6L6ua20dDyXwxFSZi1bSa'

def get_video_hikerapi(shortcode):
    headers = {
        'accept': 'application/json',
        'x-access-key': f'{hikerapi_token}',
    }

    params = {
        'code': f'{shortcode}',
    }

    response = requests.get('https://api.hikerapi.com/v1/media/by/code', params=params, headers=headers).json()

    return response['video_url']