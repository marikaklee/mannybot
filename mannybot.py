from TwitterFollowBot import TwitterBot
import random
import time
import gspread
from time import gmtime, strftime
import collections


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

#--------automatically reads file and send out tweets
def executeTweets():
	#TODO: put read files in read_files.txt
	#If read alerady, then go to the next line 
	tweetFile = open('/Users/marika.lee/Dropbox/mannyBot/mannytesting.txt');
	#doneFile = open('done.txt', "w")
	with tweetFile as f:
		for line in f:
			
			try:
				my_bot.send_tweet(line)
				#my_bot.send_tweet("Currently tweeting at..."+strftime("%H:%M", gmtime()))
				print "TWEETED: " + line
				#READ from Google excel - temporary from DropBox Excel sheet
				#TODO: WRITE to done.txt file 
				#TODO: be able to add in images 
				#TODO: add to text file while running
				#TODO restart server if exits

				#DrMannyLam: everday 9AM PST
				#JournalClub: 
				time.sleep(60)
			except:
				print "THIS TWEET HAS ALREADY BEEN TWEETTED."
				pass				
			
executeTweets()
#randomLine = (random.choice(list(file_)))
#my_bot.send_tweet(content);

#--------automatically follow any users that tweet something with a specific phrase 
#my_bot.auto_follow("cats", count=10)
#my_bot.auto_follow("#cats", count=10)

#--------automatically follow any users that have followed me
#my_bot.auto_follow_followers()

#--------automatically follow any users that follow a user
#my_bot.auto_follow_followers_of_user("marikalee15", count=10)

#--------automatically favorite tweets that have a specific phrase
#my_bot.auto_fav("fasting", count=10)

#--------automatically retweet any tweets with specific phrase
#my_bot.auto_rt("cats", count=10)

#--------automatically unfollow any users that have not follow you back
#my_bot.auto_unfollow_nonfollowers()

#--------automagically mute all users that you have followed
#my_bot.auto_mute_following()

#--------automagically unmute all users that you have muted
#my_bot.auto_unmute()

