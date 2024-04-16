from instascrape import Reel 
google_reel = Reel('https://www.instagram.com/reel/C5nBjszsoFU/?utm_source=ig_web_copy_link')
google_reel.scrape()
# print(f"This reel has {google_reel.video_view_count:,} views.")