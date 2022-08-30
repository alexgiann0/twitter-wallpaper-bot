import tweepy
import urllib.request
from datetime import datetime
import requests
import os
import schedule
import time


##twitter api setup
client_id = "xxxx"
client_secret = "xxxx"
api_key = "xxxx"
api_key_secret = "xxxx"
access_token = "xxxx"
access_token_secret = "xxxx"
bearer_token = "xxxx"

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


##main
def get_picture(url, full_path):
    urllib.request.urlretrieve(url, full_path)

def generator(x, y):
    return f"https://picsum.photos/{x}/{y}"

def imageUpload() :
    print("Pending request...")
    img = requests.get(generator(3840, 2160)).url 
    
    now = datetime.now()
    print("Got image at {}".format(now.strftime("%d/%m/%Y %H:%M:%S")))

    path = "E:/twitter_bot_images/image-{}.jpg".format(now.strftime("%d_%m_%Y-%H.%M.%S"))

    get_picture(img, path)

    api.update_status_with_media("", path)
    print("Uploaded image at {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))

    if os.path.exists("E:/twitter_bot_images/image-{}.jpg".format(now.strftime("%d_%m_%Y-%H.%M.%S"))):
        os.remove("E:/twitter_bot_images/image-{}.jpg".format(now.strftime("%d_%m_%Y-%H.%M.%S")))
        print("Deleted image from directory at {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    else:
        print("Failed to locate/delete image from directory")
    
schedule.every().hour.at(":00").do(imageUpload)

while True:
    schedule.run_pending()
    time.sleep(1)