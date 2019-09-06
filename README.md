         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 
Problems: 
1. craziest issue with getting mystyle.css to link to index.html... i couldnt link reference my stylesheet to my html file in the static folder. It wouldnt even work if my stylesheet was on the same level as my html.... i decided to abandon the compartmentalization and just put my style guide right into the html document to keep things moving. 

2. trouble parsing twitter data from twitter api queries, but realized that twitter json is key value which made life a lot easier

3. couldnt figure out how to display new data on page refreshes... then realized that all i had to do was get() my json within my main function rather than out

4. getting elements to overlay video background.... im not css master, so i sort of jerry-rigged/retro-fit everythin together which isnt much of a problem given that this is a static webpage

5. making the videobackground static even when scrolling: this just took a lot of research, but essentially filly the margins 100% and making the video static did the trick

<b>6. I failed in setting up config keys. This was really disappointing to me.... i should've started doing this earlier in the dev process<b>

7. My biggest failure was generating a new tweet each time the screen is refreshed. I'm not sure if my search terms were to specific but for the most part my implementations of get.search twitter api didnt return a new tweet every refresh...I tried to dig into this issue quite a bit but it became too time consuming so I just sort-of archived the code and went with another api just for retreiving exact tweets

8. i think i accidentally retreived a tweet about the president lol not sure how or why lol

9. even though i am retreiving the artist genius url page data from the songs api, i accidentally put in the song page url for the link on the artist photo. pretty annoying :(

10. My actual biggest issue was deploying to heroku. I spent the most time actually attempting to do this than i think i spent coding. In short, i was mostly getting runtime errors after succesful deploys to the server. Error H10. My best solution was to download the heroku widget into cloud9 terminal and clear the cache and download a few other packages fresh and reset the heroku remote and most importantly to change my running port code to a conditonal that allows heroku to choose its own port to run-on. This solution mostly comes from this blog post http://kennmyers.github.io/tutorial/2016/03/11/getting-flask-on-heroku.html
