try:
    import tweepy
    import urllib.request
    from datetime import datetime
    import requests
    import os
    import schedule
    import time
except ImportError:
    print("Error: {}".format(str(ImportError)))
    print("Install dependencies from requirements.txt!")
    print("Exiting...")
    time.sleep(5)
    exit()


##twitter api setup
client_id = "X09xWkRiYWt1SkQ0VzJVQjNaSjk6MTpjaQ"
client_secret = "03XBKdLIJqfV4ocvP60D7GVD1Xaw-ZtBV7JFZghjn7wah4JXRc"
api_key = "PgfSORbXOgnUI5Kb26jXqOyWR"
api_key_secret = "JN5yy6mpOmZJTqal5NnKXzzo6NFnmab8TjzXOjfOoSD22SaCQE" 
access_token = "1560724393483014145-DejdZZnPyEiZFmYtbmKISbrmvNbacN"
access_token_secret = "JWwvQHe6vFhIWkcM9phbVq76SW3mnwPSaQ6emssguAg5K"
bearer_token = "AAAAAAAAAAAAAAAAAAAAAL0DggEAAAAAXuMamBeFbvjQoHMcj60p0%2FrrwUQ%3DmPOX8FDbiOfza5Js0uxbRJXkAgoIycgWkvmL2CWvOwJG5NJFck" 

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit = True)


##main
def get_picture(url, full_path):
    urllib.request.urlretrieve(url, full_path)

def generator(x, y):
    return f"https://picsum.photos/{x}/{y}"

def imageUpload() :
    now = datetime.now()

    try:
        print("Pending request...") 
        img = requests.get(generator(3840, 2160)).url 
    except Exception as e:
        print("Failed to get image. \nError: {}\n".format(str(e)))
        return
    else:
        print("Got image at {}".format(now.strftime("%d/%m/%Y %H:%M:%S")))


    path = "E:/twitter_bot_images/image-{}.jpg".format(now.strftime("%d_%m_%Y-%H.%M.%S"))

    get_picture(img, path)

    try:
        api.update_status_with_media("", path)
        print("Uploaded image at {}".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    except Exception as e:
        print("Failed to upload image. Error: {}".format(str(e)))

    if os.path.exists("E:/twitter_bot_images/image-{}.jpg".format(now.strftime("%d_%m_%Y-%H.%M.%S"))):
        os.remove("E:/twitter_bot_images/image-{}.jpg".format(now.strftime("%d_%m_%Y-%H.%M.%S")))
        print("Deleted image from directory at {}\n".format(datetime.now().strftime("%d/%m/%Y %H:%M:%S")))
    else:
        print("Failed to locate/delete image from directory\n")
    
schedule.every().hour.at(":00").do(imageUpload)

while True:
    schedule.run_pending()
    time.sleep(1)