import tweepy
from tweepy import OAuthHandler
import pandas as pd
import CREDENTIALS
import json
import csv
from datetime import datetime
# CREATE THE AUTHENTICATION OBJECT
auth = OAuthHandler(CREDENTIALS.consumer_key, CREDENTIALS.consumer_secret)

# SET THE ACCESS TOKEN AND THE TOKEN SECRET
auth.set_access_token(CREDENTIALS.access_token, CREDENTIALS.access_token_secret)

# CREATE THE API OBJECT WHILE PASSING IN THE AUTHENTICATION INFORMATION
api = tweepy.API(auth, wait_on_rate_limit=True)
# scraping
terms = input("Insert name of the candidate to extract :")
tweet_amount = int(input(" Enter number of tweets to extract: "))
# Name of csv file to be created
fname = terms

# Extracting the tweets
tweets = tweepy.Cursor(api.search_tweets, q=terms+' -filter:retweets',tweet_mode='extended', lang='en').items(tweet_amount)
# Open the spreadsheet
with open('%s.csv' % (fname), 'w', encoding="utf-8") as file:
    w = csv.writer(file)

    # Write header row (feature column names of your choice)
    w.writerow(['timestamp', 'tweet_text', 'username',  'location',
                'followers_count', 'retweet_count', 'favorite_count'])
    for tweet in tweets:
        w.writerow([tweet.created_at,
                    tweet,
                    tweet.user.screen_name,
                    tweet.user.location,
                    tweet.user.followers_count,
                    tweet.retweet_count,
                    tweet.favorite_count])
        print(tweet)





