from facebook_scraper import get_posts
import pandas as pd
#import csv

if __name__ == '__main__':
    # Make Dataframe for Post ID
    post_id = pd.DataFrame(columns = ["post_id"])
    
    i=0

    # For loop looping through posts
    for post in get_posts('hershey', pages=3):

        #For each position [i] place post_id[i] into i position in dataframe
        post_id.loc[i] = post['post_id']
        print(post_id)
        
        i+=1

    # Pandas puts dataframe into CSV
    post_id.to_csv("Post_IDs.csv", index=True)