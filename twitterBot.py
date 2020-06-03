import tweepy
import time

CONSUMER_KEY = 'your API key number here'
CONSUMER_SECRET = 'your API secret key number here'
ACCESS_KEY = 'your access token here'
ACCESS_SECRET = 'your access token secret here'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

twitter_API = tweepy.API(auth)

def mention_followers():
    followers = twitter_API.followers()
    for follower in followers:
        twitter_API.update_status('Hello @' + follower.screen_name)
       
while True:
   mention_followers()
   time.sleep(3600)