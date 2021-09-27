import snscrape.modules.twitter as sntwitter
import pandas as pd

# Creating list to append tweet data 
tweets_list = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('mRNA Vaccine since:2020-08-01 until:2021-08-31 min_retweets:50 min_faves:50').get_items()):
  
  # search tweets with "mRNA vaccine" from 1st August 2021 till 31st August 2021. Tweets are filtered based on a minimum of 50 retweets and 50 favourites.
  
   #declare a username 
    if i>100000: # keep number of tweets to a maximum of 100000.
        break
    tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.likeCount,tweet.retweetCount, tweet.replyCount, tweet.quoteCount]) #declare the attributes to be returned
    
# Creating a dataframe from the tweets list above 
df = pd.DataFrame(tweets_list, columns=['Datetime', 'Tweet Id', 'Text', 'Number of Likes', 'Number of Retweets', 'Number of Replies', 'Number of Quotes'])

df= df.sort_values(by=['Number of Retweets', 'Number of Likes'],ascending=False)

df.to_csv('vaccine_tweet.csv')
