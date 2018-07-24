import tweepy
import csv

#Twitter API credentials
consumer_key = "w3RFCtjqIMhbghAKOlMr5S87R"
consumer_secret = "u2vvQipuq8Lj4KETw4Gv485ecrpAGpiWEuVDzzYuU4IQCbKHYK"
access_key = "803829949459296256-eKUb1zZVpu5Ik0J82fDgy2x3pDz0Vf9"
access_secret = "1euzY4XHpBNh1BeYzO7GlBCHtD80nopB4C8DqDssSzXlb"
#screen_name = "realDonaldTrump"

def getalltweets(screen_name):
	#Twitter only allows access to a users most recent 3240 tweets with this method
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
			
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print ("...%s tweets downloaded so far" % (len(alltweets)))
		
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.text.encode("utf-8")] for tweet in alltweets]
	
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)

	text_file = open("Output.txt", "w")
	text_file.write("%s" % outtweets)
	text_file.close()