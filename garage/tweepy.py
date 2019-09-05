import requests_oauthlib, requests
from flask import Flask, render_template
import os
import requests
import json
import tweepy

twitter = Flask(__name__)

@twitter.route("/new")
def tweet():
    url = "https://api.twitter.com/1.1/statuses/user_timeline.json"
    
    consumer_key = '3ICZ0C7ojimzEIcikzi1TahJV'
    consumer_secret = 'Ps6IelFUnvmEUk9oqgkrQFfsaLaJG56HRWJCKfOs2n0Lh6OqfJ'
       
    access_token = '317341733-Mh9eGlPW0Mrr0DRVn0oUc9I3M6jh90PYCjy6lUUa'
    access_token_secret = 'KRTf4ZH4mFzMKQlpRXUhdcbvYblWu5BCAz84j3v4sKCIo'
    
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret, callback_url)
    
    twitt = requests.get(url, auth=auth)
    twitt_json = twitt.json()
    twitt_format = json.dumps(twitt.json(), indent=2) 
    # tweet = twitt_json['text']
    
    
    
    return render_template('/templates/garage/tweets.html', twitt_json(screen_name=tommisch, count=2))
    
    twitter.run(host=os.getenv('IP', '0.0.0.0'), port=int(os.getenv('PORT', 8080)), debug=True)