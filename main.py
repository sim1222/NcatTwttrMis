import datetime
from email.header import Header
import tweepy
import requests
import json
from config import CONFIG
from misskey import Misskey
import time


consumer_key = CONFIG["CONSUMER_KEY"]
consumer_secret = CONFIG["CONSUMER_SECRET"]
access_token = CONFIG["ACCESS_TOKEN"]
access_token_secret = CONFIG["ACCESS_SECRET"]
isDiscord = CONFIG["isDiscord"]
DiscordWebhook = CONFIG["DiscordWebhook"]


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

misskey_addr = CONFIG["MISSKEY_ADDRESS"]
misskey_token = CONFIG["MISSKEY_API"]

mk = Misskey(misskey_addr, misskey_token)

global last_tw_id
last_tw_id: int = 1

#nullnyat
user_id = 1451961024257540096

isFirst = True

def gettw():
    #for tweet in public_tweets:
        global last_tw_id
        public_tweets = api.user_timeline(user_id=user_id, since_id=last_tw_id, count=40)

        if len(public_tweets) == 0:
            print("already noted")
            return


        for tweet in reversed(public_tweets):

            print()
            print("getting...")
            print("Last ID: " + str(last_tw_id))
            print("Tweet ID: " + str(tweet.id))
            print("Posted from: " + tweet.user.name)
            print("Posted Time: " + str(tweet.created_at))
            print(tweet.text)
            print()

            global isFirst
            if isFirst == True:
                print("Its first get.")
                isFirst = False
                break

            postNakami = "ID: " + str(tweet.id) + "\n" \
                        + "Name: " + tweet.user.name.translate(str.maketrans({'@': '＠', '#': '＃'})) + "\n"\
                        + "Time: " + str(tweet.created_at) + "\n"\
                        + tweet.text.translate(str.maketrans({'@': '＠', '#': '＃'})) + "\n"\
                        + "https://twitter.com/" + str(tweet.user.screen_name) + "/status/" + str(tweet.id)

            if tweet.id > last_tw_id:
                if isDiscord == True:
                    sendData = {"content": postNakami}
                    sendHead = {"Content-Type": "application/json"}
                    requests.post(DiscordWebhook, data=json.dumps(sendData), headers=sendHead)
                    print("posted to discord")
                else:
                    mk.notes_create(
                        text=postNakami,
                        visibility="home",
                        local_only=True
                    )
                    print("noted")
            else:
                print("already noted")
            time.sleep(2)


        last_tw_id = public_tweets[0].id



while True:
    try:
        start = time.time()
        gettw()
        print("lastID: " + str(last_tw_id))
        used_time = time.time() - start
        print("time: " + str(used_time))
        print("sleep...")
        #if 60-used_time > 0:
        #    mk.notes_create(text="Sleep: " + str(int(60-used_time)) + "\n"
        #                    "Next: " + str(datetime.datetime.now() + datetime.timedelta(seconds=60-used_time)), visibility="home", local_only=True)
        #    time.sleep(60-used_time)

        #else:
        #    mk.notes_create(text="Sleep: " + str(int(used_time)) + "\n"
        #                    "Next: " + str(datetime.datetime.now() + datetime.timedelta(seconds=used_time)), visibility="home", local_only=True)
        #    time.sleep(1)

        time.sleep(300)


    except TimeoutError:
        print("timeout")
        time.sleep(60)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print("timeout" + str(e))
        time.sleep(60)

