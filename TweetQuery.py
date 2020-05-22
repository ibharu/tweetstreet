from pymongo import MongoClient

def Tweetquery(searchstring,dname="GetTweets",cname="GetTweets"):
    d_name=dname
    collection_name=cname
    client = MongoClient('127.0.0.1', 27017)
    db = client[d_name]
    tweets = db.GetTweets
    tweet_text = list(tweets.find({"text": {'$regex': searchstring, '$options': 'i'}}, {"_id": 0, "text": 1}))
    return tweet_text