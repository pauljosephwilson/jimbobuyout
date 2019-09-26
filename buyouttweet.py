import bot
from datetime import date
import datetime

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
    bot.updatestatus('If he were fired today, Jimbo Fisher would be owed $'+ str('{:,.2f}'.format(buyout))+ ' by Texas A&M, with $' +str('{:,.2f}'.format(lumpsum))+' due by '+ lumpdate.strftime('%B %d')+' #12thman #wrts #gigemgang2020')
    print('done')
