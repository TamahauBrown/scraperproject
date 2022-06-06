from facebook_scraper import get_posts

if __name__ == '__main__':
    print("test")

    for post in get_posts('nintendo', pages=1):
        print(post['text'][:50])