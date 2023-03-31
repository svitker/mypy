import tweepy

# Set up your Twitter API keys and access tokens
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Create a new API object
api = tweepy.API(auth)

# Define the text of your tweet
tweet_text = "Hello, world! This is my first tweet from a bot."

# Send the tweet
api.update_status(tweet_text)
