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
import socket
import sys
import glob


AUTOBOT = sys.argv[1:2] 
WHEN = sys.argv[2:3]

TYPE = 'WORK'
PROJECT = ''
ACCOUNT = ''
QUEUE = ''
COMPUTER = ''
QUEUE = ''

REMOTE_SERVER = "www.google.com"

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

if (TYPE =='WORK'):
	COMPUTER = 'marika.lee'


QUEUE_LIST_PATH = '/Users/%s/Dropbox/%s/%s/queues/list.txt' % (COMPUTER, PROJECT, ACCOUNT)
QUEUE_DONE_PATH = '/Users/%s/Dropbox/%s/%s/queues/done.txt' % (COMPUTER, PROJECT, ACCOUNT)

files = glob.glob('/Users/%s/Dropbox/%s/%s/tweets/*.txt' % (COMPUTER, PROJECT, ACCOUNT))
last = ''
for i in range(0, len(files)):
	check = files[i].split('/')[7].rstrip('.txt')
	files[i]= check
open(QUEUE_LIST_PATH, 'w').writelines(files)
	
TWEETS_PATH = '/Users/%s/Dropbox/%s/%s/tweets/%s.txt' % (COMPUTER, PROJECT, ACCOUNT, QUEUE)
DONE_PATH = '/Users/%s/Dropbox/%s/%s/done/%s_done.txt' % (COMPUTER, PROJECT, ACCOUNT, QUEUE)

with open(QUEUE_DONE_PATH, 'rb') as fh:
    last = fh.readlines()[-1]

if (last == files[len(files)-1]):
	QUEUE = files[0]
else:
	for i in range(0, len(files)):
		if (last == files[i]):
			QUEUE = files[i+1]


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
		print "Trying to connect to wifi.."
		executeTweets()

	try:
		file = open(TWEETS_PATH, 'r')
	except:
		file = open(TWEETS_PATH, 'a')

	lines = file.readlines()

	if (len(lines) < 1):
		print "Trying to find tweets to tweet..."
		time.sleep(10)
		executeTweets()

	count = 0
	tweet = lines[0]
	
	if ("=====" not in tweet and "LATER:" not in tweet):
		tweet = lines[0]
	else:	
		while ("=====" in tweet or "LATER:" in tweet):
			count = count + 1
			tweet = lines[count]

	print "[{:%b %d | %H:%M}".format(datetime.today()) + "]", str(tweet),
	
	try:
		if "("====="" not in tweet and "LATER:" not in tweet:
			#my_bot.send_tweet(tweet)
			print "[SUCCESSFUL]"
			open(DONE_PATH, 'a').writelines(tweet)

			
			if (count == 0):
				open(TWEETS_PATH, 'w').writelines(lines[1:len(lines)])
			else:  
				open(TWEETS_PATH, 'w').writelines(lines[0:count])
				open(TWEETS_PATH, 'a').writelines(lines[count+1:len(lines)])

			open(QUEUE_DONE_PATH, 'a').writelines(QUEUE)

	

	except TwitterError as err:
		if err.e.code == 401:
			print ("[ERROR 401 Token expired")
   		if err.e.code == 404:
   			print ("ERROR 404 Page not found")
   			executeTweets()
   		elif err.e.code == 403:
   			print ("ERROR 403 Status is duplicate")
   			open(DONE_PATH, 'a').writelines(tweet)
			open(TWEETS_PATH, 'w').writelines(lines[1:len(lines)])
			executeTweets()
		else:
			print ("ERROR ", err.e.code)
	


if (WHEN == ['now']):
	executeTweets()		
#schedule.every(1).minutes.do(executeTweets)
#schedule.every().hour.do(job)
#schedule.every().day.at("06:30").do(executeTweets)
#my_bot.sync_follows()


while 1:
    schedule.run_pending()
    time.sleep(1)



