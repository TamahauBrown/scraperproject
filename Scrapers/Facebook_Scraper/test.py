# fbmain.py but dataframes are concatenated, put into CSV, and results print to terminal

from facebook_scraper import get_posts
import pandas as pd

if __name__ == '__main__':
    # Make Dataframes for Post Attributes
    post_id = pd.DataFrame(columns = ['post_id'])
    post_time = pd.DataFrame(columns = ['time'])       
    post_user = pd.DataFrame(columns = ['username'])
    post_likes = pd.DataFrame(columns = ['likes'])
    post_comments = pd.DataFrame(columns = ['comments'])
    post_shares = pd.DataFrame(columns = ['shares'])
    post_text = pd.DataFrame(columns = ['text']) 
  
    i=0

    # For loop looping through posts
    for post in get_posts('nintendo', pages=3):

        #For each position [i] place post_attributes[i] into 'i' position in dataframe
        post_id.loc[i] = post['post_id']       
        post_time.loc[i] = post['time']
        post_user.loc[i] = post['username']
        post_likes.loc[i] = post['likes']
        post_comments.loc[i] = post['comments']
        post_shares.loc[i] = post['shares']
        post_text.loc[i] = post['text']
        
        i+=1

    # Concatenate dataframes into 1
    full_data = pd.concat([post_id, post_time, post_user, post_likes, 
                    post_comments, post_shares, post_text], axis = 1, join = 'inner')
    print(full_data)

    # Pandas puts dataframe into CSV
    full_data.to_csv('Data.csv', index = True)