import tweepy
from datetime import date
from sportsreference.ncaaf.teams import Teams


# authorizations for bot
consumer_key= 'A7W4xgF21W7qAa23u7V7hhvIC'
consumer_secret='xIqtm7fJgga0BFjX4IE4ZOTQPLNQBPuWK8VAwcubvbMpViNw07'
access_token = '1098063757006254080-mev9NsOgYXUKBjHWy6F5VrJJLnXpEw'
access_token_secret = 'XOud0ZDc9kmNFviCavHXxpo7PX7BCSQGDXnJMQsKwHUaJ'

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api= tweepy.API(auth)

def updatestatus(x):
    api.update_status(x)
