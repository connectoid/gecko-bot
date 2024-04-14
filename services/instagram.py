from datetime import datetime
from time import sleep

from instagrapi import Client
import yt_dlp


USERNAME = 'beleysasha'
PASSWORD = 's028006000434'

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


def get_video_instagrapi(url):
    cl = Client()
    cl.login(USERNAME, PASSWORD)


    if 'reel' in url:
        id = cl.media_pk_from_url(url)
        # sleep(2)
        media_info = cl.media_info(id)
        # sleep(2)
        video_url = media_info.video_url
        # video_url = cl.media_info(id).video_url
        # cl.video_download_by_url(video_url, folder='/video')
        return video_url
    else:
        print(f'Это не Reel')
        return None


def get_video_ytdl(url):
    if 'reel' in url:
        ydl_opts = {}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.url
        return video_url
    else:
        print(f'Это не Reel')
        return None


for url in urls:
    time1 = datetime.now()
    video_url = get_video_ytdl(url)
    time2 = datetime.now()
    print(f'Video url: {video_url}\nDownloaded by {time2 - time1} sec')