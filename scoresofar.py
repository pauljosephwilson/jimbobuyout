from sportsreference.ncaaf.teams import Teams
import buyouttweet
import bot
from sportsreference.ncaaf.boxscore import Boxscores



#get list of teams
teams = Teams()

#get list of teams from 2018
teams2018= Teams(year=2018)

#single out aggy
aggy = teams('TEXAS-AM')

#single out aggy 2018
aggy2018= teams2018('TEXAS-AM')

#determine amount paid to date
paid = int(75000000-buyouttweet.buyoutcalc)

#count of wins this year and so far
winsThisYear= aggy.wins
winsTotal=  aggy.wins+ aggy2018.wins

#game counter
gamesThisYear = aggy.wins + aggy.losses
gamesTotal= winsTotal + aggy.losses + aggy2018.losses
print(gamesThisYear, gamesTotal)

#conference wins math
conferenceWinsThisYear= aggy.conference_wins
conferenceWinsTotal= aggy.conference_wins + aggy2018.conference_wins

#calculate $ paid per point scored
moneyPerPoint2019=(paid/((aggy.points_per_game*4)))
moneyPerPointTotal=(paid/((aggy.points_per_game*4)+(aggy2018.points_per_game*13)))


#get rid of undefined while they still dont have a conference win
def confWinsCheck():
    float(moneyPerConferenceWin2019)
    if (conferenceWinsThisYear>= 1):
            moneyPerConferenceWin2019= (paid/conferenceWinsThisYear);
    else: moneyPerConferenceWin2019= 0

#calculateds money per conference wins since beginning of tenure
moneyPerConferenceWinTotal= (paid/conferenceWinsTotal)


#print checks to make sure it works

def statusUpdatePaid() :
    bot.updatestatus('Texas A&M has paid Jimbo $' + str('{:,.2f}'.format(paid)) + ' so far. That\'s $' + str('{:,.2f}'.format(moneyPerPointTotal)) + ' per point scored and $' + str('{:,.2f}'.format(moneyPerConferenceWinTotal)) + ' per conference win. #justmeansmore #SEC #TAMUfootball')
    print('done')
