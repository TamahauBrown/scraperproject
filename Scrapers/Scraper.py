from asyncio.windows_events import NULL
import praw
import os

class Scraper:
    def __init__(self):
        reddit = praw.Reddit(   client_id =     os.getenv("REDDIT_CLIENT_ID"), 
                                client_secret = os.getenv("REDDIT_CLIENT_SECRET"),
                                user_agent =    os.gentenv("REDDUT_USER_AGENT"))
        
        twitter = os.getenv('TWITTER_BEARER_TOKEN')
        facebook = NULL

def getReddit(scraper:Scraper()):
    scraper.reddit

def getTwitter(scraper:Scraper()):
    scraper.twitter