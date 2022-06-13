#From <file> import <method>
from RedditScraper import subreddit_scraper, subreddit, clear_file, post_scraper, top_posts
import praw

#Credentials
#reddit_read_only = praw.Reddit(client_id="",                  # your client id
#                               client_secret="",      # your client secret
#                               user_agent="")                         # your user agent

if __name__ == '__main__':
    subreddit = subreddit('geek', reddit_read_only)
    #Subreddit_Scraper(subreddit)
    top_posts(subreddit)