import requests,tweepy
from bs4 import BeautifulSoup

# You can choose to get quotes from a different category, just change the tag in URL
# For example, if you want to get Love quotes, the URL should be https://www.quotesdaddy.com/feed/tagged/love

url = "https://www.quotesdaddy.com/feed/tagged/Inspirational"
r = requests.get(url)

soup = BeautifulSoup(r.text,'html.parser')
q = soup.find_all("description")
quote = q[1].get_text()

# Following Keys can be obtained from apps.twitter.com

consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Due to Twitter's API limitations, only a limited set of IDs can be liked/favorited

def fav(id):
    api.create_favorite(id)
    print("Favoriting Tweet...")

# Following function does search for a given string, you can replace it with any other string

def tweet(q_string):
    s = api.search("#quote")
    try:
        api.update_status(q_string)
        print("Tweet Successful! Favoriting Tweets Now...")
        for i in range(len(s)):
            fav(s[i].id)
    except:
        print("Tweet Exists! Favoriting Tweets...")
        for i in range(len(s)):
            fav(s[i].id)

if len(quote) > 140:
    new_quote = quote[:140]
    tweet(new_quote)

elif len(quote) <= 133:
    new_quote = quote + " #quote"
    tweet(new_quote)

else:
    tweet(quote)