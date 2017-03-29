from TwitterFollowBot import TwitterBot
import sys

AUTOBOT = sys.argv[1:] 

my_bot = TwitterBot()
my_bot.sync_follows()


if (AUTOBOT ==  ['M']):
	my_bot.auto_follow("intermittentfasting", count=50)
	my_bot.auto_follow("keto", count=50)
	my_bot.auto_follow("#keto", count=50)
	my_bot.auto_follow("ketogenic", count=50)
	my_bot.auto_follow("#ketogenic", count=50)
	my_bot.auto_follow("lchf", count=50)
	my_bot.auto_follow("#nutrition", count=50)

if (AUTOBOT == ['J']):
	my_bot.auto_follow("stanford", count=100)
	my_bot.auto_follow("stanford", count=100)
	my_bot.auto_follow("#stanford", count=50)
	my_bot.auto_follow("stanfordmed", count=50)
	my_bot.auto_follow("#stanfordmed", count=50)
	my_bot.auto_follow("medicine", count=150)
	my_bot.auto_follow("#medicine", count=50)

