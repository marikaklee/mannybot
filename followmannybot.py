from TwitterFollowBot import TwitterBot


my_bot = TwitterBot()

#my_bot.sync_follows()
#--------automatically follow any users that tweet something with a specific phrase 

my_bot.auto_unfollow_nonfollowers()

# my_bot.auto_follow("keto", count=50)
# my_bot.auto_follow("#keto", count=50)
# my_bot.auto_follow("ketogenic", count=50)
# my_bot.auto_follow("#ketogenic", count=50)
# my_bot.auto_follow("lchf", count=50)
# my_bot.auto_follow("#nutrition", count=50)
my_bot.auto_follow("stanford", count=100)
my_bot.auto_follow("#stanford", count=50)
my_bot.auto_follow("stanfordmed", count=50)
my_bot.auto_follow("#stanfordmed", count=50)
my_bot.auto_follow("medicine", count=150)
my_bot.auto_follow("#medicine", count=50)

# following = sum(1 for line in open('following.txt'))
# followers = sum(1 for line in open('followers.txt'))

# def execute():

# 	if (followers > following):
# 		my_bot.auto_follow("keto", count=50)
# 		my_bot.auto_follow("ketogenic", count=50)
# 		my_bot.auto_follow("lowcarb", count=50)
# 		my_bot.auto_follow("lchf", count=50)

# 	else:
# 		my_bot.auto_unfollow_nonfollowers()






#--------automatically follow any users that have followed me
#my_bot.auto_follow_followers(

#--------automatically follow any users that follow a user
#my_bot.auto_follow_followers_of_user("@dietdoctor1", count=8000)

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
