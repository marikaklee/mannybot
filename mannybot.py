import schedule
from TwitterFollowBot import TwitterBot
import random
import time
import gspread
from time import gmtime, strftime
from datetime import datetime, date
from threading import Timer
import urllib2
from twitter import Twitter, TwitterError, TwitterHTTPError
import sched

TWITTER_ACCOUNT = 'marikalee15'
TWEET_TIME = 1; #4PM

#---------Read from Google Spreadsheet file
# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# scope = ['https://spreadsheets.google.com/feeds']
# credentials = ServiceAccountCredentials.from_json_keyfile_name('tweetbotpy.json', scope)
# gc = gspread.authorize(credentials)
# wks = gc.open("Where is the money Lebowski?").sheet1

# import gspread
# from oauth2client.service_account import ServiceAccountCredentials
# #scope = ["https://docs.google.com/spreadsheets/d/pip install -t lib httplib2-z65q5uFHvvdH1Zn5gzM/edit?usp=sharing"]
# scope = ["https://spreadsheets.google.com/feeds"]
# credentials = ServiceAccountCredentials.from_json_keyfile_name("tweetbot.json", scope)
# gc = gspread.authorize(credentials)
# wks = gc.open_by_url("https://docs.google.com/spreadsheets/d/1tWDAdHesWTZKu53OYWRlVoEm_tzi8UtLrkD95Piumkg/edit#gid=0").sheet1
# print wks.acell("A1").value
# print wks.cell(1,1).value

my_bot = TwitterBot()

def executeTweets():
	#lines = open('/Users/marika.lee/Dropbox/mannyBot/%s' % TWITTER_ACCOUNT + '/tweets.txt').readLines()
	lines = open('tweets.txt').readlines()

	if (len(lines) < 1):
		return

	tweet = lines[0]

	open('done.txt', 'w').writelines(tweet)
	open('tweets.txt', 'w').writelines(lines[1:len(lines)])

	print "[{:%b %d | %H:%M}".format(datetime.today()) + "] Tweeting...", tweet,

	try:
		if datetime.now().hour == TWEET_TIME:
			my_bot.send_tweet(tweet)
			print "!!!SUCCESSFULL TWEET!!!"

	except TwitterError as err:
   		if err.e.code == 404:
   			print "ERROR 404 Page not found"
   		elif err.e.code == 403:
   			print "ERROR 403 Status is duplicate"
		else:
			print "ERROR ", err.e.code
			
schedule.every(.1).minutes.do(executeTweets)
#schedule.every().hour.do(job)
#schedule.every().day.at(str(TWEET_TIME)).do(executeTweets)

while 1:
    schedule.run_pending()
    time.sleep(1)



