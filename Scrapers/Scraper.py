from asyncio.windows_events import NULL
import praw
import os
import Tweet_Scraper as ts

class Scraper:
    #All information is gathered through the system environment variables under the name
    def __init__(self):
        #Reddit authentication credentials
        reddit = praw.Reddit(   client_id           =       os.getenv("REDDIT_CLIENT_ID"), 
                                client_secret       =       os.getenv("REDDIT_CLIENT_SECRET"),
                                user_agent          =       os.gentenv("REDDUT_USER_AGENT")
                                )
        
        #Twitter authentication credentials
        twitter = ts.auth(      os.getenv("TWITTER_API_KEY"),
                                os.getenv("TWITTER_API_KEY_SECRET"),
                                os.getenv("TWITTER_ACCESS_TOKEN"),
                                os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
                                )
        facebook = NULL

#Gets credential information for Reddit
def getReddit(scraper:Scraper()):
    scraper.reddit

#Gets credential information for Twitter
def getTwitter(scraper:Scraper()):
    scraper.twitter