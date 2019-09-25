# authorizations for bot
consumer_key= 'A7W4xgF21W7qAa23u7V7hhvIC'
consumer_secret='xIqtm7fJgga0BFjX4IE4ZOTQPLNQBPuWK8VAwcubvbMpViNw07'
access_token = '1098063757006254080-mev9NsOgYXUKBjHWy6F5VrJJLnXpEw'
access_token_secret = 'XOud0ZDc9kmNFviCavHXxpo7PX7BCSQGDXnJMQsKwHUaJ'

auth= tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api= tweepy.API(auth)

#calculate first tweet
d0= date(2018,1,1)
d1= date.today()
daysbetween= abs(d1-d0)
print(d0)
print(d1)
print(daysbetween.days)
print(10000/daysbetween.days)

buyoutcalc = 75000000-((7500000/365)*daysbetween.days)

lumpdate= date.today()+datetime.timedelta(days=60)

buyout= int(buyoutcalc)

lumpsum= buyout*.25

def moneyupdate():
    api.update_status('If he were fired today, Jimbo Fisher would be owed $'+ str('{:,.2f}'.format(buyout))+ ' by Texas A&M, with $' +str('{:,.2f}'.format(lumpsum))+' due by '+ lumpdate.strftime('%B %d')+' #12thman #wrts #gigemgang2020')
    print('done')




