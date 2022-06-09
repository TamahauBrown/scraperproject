from facebook_scraper import get_posts
import pandas as pd

if __name__ == '__main__':
    # Make Dataframes for Post Attributes
    post_id = pd.DataFrame(columns = ['post_id', 'time', 'username', 'likes', 'comments', 'shares', 'text'])
#    post_time = pd.DataFrame(columns = ['time'])
#   post_user = pd.DataFrame(columns = ['username'])
#   post_likes = pd.DataFrame(columns = ['likes'])
#    post_comments = pd.DataFrame(columns = ['comments'])
#    post_shares = pd.DataFrame(columns = ['shares'])
#    post_text = pd.DataFrame(columns = ['text'])
  
    i=0

    # For loop looping through posts
    for post in get_posts('nintendo', pages=3):

        # For each position [i] place post_attribute[i] into 'i' position in dataframe
        post_id.loc[i] = [post['post_id'], post['time'], post['username'], post['likes'], post['comments'], post['shares'], post['text']]
 #       post_time.loc[i] = post['time']
 #       post_user.loc[i] = post['username']
#        post_likes.loc[i] = post['likes']
#        post_comments.loc[i] = post['comments']
#        post_shares.loc[i] = post['shares']
#        post_text.loc[i] = post['text']
        
        i+=1

    # Pandas puts dataframes into separate CSVs
    post_id.to_csv('Post_IDs.csv', index = True)
#    post_text.to_csv('Post_Text.csv', index = True)
#    post_time.to_csv('Post_Time.csv', index = True)
#    post_user.to_csv('Post_User.csv', index = True)
#    post_likes.to_csv('Post_Likes.csv', index = True)
#    post_comments.to_csv('Post_Comments.csv', index = True)
#cc    post_shares.to_csv('Post_Shares.csv', index = True)
