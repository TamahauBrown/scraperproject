import tweepy
import pandas as pd

#api_key = ''
#api_key_secret = ''

#access_token = ''
#access_token_secret = ''

def auth(api_key, api_key_secret, access_token, access_token_secret):
    # authentication
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    return api.home_timeline()

def createdf(public_tweets):
    # create dataframe
    columns = ['Time', 'User', 'Tweet']
    data = []
    for tweet in public_tweets:
        data.append([tweet.created_at, tweet.user.screen_name, tweet.text])

    df = pd.DataFrame(data, columns=columns)

    df.to_csv('tweets.csv')

#if __name__ == '__main__':
#    public_tweets = auth()
#    createdf(public_tweets)