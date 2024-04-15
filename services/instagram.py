from datetime import datetime
from time import sleep
import random

from instagrapi import Client
from instagrapi.exceptions import LoginRequired


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

USERNAME = 'beleysasha@gmail.com'
PASSWORD = 's028006000434'

cl = Client()
cl.login(USERNAME, PASSWORD)
cl.dump_settings("session.json")

def login_user():
    """
    Attempts to login to Instagram using either the provided session information
    or the provided username and password.
    """
    

    cl = Client()
    session = cl.load_settings("session.json")

    login_via_session = False
    login_via_pw = False

    if session:
        try:
            cl.set_settings(session)
            cl.login(USERNAME, PASSWORD)

            # check if session is valid
            try:
                cl.get_timeline_feed()
            except LoginRequired:
                print("Session is invalid, need to login via username and password")

                old_session = cl.get_settings()

                # use the same device uuids across logins
                cl.set_settings({})
                cl.set_uuids(old_session["uuids"])

                cl.login(USERNAME, PASSWORD)
            login_via_session = True
            return cl
        except Exception as e:
            print("Couldn't login user using session information: %s" % e)

    if not login_via_session:
        try:
            print("Attempting to login via username and password. username: %s" % USERNAME)
            if cl.login(USERNAME, PASSWORD):
                login_via_pw = True
        except Exception as e:
            print("Couldn't login user using username and password: %s" % e)

    if not login_via_pw and not login_via_session:
        raise Exception("Couldn't login user with either password or session")


def get_random_proxy():
    proxy = random.choice(proxy_list)
    proxies = {
        'http': proxy,
        'https': proxy,
    }
    return proxy


def get_video_instagrapi(url):
    print(f'Запрошена ссылка {url}')
    cl = login_user()
    proxy = get_random_proxy()
    cl.set_proxy(proxy)
    cl.delay_range = [1, 3]
    if 'reel' in url:
        print('getting id')
        id = cl.media_pk_from_url(url)
        print('getting media info')
        try:
            media_info = cl.media_info(id)
            print('getting video_url')
            video_url = media_info.video_url
            # cl.video_download_by_url(video_url, folder='/video')
            return video_url
        except Exception as e:
            print(f'Error of getting media info: {e}')
            return None
    else:
        print(f'Это не Reel')
        return None


# for url in urls:
#     time1 = datetime.now()
#     # video_url = get_video_ytdl(url)
#     video_url = get_video_instagrapi(url)
#     time2 = datetime.now()
#     print(f'Video url: {video_url}\nDownloaded by {time2 - time1} sec')
