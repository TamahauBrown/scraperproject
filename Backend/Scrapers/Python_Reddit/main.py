#From <file> import <method>
from RedditScraper import Subreddit_Scraper, Subreddit, Clear_File, Post_Scraper, Top_Posts
import praw

#Credentials
reddit_read_only = praw.Reddit(client_id="",                  # your client id
                               client_secret="",      # your client secret
                               user_agent="")                         # your user agent

if __name__ == '__main__':
    subreddit = Subreddit('geek', reddit_read_only)
    #Subreddit_Scraper(subreddit)
    Top_Posts(subreddit)