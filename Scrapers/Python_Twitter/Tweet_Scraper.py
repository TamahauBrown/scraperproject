import tweepy
import pandas as pd

api_key = 'uIHijNe1Ss7bIwJq8Y6LhyHAy'
api_key_secret = 'Ge9M81dIdgrWiCDOjM4aYb8gTqxrrHaqHvMZNWiROlTqXa59eZ'

access_token = '2291659404-Lkkbhcw23RsxATfAFUcrPiGpQER362lycnPgryi'
access_token_secret = '4PFM0o0lc22Mk44XqUFgTFaekdVDSh6AzP1QlxlaVHIfW'

def auth():
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