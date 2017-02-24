#MannyBot
A Python Bot that automates sending tweets everyday and runs in the background.

##Capabilities:
- Configure time to tweet any time of the day
- Configure to run at an interval of time (every hour, day, week, etc)

##How to run:
- Change configuration in _init_.py 
```
OAUTH_TOKEN:****
OAUTH_SECRET:****
CONSUMER_KEY:****
CONSUMER_SECRET:****
TWITTER_HANDLE:marikalee15
```
- Create a folder within the MannyBot project folder
- Set the folder name to the variable 'twitterAccount' in mannybot.py
```
twitterAccount = 'marikalee15'
```
- Change filepath of textfile to read the tweets from
```
tweetFile = open('{FILE PATH}%s' % twitterAccount + '/tweets.txt');
```
- Run this command to execute this script in the background
```
nohup python mannybot.py &
```

##Python Dependencies
- pip install {all dependencies below}
```
TwitterFollowBot 
gspread 
urllib2 
twitter 
sched 
```
##Sources
- TwitterFollowBot 
