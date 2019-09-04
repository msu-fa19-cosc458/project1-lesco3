{"filter":false,"title":"appli.py","tooltip":"/appli.py","undoManager":{"mark":6,"position":6,"stack":[[{"start":{"row":0,"column":0},"end":{"row":66,"column":0},"action":"insert","lines":["Skip to content","Search or jump to…","","Pull requests","Issues","Marketplace","Explore"," ","@leoncscott543 ","Code Issues 0 Pull requests 0 Projects 0 Wiki Security Pulse Community","TomMisch-Webapp/appli.py"," Ubuntu Huge commit :) ==>> 1. couldnt get randomized songs to work on refres…","f724b3c 3 hours ago","39 lines (31 sloc)  1.3 KB","  ","# this is the main executable file ","# I built a route that sends song data ","# (fetched from genius) to the page.html templates file","# to use the data dynamically on the page","","from flask import Flask, render_template","import os","import requests","import json","import random","","# app execution name is appli","appli = Flask(__name__)","","# defining authorization header in myheader :)","myheader = {\"Authorization\": \"Bearer eTnvJMtGEvFKJVrj72lNjVZzXgtyE1xD6Q-Unv2A0Amjhgfx-DEo-1oEUnipH87b\"}","","song_id=[3300945, 484106, 484106] # multiple songs to randomly generate","","# retreiving song api from genius and converting to json","song = requests.get('https://api.genius.com/songs/' + str(random.choice(song_id)) + '?text_format=plain', headers=myheader)","song_json = song.json()","","# just print(song_string) to inspect json data tree","song_string = json.dumps(song_json, indent=2) ","","# main route, returns .json api data to page.html ","# uses render_template to access page.html","@appli.route(\"/\")","def songdata():","    return render_template('page.html', ","    song_art= song_json['response']['song']['song_art_image_url'],","    song_fulltitle = song_json['response']['song']['full_title'],","    song_lyrics = song_json['response']['song']['embed_content']",")","","appli.run(host=os.getenv('IP', '0.0.0.0'), ","          port=int(os.getenv('PORT', 8080)),","          debug=True)","© 2019 GitHub, Inc.","Terms","Privacy","Security","Status","Help","Contact GitHub","Pricing","API","Training","Blog","About",""],"id":2}],[{"start":{"row":54,"column":0},"end":{"row":65,"column":5},"action":"remove","lines":["© 2019 GitHub, Inc.","Terms","Privacy","Security","Status","Help","Contact GitHub","Pricing","API","Training","Blog","About"],"id":3}],[{"start":{"row":0,"column":0},"end":{"row":6,"column":7},"action":"remove","lines":["Skip to content","Search or jump to…","","Pull requests","Issues","Marketplace","Explore"],"id":4}],[{"start":{"row":0,"column":0},"end":{"row":7,"column":26},"action":"remove","lines":[""," ","@leoncscott543 ","Code Issues 0 Pull requests 0 Projects 0 Wiki Security Pulse Community","TomMisch-Webapp/appli.py"," Ubuntu Huge commit :) ==>> 1. couldnt get randomized songs to work on refres…","f724b3c 3 hours ago","39 lines (31 sloc)  1.3 KB"],"id":5}],[{"start":{"row":1,"column":2},"end":{"row":2,"column":0},"action":"remove","lines":["",""],"id":6},{"start":{"row":1,"column":1},"end":{"row":1,"column":2},"action":"remove","lines":[" "]},{"start":{"row":1,"column":0},"end":{"row":1,"column":1},"action":"remove","lines":[" "]},{"start":{"row":0,"column":0},"end":{"row":1,"column":0},"action":"remove","lines":["",""]},{"start":{"row":0,"column":19},"end":{"row":0,"column":29},"action":"remove","lines":["executable"]},{"start":{"row":0,"column":19},"end":{"row":0,"column":20},"action":"insert","lines":["p"]},{"start":{"row":0,"column":20},"end":{"row":0,"column":21},"action":"insert","lines":["y"]},{"start":{"row":0,"column":21},"end":{"row":0,"column":22},"action":"insert","lines":["t"]},{"start":{"row":0,"column":22},"end":{"row":0,"column":23},"action":"insert","lines":["h"]},{"start":{"row":0,"column":23},"end":{"row":0,"column":24},"action":"insert","lines":["o"]},{"start":{"row":0,"column":24},"end":{"row":0,"column":25},"action":"insert","lines":["n"]}],[{"start":{"row":0,"column":14},"end":{"row":0,"column":18},"action":"remove","lines":["main"],"id":7},{"start":{"row":0,"column":14},"end":{"row":0,"column":15},"action":"insert","lines":["r"]}],[{"start":{"row":0,"column":15},"end":{"row":0,"column":16},"action":"insert","lines":["o"],"id":8},{"start":{"row":0,"column":16},"end":{"row":0,"column":17},"action":"insert","lines":["o"]},{"start":{"row":0,"column":17},"end":{"row":0,"column":18},"action":"insert","lines":["t"]}]]},"ace":{"folds":[],"scrolltop":0,"scrollleft":0,"selection":{"start":{"row":21,"column":23},"end":{"row":21,"column":23},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":0},"timestamp":1567596740554,"hash":"5703ed286ded791151560175bc29be829186a789"}