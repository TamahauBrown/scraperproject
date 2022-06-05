from facebook_scraper import get_posts

if __name__ == '__main__':

    for post in get_posts('sss', pages=1):
         print(post['text'][:50])