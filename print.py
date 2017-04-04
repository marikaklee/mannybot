from TwitterFollowBot import TwitterBot
import sys

AUTOBOT = sys.argv[1:2] 
COMPUTER = 'marika.lee'


my_bot = TwitterBot()
my_bot.sync_follows()

def printNumbers():
    PROJECT = 'MannyBot'
    ACCOUNT = 'drmannylam'
    followingSum = sum(1 for line in open('following.txt'))
    followerSum = sum(1 for line in open('followers.txt'))

    print (ACCOUNT)
    print "FOLLOWING:",followingSum
    print "FOLLOWERS:",followerSum

printNumbers()
