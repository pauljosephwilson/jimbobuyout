
import tweepy
from datetime import date, datetime


consumer_key= 'A7W4xgF21W7qAa23u7V7hhvIC'
consumer_secret='xIqtm7fJgga0BFjX4IE4ZOTQPLNQBPuWK8VAwcubvbMpViNw07'
access_token = '1098063757006254080-mev9NsOgYXUKBjHWy6F5VrJJLnXpEw'
access_token_secret = 'XOud0ZDc9kmNFviCavHXxpo7PX7BCSQGDXnJMQsKwHUaJ'

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api= tweepy.API(auth)


d0= date(2018,1,1)
d1= date.today()
daysbetween= abs(d1-d0)
print(d0)
print(d1)
print(daysbetween.days)
print(10000/daysbetween.days)

buyoutcalc = 75000000-((7500000/365)*daysbetween.days)
buyout= int(buyoutcalc)
print(buyout)

user=api.me()
print(user.name)

api.update_status('If he were fired today, Jimbo Fisher would be owed $'+ str(buyout)+ ' by Texas A&M #12thman #wrts #gigemgang2020')
print('done')
