import schedule
from TwitterFollowBot import TwitterBot
import random
import time
from time import gmtime, strftime
from datetime import datetime, date
from threading import Timer
import urllib2
from twitter import Twitter, TwitterError, TwitterHTTPError
import sched
import socket
import sys

AUTOBOT = sys.argv[1:2] 
print(AUTOBOT)
WHEN = sys.argv[2:3]

TYPE = 'WORK'
PROJECT = 'MannyBot'
ACCOUNT = ''
QUEUE = 'tweets'

#-------------HOW TO RUN-------------
# python mannybot.py M
#------------------------------------
now = datetime.now()

if (AUTOBOT ==  ['M']):
	if (now.isoweekday() == 1):
		QUEUE = 'clinical'
	if (now.isoweekday() == 2):
		QUEUE = 'diabetes'
	if (now.isoweekday() == 3):
		QUEUE = 'fasting'
	if (now.isoweekday() == 4):
		QUEUE = 'lowcarb'
	if (now.isoweekday() == 5):
		QUEUE = 'telomeres'
	ACCOUNT = 'drmannylam'

if (AUTOBOT == ['T']):
	PROJECT = 'TestingBot'
	ACCOUNT = 'marikalee15'

if (AUTOBOT == ['J']):
	if (now.isoweekday() == 1):
		QUEUE = 'glossary'
	ACCOUNT = 'journalclubapp'

if (TYPE == 'HOME'):
	COMPUTER = 'marikalee'

if (TYPE == 'WORK'):
	COMPUTER = 'm0l01bz'

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

	global QUEUE
	TWEETSPATH = '/Users/%s/Dropbox/%s/%s/tweets/%s.txt' % (COMPUTER, PROJECT, ACCOUNT, QUEUE)
	DONEPATH = '/Users/%s/Dropbox/%s/%s/done/%s_done.txt' % (COMPUTER, PROJECT, ACCOUNT, QUEUE)

	file = open(TWEETSPATH, 'r')
	lines = file.readlines()

	if (len(lines) < 1):
		print "Trying to find tweets to tweet from", QUEUE, "..."
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

	if ("RULERRULERRULER" in tweet or "LATER:" in tweet):
		if (QUEUE == 'clinical'):
			QUEUE = 'diabetes'
		if (QUEUE == 'diabetes'):
			QUEUE = 'fasting'
		if (QUEUE == 'fasting'):
			QUEUE = 'lowcarb'
		if (QUEUE == 'telomeres'):
			QUEUE = 'tweets'
		if (QUEUE == 'tweets'):
			QUEUE = 'clinical'
		executeTweets()

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

