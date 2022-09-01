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
    
    try:
        print("Pending request...") 
        img = requests.get(generator(3840, 2160)).url 
    except Exception as e:
        print("Failed to get image. \nError: {}\n".format(str(e)))
        return
    else:
        print("[{}]Got image".format(datetime.now().strftime("%H:%M:%S")))


    path = "E:/twitter_bot_images/image.jpg"

    get_picture(img, path)

    try:
        api.update_status_with_media("", path)
        print("[{}]Uploaded image".format(datetime.now().strftime("%H:%M:%S")))
    except Exception as e:
        print("Failed to upload image. Error: {}".format(str(e)))

    if os.path.exists("E:/twitter_bot_images/image.jpg"):
        os.remove("E:/twitter_bot_images/image.jpg")
        print("[{}]Deleted image from directory\n".format(datetime.now().strftime("%H:%M:%S")))
    else:
        print("Failed to locate/delete image from directory\n")
    
schedule.every().minute.at(":00").do(imageUpload) ####

while True:
    schedule.run_pending()
    time.sleep(1)
