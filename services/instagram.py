from datetime import datetime

import instaloader

SHORTCODE = 'C3mXyHpOsiE'
url = 'https://www.instagram.com/reel/C3rc1NFMb-K/?igsh=MWwxY3czeXByeXVvaw=='

L = instaloader.Instaloader()

def get_video_il(url):
    if 'reel' in url:
        SHORTCODE = url.split('/reel/')[1].split('/')[0]
        post = instaloader.Post.from_shortcode(L.context, SHORTCODE)
        L.download_post(post, target='video')
    else:
        print(f'Это не Reel')

while True:
    url = input('Enter url')
    get_video_il(url)