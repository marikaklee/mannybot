from TwitterFollowBot import TwitterBot
import sys

AUTOBOT = sys.argv[1:2] 
COMPUTER = 'marika.lee'

if (AUTOBOT ==  ['M']):
    PROJECT = 'MannyBot'
    ACCOUNT = 'drmannylam'

if (AUTOBOT == ['T']):
    PROJECT = 'TestingBot'
    ACCOUNT = 'marikalee15'

if (AUTOBOT == ['J']):
    PROJECT = 'MannyBot'
    ACCOUNT = 'journalclubapp'

my_bot = TwitterBot()
my_bot.sync_follows()

def printNumbers():
    followingSum = sum(1 for line in open('following.txt'))
    followerSum = sum(1 for line in open('followers.txt'))

    print (ACCOUNT)
    print "FOLLOWING:",followingSum
    print "FOLLOWERS:",followerSum

printNumbers()
