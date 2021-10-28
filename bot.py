import tweepy
from datetime import date
from sportsreference.ncaaf.teams import Teams


# authorizations for bot
consumer_key= 'key'
consumer_secret='key'
access_token = 'key'
access_token_secret = 'key'

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api= tweepy.API(auth)

def updatestatus(x):
    api.update_status(x)
