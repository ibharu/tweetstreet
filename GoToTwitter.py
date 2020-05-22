import os
print(os.environ.get('TWITTER_CONSUMER_KEY'))
print(os.environ.get('TWITTER_CONSUMER_SECRET'))
print(os.environ.get('TWITTER_ACCESS_TOKEN'))
print(os.environ.get('TWITTER_ACCESS_SECRET'))
#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from pymongo import MongoClient
import json
from tweepy import OAuthHandler
from tweepy import Stream

#Variables that contains the user credentials to access Twitter API
access_token = os.environ.get('TWITTER_ACCESS_TOKEN')
access_token_secret = os.environ.get('TWITTER_ACCESS_SECRET')
consumer_key = os.environ.get('TWITTER_CONSUMER_KEY')
consumer_secret = os.environ.get('TWITTER_CONSUMER_SECRET')


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print(data)
        client = MongoClient()
        db = client.GetTweets
        datajson = json.loads(data)
        created_at = datajson['created_at']
        tweets = db.GetTweets
        # tweets.insert_one(status._json)
        tweets.insert_one(datajson)
        print(datajson['text'])

        return True

    def on_error(self, status_code):
        print(status_code)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
# print("This is printing from GotoTwitter")
