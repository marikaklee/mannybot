from TwitterFollowBot import TwitterBot
import random
import time
import gspread

my_bot = TwitterBot()
gc = gspread.authorize(credentials)

#--------automatically reads file and send out tweets
def executeTweets():
	#TODO: put read files in read_files.txt
	#If read alerady, then go to the next line 
	tweetFile = open('mannymessages.txt');
	doneFile = open('done.txt', "w")

	with tweetFile as f:
		for line in f:
			try:
				my_bot.send_tweet(line)
				print "TWEETED: " + line
				#READ from Google excel
				#TODO: WRITE to done.txt file 
				#TODO: be able to add in images 
				#TODO: add to text file while running
				time.sleep(60)
			except:
				pass				
			

while True:
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
#my_bot.auto_fav("cats", count=10)

#--------automatically retweet any tweets with specific phrase
#my_bot.auto_rt("cats", count=10)

#--------automatically unfollow any users that have not follow you back
#my_bot.auto_unfollow_nonfollowers()

#--------automagically mute all users that you have followed
#my_bot.auto_mute_following()

#--------automagically unmute all users that you have muted
#my_bot.auto_unmute()

