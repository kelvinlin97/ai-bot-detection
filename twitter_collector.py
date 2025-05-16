# twitter_collector.py
import tweepy
import os
import json

# Replace with your own API keys
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)

def fetch_tweets(query, max_results=100):
    tweets = client.search_recent_tweets(query=query, tweet_fields=["author_id", "created_at", "text"], max_results=max_results)
    data = []
    for tweet in tweets.data:
        data.append({
            "platform": "twitter",
            "user_id": tweet.author_id,
            "text": tweet.text,
            "timestamp": tweet.created_at.isoformat()
        })
    return data

if __name__ == "__main__":
    tweets = fetch_tweets("chatgpt")
    with open("data/twitter/tweets.json", "w") as f:
        json.dump(tweets, f, indent=2)
