import praw
import pandas as pd
from praw.models import MoreComments
import keyring

# r/abortion  
# r/abrathatfits    
# r/amipregnant   
# r/askdocs    
# r/birthcontrol      
# r/endo     
# r/menopause   
# r/periods  
# r/vaginismus

subredditsToRead = ["womenshealth", "abortion", "amipregnant", "birthcontrol", "periods", "skincareaddiction", "twoxchromosomes"]
numberTopPostsToRead = 100
periodTopPosts = "year"
hashmapPosts = {}

#Set up your keyring using keyring.set_password('reddit', 'client_secret', '<secret key>')
clientSecret = keyring.get_password('reddit', 'client_secret') 
reddit_read_only = praw.Reddit(client_id="toUB0mGKbyzPwepWj3hVrw",         # your client id
                               client_secret=clientSecret,      # your client secret
                               user_agent="genZ Hot Topics 1.0 dsAnalysis")        # your user agent
 
for subredditName in subredditsToRead:
    subreddit = reddit_read_only.subreddit(subredditName)
    
    # Display the name of the Subreddit
    print("Display Name:", subreddit.display_name)
    
    # Display the title of the Subreddit
    # print("Title:", subreddit.title)
    
    # Display the description of the Subreddit
    # print("Description:", subreddit.description)


    # for post in subreddit.hot(limit=numberTopPostsToRead):
    #     # print(post.title)
    #     print()
        

    posts = subreddit.top(periodTopPosts)
    # Scraping the top posts of the current month
    
    # posts_dict = {"Title": [], "Post Text": [],
    #             "ID": [], "Score": [],
    #             "Total Comments": [], "Post URL": []
    #             }
    # counter = 0
    # for post in posts:
    #     # Title of each post
    #     posts_dict["Title"].append(post.title)
        
    #     # Text inside a post
    #     posts_dict["Post Text"].append(post.selftext)
        
    #     # Unique ID of each post
    #     posts_dict["ID"].append(post.id)
        
    #     # The score of a post
    #     posts_dict["Score"].append(post.score)
        
    #     # Total number of comments inside the post
    #     posts_dict["Total Comments"].append(post.num_comments)
        
    #     # URL of each post
    #     posts_dict["Post URL"].append(post.url)

        # counter += 1
        # if counter > 2:
        #     break
    
    # Saving the data in a pandas dataframe
    # top_posts = pd.DataFrame(posts_dict)
    # top_posts

    post_comments = []
    post_title = []
    post_body = []
    
    counter = 0
    for post in posts:
        # print(post)
        submission = reddit_read_only.submission(url=post.shortlink)
        # print(submission.selftext)
        post_comments.append(submission.title + ' ' + submission.selftext)
        for comment in submission.comments:
            if type(comment) == MoreComments:
                continue
        
            post_comments.append(comment.body)
            post_title.append(submission.title)
            post_body.append(submission.selftext)
    
    # creating a dataframe
    post_comments = pd.DataFrame(post_comments, columns = ['post_comments'])
    post_title = pd.DataFrame(post_title, columns = ['post_title'])
    post_body = pd.DataFrame(post_body, columns = ['post_body'])
    comments_df = pd.concat([post_title, post_body, post_comments], names = ['post_title', 'post_body', 'post_comments'], axis = 1)
    # comments_df = pd.DataFrame(post_comments, columns=['comment'])
    comments_df.to_csv("CommentsInTopPosts_" + subredditName + ".csv")
# print("here")
    # hashmapPosts[subredditName] = comments_df
# postsDF = pd.DataFrame(hashmapPosts, columns = ["Posts"])
    
# print("here") 