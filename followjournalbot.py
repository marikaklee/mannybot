from TwitterFollowBot import TwitterBot


my_bot = TwitterBot()
my_bot.get_followers_list()

#my_bot.get_followers_list(self)
#--------automatically follow any users that tweet something with a specific phrase 
#my_bot.auto_follow("intermittentfasting", count=50)
#my_bot.auto_follow("#intermittentfasting", count=50)

#--------automatically follow any users that have followed me
#my_bot.auto_follow_followers(

#--------automatically follow any users that follow a user
my_bot.auto_follow_followers_of_user("@drericstrong", count=40)

#--------automatically favorite tweets that have a specific phrase
#my_bot.auto_fav("fasting", count=10)

#--------automatically retweet any tweets with specific phrase
#my_bot.auto_rt("cats", count=10)

#--------automatically unfollow any users that have not follow you back
my_bot.auto_unfollow_nonfollowers()

#--------automagically mute all users that you have followed
#my_bot.auto_mute_following()

#--------automagically unmute all users that you have muted
#my_bot.auto_unmute()
