from datetime import datetime

from instagrapi import Client

cl = Client()

def get_video_il(url):
    if 'reel' in url:
        id = cl.media_pk_from_url(url)
        video_url = cl.media_info(id).video_url
        cl.video_download_by_url(video_url, folder='/video')
        return video_url
    else:
        print(f'Это не Reel')
        return None

while True:
    url = input('Enter url: ')
    time1 = datetime.now()
    video_url = get_video_il(url)
    time2 = datetime.now()
    print(f'Video url: {video_url}\nDownloaded by {time2 - time1} msec')