#!/usr/bin/env python
# coding: utf-8

# Get Tweets From @username and Write to txt



#### Firstly setting up libraries

import tweepy
from datetime import datetime



#### Twitter API requirements

consumer_key = 'YOUR_CONSUMER_KEY'
consumer_secret = 'YOUR_CONSUMER_SECRET'
access_token = 'YOUR_ACCESS_TOKEN'
access_token_secret = 'YOUR_ACCESS_SECRET'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth)



#### Getting username

print("Write a username who you want to get tweets.")
username = input("username: @")



#### Defining variables

userAllInfo = api.get_user(screen_name = username)

userId = userAllInfo.id
print(username +"'s id: " + str(userId) + "\n PS: May be you want to keep that ID for possible changing username")

screenName = userAllInfo.screen_name
name = userAllInfo.name

dateTime = datetime.now()
time = datetime.strftime(dateTime, '%m_%d_%y__%H_%M_%S')

tweetCount = 1

fileName = "All_Tweets_From_@"+screenName+"_Until_"+str(time)+".txt"



#### Writing tweets to txt

with open(fileName, "w") as f:

    f.write("All Tweets From @"+screenName+" Until " + str(time))
    f.write("\n")
    f.write("---------------------")
    
    for status in tweepy.Cursor(api.user_timeline, user_id = userId,
                                tweet_mode="extended", exclude_replies= False,
                                include_rts = True).items():

        try:
            f.write("\n")
            f.write("Tweet No: " + str(tweetCount) + "\n")
            f.write("\n")
            f.write(name + " @" + screenName + " :\n")
            f.write(status.full_text + "\n")
            f.write("\n")
            f.write(str(status.created_at) + "\n")
            f.write("\n")
            f.write("---------------------")
            f.write("\n")
        except UnicodeEncodeError:
            f.write(status.full_text.encode('unicode-escape').decode('utf-8') + "\n")
            
        tweetCount += 1
    
    f.write("\n")
    f.write("---------------------")
    f.write("\n")
    f.write(str((tweetCount - 1))+" Tweets from @"+screenName+" successfully extracted.") 
    f.close()

print(str((tweetCount - 1))+" Tweets from @"+screenName+" successfully extracted. Look up your txt file to see tweets.")



###### After seconds you will see tweets in txt file.





