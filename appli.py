# this is the root python file 
# I built a route that sends song data 
# (fetched from genius) to the page.html templates file
# to use the data dynamically on the page

from flask import Flask, render_template
import os
import requests
import json
import random

# app execution name is appli
appli = Flask(__name__)

# defining authorization header in myheader :)
myheader = {"Authorization": "Bearer eTnvJMtGEvFKJVrj72lNjVZzXgtyE1xD6Q-Unv2A0Amjhgfx-DEo-1oEUnipH87b"}

song_id=[3300945, 484106, 1234412] # multiple songs to randomly generate


# main route, returns .json api data to page.html 
# uses render_template to access page.html
@appli.route("/")
def songdata():
    
    choice_num=str(random.choice(song_id))
    
    # retreiving song api from genius and converting to json
    song = requests.get('https://api.genius.com/songs/' + choice_num + '?text_format=plain', headers=myheader)
    song_json = song.json()
    
    # just print(song_string) to inspect json data tree
    song_string = json.dumps(song_json, indent=2) 
    
    return render_template('testing_media.html',
    choice_num=choice_num,
    song_art= song_json['response']['song']['song_art_image_url'],
    song_title = song_json['response']['song']['full_title'],
    song_lyrics = song_json['response']['song']['embed_content'],
    artist_photo = song_json['response']['song']['primary_artist']['header_image_url'],
    artist_link = song_json['response']['song']['primary_artist']['url']
)

appli.run(host=os.getenv('IP', '0.0.0.0'), 
          port=int(os.getenv('PORT', 8080)),
          debug=True)

