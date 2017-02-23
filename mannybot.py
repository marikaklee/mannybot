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

twitterAccount = 'drmannylam'
my_bot = TwitterBot()

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

#--------automatically reads file and send out tweets
def executeTweets():
	#If read already, then go to the next line 

	print '************'
	tweetFile = open('/Users/marika.lee/Dropbox/mannyBot/%s' % twitterAccount + '/tweets.txt');

	#catch exception is file is wrong
	tweetFile = open('tweets.txt');
	with tweetFile as f:
		for line in f:
			print "*****[{:%b %d | %H:%M}".format(datetime.today()),"] TWEET:",line,
			try:
				print "!!!SUCCESSFULL!!!"

				with open('textfiles/done.txt', 'a') as file:
					file.write(line)

				time.sleep(300)	 #5 minutes

			except TwitterError as err:
   				if err.e.code == 404:
   					print "ERROR 404 Page not found"
   				elif err.e.code == 403:
   					print "ERROR 403 Status is duplicate"
				else:
					print "ERROR ", err.e.code
						
	
def scheduler_reddit():	
	scheduler = sched.scheduler(time.time, time.sleep)
	scheduler.enter(0, 1, executeTweets(), ())
  	scheduler.run()

print "START TIME {:%H:%M:%S}".format(datetime.today())
while True:
  scheduler_reddit()


				#TODO check 140 characters
				#TODO read from Google excel - temporary from DropBox Excel sheet
				#TODO be able to add in images 
				#TODO add to text file while running
				#TODO restart server if exits
				#TODO Notification when tweet sent. email? text?



