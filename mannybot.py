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
import gspread
import socket

#-------------SET VARIABLES HERE ONLY-------------
AUTOBOT = 'TESTING'
TYPE = 'HOME'
#-------------------------------------------------

if (AUTOBOT ==  'MANNY'):
	PROJECT = 'MannyBot'
	ACCOUNT = 'drmannylam'

if (AUTOBOT == 'TESTING'):
	PROJECT = 'TestingBot'
	ACCOUNT = 'marikalee15'

if (TYPE == 'HOME'):
	COMPUTER = 'marikalee'

if (TYPE =='WORK'):
	COMPUTER = 'marika.lee'

#PROJECT = 'TestingBot'
#ACCOUNT = 'marikalee15'
TWEET_TIME = 11; #9AM
REMOTE_SERVER = "www.google.com"

def is_connected():
  try:
    host = socket.gethostbyname(REMOTE_SERVER)
    s = socket.create_connection((host, 80), 2)
    return True
  except:
     pass
  return False
print is_connected()


my_bot = TwitterBot()
def executeTweets():

	if (is_connected() == False):
		time.sleep(5)
		executeTweets()

	TWEETSPATH = '/Users/%s/Dropbox/%s/%s/tweets.txt' % (COMPUTER, PROJECT, ACCOUNT)
	DONEPATH = '/Users/%s/Dropbox/%s/%s/done.txt' % (COMPUTER, PROJECT, ACCOUNT)
	
	file = open(TWEETSPATH, 'r')
	lines = file.readlines()

	if (len(lines) < 1):
		print "---------------NO MORE TWEETS LEFT---------------"
		return

	tweet = lines[0]

	if ("RULERRULERRULER" in tweet):
		tweet = lines[1]

	print "[{:%b %d | %H:%M}".format(datetime.today()) + "] Tweeting...", str(tweet)

	open(DONEPATH, 'a').writelines(tweet)
	open(TWEETSPATH, 'w').writelines(lines[1:len(lines)])
	
	try:
		if datetime.now().hour == TWEET_TIME:
			my_bot.send_tweet(tweet)
			print "---------------SUCCESSFULL TWEET---------------"
	except TwitterError as err:
   		if err.e.code == 404:
   			print ("ERROR 404 Page not found")
   		elif err.e.code == 403:
   			print ("ERROR 403 Status is duplicate")
		else:
			print ("ERROR ", err.e.code)
	

print "---------------MANNYBOT HAS STARTED---------------"
#executeTweets()		
#schedule.every(1).minutes.do(executeTweets)
#schedule.every().hour.do(job)

schedule.every().day.at("11:50").do(executeTweets)


while 1:
    schedule.run_pending()
    time.sleep(1)


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


