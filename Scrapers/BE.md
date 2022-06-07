# Python Scrapers
The backend primarily relies on three platforms to extract information: Reddit, Twitter and Facebook. All three platforms require you to have access to their developer portal with an API key in order to extract information. 

| API | Developer Portal |
| ----------- | ----------- |
| Reddit | https://www.reddit.com/prefs/apps |
| Twitter | https://developer.twitter.com/en/portal/dashboard |
| Facebook | https://developers.facebook.com/ |

### **Prerequisites:**
1. Python 3.0 or greater
2. Python Anaconda
3. IDE which supports Python 3.0 or greater (we use Visual Studio Code)
 
## Reddit
----

### **Useful pages:**
| Page Name | Description |
| --------- | ---- |
| [Terms of Use](https://docs.google.com/a/reddit.com/forms/d/e/1FAIpQLSezNdDNK1-P8mspSbmtC2r86Ee9ZRbC66u929cG2GX0T9UMyw/viewform) | This page explains the terms of service regarding the Reddit API |
| [API Information](https://www.reddit.com/dev/api) | This explains information on how the API is used |
| [Developer Portal](https://www.reddit.com/prefs/apps) | You can create your application here with information explaining the purpose of your project. The Reddit application requires you to have a **redirecturl**, **name**, and **description** |

### **How to use the API:**
The Reddit API is able to gather the data provided by the user which provides the name of the subreddit they wish to access and how they wish to filter their information, an example of this is: Top posts filter (See figure 1).

![alt text](ffxiv_subreddit.png)
> Figure 1: Where to find filters on Reddit for top posts

Currently only the top posts feature is working for a basic application to test connection where it will turn the information into a Pandas dataframe and write the information to a csv file called 'TopPosts.csv'. This will allow the Front end team to be able to grab the dataframe and use the information for graphing purposes or display the information to the user.

### Important Libraries:
| Library | Description |
| ------- | ----------- |
| [Pandas](https://pypi.org/project/pandas/) | Our primary dataframe which will take the extracted information and be used to pass the information to display to the Rust environment on the front end while being able to create a data file (.csv) if requested from the front end. |
| [Praw](https://praw.readthedocs.io/en/stable/) | Primarily used with Reddit in order to gather the API key information. |
| [Praw.models](https://praw.readthedocs.io/en/stable/code_overview/praw_models.html?highlight=models) | Using the MoreComments feature to check against the Reddit API which will continue until all relevant comments on a post have been added. 
| [RedditScraper]() | Connects with the Reddit developer API to connect the API key provided by the user to allow Python to extract the relevant information and be able to extract the information for the Pandas Dataframe. |



## Twitter
----

### **Useful pages:**
| Page Name | Description |
| --------- | ---- |
| [Terms of Use](https://developer.twitter.com/en/developer-terms/agreement-and-policy) | This is a standard terms of use for the Twitter API |
| [API Information](https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2) | This is a document which explains all of Twitter's APIs that can be used, in this project we use TwitterAPI|
| [Developer Portal](https://developer.twitter.com/en/portal/dashboard) | Where you can access the developer portal. |

### Important Libraries:
| Library | Description |
| ------- | ----------- |
| [os](https://docs.python.org/3/library/os.html) | Primarily used to gather the API token provided by the user to pass into a request in order to access the Twitter API Service.|
| [requests](https://pypi.org/project/requests/) | Makes HTTP requests to Twitter to authenticate and extract information. |
| [Pandas](https://pypi.org/project/pandas/) | Our primary dataframe which will take the extracted information and be used to pass the information to display to the Rust environment on the front end while being able to create a data file (.csv) if requested from the front end |

## Facebook/Meta
----
### **Useful pages:**
| Page Name | Description |
| --------- | ---- |
| [Terms of Use](https://developers.facebook.com/terms/dfc_platform_terms/) | This is a standard terms of use for the Facebook API |
| [API Information](https://pypi.org/project/facebook-scraper/) | This is a document which explains all of the Facebook APIs that can be used, in this project we use Facebooks API|
| [Developer Portal](https://developers.facebook.com/) | Where you can access the developer portal. |

### Important Libraries:
| Library | Description |
| ------- | ----------- |
| [facebook_scraper](https://pypi.org/project/facebook-scraper/) | Using the Facebook Scraper Library to extract information but requires you to give the link of the information from https://m.facebook.com/*[Insert name here]*/?locale=en_US so you cannot provide usernames but instead the name of the link.|
| [Pandas](https://pypi.org/project/pandas/) | Our primary dataframe which will take the extracted information and be used to pass the information to display to the Rust environment on the front end while being able to create a data file (.csv) if requested from the front end |