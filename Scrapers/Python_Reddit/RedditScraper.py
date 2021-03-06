import praw
import pandas as pd
from praw.models import MoreComments

def subreddit(subred, reddit_read_only):
    return reddit_read_only.subreddit(subred)

def subreddit_scraper(subreddit): 

    # Display the name of the Subreddit
    print("Display Name:", subreddit.display_name)

    # Display the title of the Subreddit
    print("Title:", subreddit.title)

    # Display the description of the Subreddit
    print("Description:", subreddit.description)

def scrape(reddit_read_only):
    subreddit = reddit_read_only.subreddit("ffxiv")

    for post in subreddit.hot(limit=5):
        print(post.title)
        print()


def top_posts(subreddit):
    posts = subreddit.top("month")
    # Scraping the top posts of the current month

    posts_dict = {"Title": [], "Post Text": [],
              "ID": [], "Score": [],
              "Total Comments": [], "Post URL": []
              }

    for post in posts:
        # Title of each post
        posts_dict["Title"].append(post.title)

        # Text inside a post
        posts_dict["Post Text"].append(post.selftext)

        # Unique ID of each post
        posts_dict["ID"].append(post.id)

        # The score of a post
        posts_dict["Score"].append(post.score)

        # Total number of comments inside the post
        posts_dict["Total Comments"].append(post.num_comments)

        # URL of each post
        posts_dict["Post URL"].append(post.url)

        # Saving the data in a pandas dataframe
        top_posts = pd.DataFrame(posts_dict)
        #top_posts
        top_posts.to_csv("Top Posts.csv", index=True)

def post_scraper(reddit_read_only):
    # URL of the post
    url = "https://www.reddit.com/r/ffxiv/comments/u4zzrk/ishgardian_housing_lottery_megathread/"

    # Creating a submission object
    submission = reddit_read_only.submission(url=url)

    post_comments = []

    for comment in submission.comments:
        if type(comment) == MoreComments:
            continue

        post_comments.append(comment.body)

    # creating a dataframe
    comments_df = pd.DataFrame(post_comments, columns=['comment'])
    #comments_df
    comments_df.to_csv("Top Comments.csv", index=True)

def clear_file(output_file):
    # opening the file with w+ mode truncates the file
    f = open(output_file, "w+")
    f.close()    