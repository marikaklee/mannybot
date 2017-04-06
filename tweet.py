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
import sys

AUTOBOT = sys.argv[1:2] 
print(AUTOBOT)
WHEN = sys.argv[2:3]

TYPE = 'HOME'
PROJECT = ''
ACCOUNT = ''
QUEUE = 'tweets'

#-------------HOW TO RUN-------------
# python mannybot.py M
#------------------------------------

if (AUTOBOT ==  ['M']):
	PROJECT = 'MannyBot'
	ACCOUNT = 'drmannylam'

if (AUTOBOT == ['T']):
	PROJECT = 'TestingBot'
	ACCOUNT = 'marikalee15'

if (AUTOBOT == ['J']):
	PROJECT = 'MannyBot'
	ACCOUNT = 'journalclubapp'

if (TYPE == 'HOME'):
	COMPUTER = 'marikalee'

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
	# if (is_connected() == False):
	# 	time.sleep(5)
	# 	print "Trying to connect to wifi.."
	# 	executeTweets()

	print(PROJECT)
	TWEETSPATH = '/Users/%s/Dropbox/%s/%s/tweets/%s.txt' % (COMPUTER, PROJECT, ACCOUNT, QUEUE)
	DONEPATH = '/Users/%s/Dropbox/%s/%s/done/%s_done.txt' % (COMPUTER, PROJECT, ACCOUNT, QUEUE)
	
	# TWEETSPATH = '/Users/%s/Dropbox/%s/%s/tweets/glossary.txt' % (COMPUTER, PROJECT, ACCOUNT)
	# DONEPATH = '/Users/%s/Dropbox/%s/%s/done/done.txt' % (COMPUTER, PROJECT, ACCOUNT)
	
	print(TWEETSPATH)

	file = open(TWEETSPATH, 'r')
	lines = file.readlines()

	if (len(lines) < 1):
		print "Trying to find tweets to tweet..."
		time.sleep(5)
		executeTweets()

	count = 0
	tweet = ''
	
	if ("RULERRULERRULER" not in tweet and "LATER:" not in tweet):
		tweet = lines[0]
	else:	
		while ("RULERRULERRULER" not in tweet and "LATER:" not in tweet):
			count = count + 1
			tweet = lines[count]

	print "[{:%b %d | %H:%M}".format(datetime.today()) + "]", str(tweet),
	
	#CHECK SPACE!
	#if just ruler

	try:
		if "RULERRULERRULER" not in tweet and "LATER:" not in tweet:
			my_bot.send_tweet(tweet)
			print "[SUCCESSFUL]"
			open(DONEPATH, 'a').writelines(tweet)
			
			if (count == 0):
				open(TWEETSPATH, 'w').writelines(lines[1:len(lines)])
			else:  
				open(TWEETSPATH, 'w').writelines(lines[0:count])
				open(TWEETSPATH, 'a').writelines(lines[count+1:len(lines)])


	

	except TwitterError as err:
		if err.e.code == 401:
			print ("[ERROR 401 Token expired")
   		if err.e.code == 404:
   			print ("ERROR 404 Page not found")
   			executeTweets()
   		elif err.e.code == 403:
   			print ("ERROR 403 Status is duplicate")
   			open(DONEPATH, 'a').writelines(tweet)
			open(TWEETSPATH, 'w').writelines(lines[1:len(lines)])
			executeTweets()
		else:
			print ("ERROR ", err.e.code)
	


if (WHEN == ['now']):
	executeTweets()		

if (WHEN == ['twice']):
	schedule.every().day.at("06:30").do(executeTweets)
	executeTweets()		

#schedule.every(1).minutes.do(executeTweets)
#schedule.every().hour.do(job)
schedule.every().day.at("06:30").do(executeTweets)
#my_bot.sync_follows()


while 1:
    schedule.run_pending()
    time.sleep(1)

