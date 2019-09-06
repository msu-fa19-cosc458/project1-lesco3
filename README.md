         ___        ______     ____ _                 _  ___  
        / \ \      / / ___|   / ___| | ___  _   _  __| |/ _ \ 
       / _ \ \ /\ / /\___ \  | |   | |/ _ \| | | |/ _` | (_) |
      / ___ \ V  V /  ___) | | |___| | (_) | |_| | (_| |\__, |
     /_/   \_\_/\_/  |____/   \____|_|\___/ \__,_|\__,_|  /_/ 
 ----------------------------------------------------------------- 
Theme:  Chill Vibes
 ---------------------------
 So i essentially was trying to create a fanpage of Tom Misch who's my fav artist as of this month. He's sort-of floats somewhere between new-school r&b, neo-soul, and strong jazz underdones.... he's not necessarily a world class vocalist, but he knows melodies and has a fantastic ear and it comes across in his live jams espeically. But I wanted to capture his vibe and his creative enviornment through the page. So its sort-of visual art more than an interactive app to me lol and i didnt realize thats what I was doing until about midway through this project. But its was fun nonetheless. 
 
 The quotes i pulled are a reflection i think of Tom's demeanor in life and through his art. They're all (with the exception of the random one about donald trump lol) centered around living a life of relentless simplicity and chillaxness~ I failed at pulling random twitter quotes so i just pulled random status ids from the api instead :( 

<b>Problems: </b>
1. craziest issue with getting mystyle.css to link to index.html... i couldnt link reference my stylesheet to my html file in the static folder. It wouldnt even work if my stylesheet was on the same level as my html.... i decided to abandon the compartmentalization and just put my style guide right into the html document to keep things moving. 

2. trouble parsing twitter data from twitter api queries, but realized that twitter json is key value which made life a lot easier

3. couldnt figure out how to display new data on page refreshes... then realized that all i had to do was get() my json within my main function rather than out

4. getting elements to overlay video background.... im not css master, so i sort of jerry-rigged/retro-fit everythin together which isnt much of a problem given that this is a static webpage

5. making the videobackground static even when scrolling: this just took a lot of research, but essentially filly the margins 100% and making the video static did the trick

<b>6. I failed in setting up config keys. This was really disappointing to me.... i should've started doing this earlier in the dev process</b>

7. My biggest failure was generating a new tweet each time the screen is refreshed. I'm not sure if my search terms were to specific but for the most part my implementations of get.search twitter api didnt return a new tweet every refresh...I tried to dig into this issue quite a bit but it became too time consuming so I just sort-of archived the code and went with another api just for retreiving exact tweets

8. i think i accidentally retreived a tweet about the president lol not sure how or why lol

9. even though i am retreiving the artist genius url page data from the songs api, i accidentally put in the song page url for the link on the artist photo. pretty annoying :(

10. My actual biggest issue was deploying to heroku. I spent the most time actually attempting to do this than i think i spent coding. In short, i was mostly getting runtime errors after succesful deploys to the server. Error H10. My best solution was to download the heroku widget into cloud9 terminal and clear the cache and download a few other packages fresh and reset the heroku remote and most importantly to change my running port code to a conditonal that allows heroku to choose its own port to run-on. This solution mostly comes from this blog post http://kennmyers.github.io/tutorial/2016/03/11/getting-flask-on-heroku.html

<b>What I'd do differently</b>
So in the spririt of transparency, I hadn't really started the project until last weekend because I thought it was going to be a two day affair at the most lol and i was wrong not because the project was that hard, but because I made it harder than it needed to because Im obsessed with doing that for some reason. So if i were to go back and push updates, which i probably will because this is going into my portfolio, here's what they'd be: 

1. Hide my gosh-darn config keys
2. Branch my code (specifically my apis) into different files
3. And at the same time writing seperate functions for each API and for some of the other processes i wrote in my only function
4. Documented better.... I'm usually a lot better at commenting throughout my code but I was a mess with this project tryging to debug and troubleshoot a million issues and creating new projects ect... that a lot of the comments in other portions of my code got loss in the sauce... But i think i did a fair amount of documentation in my git pushes
5. Built a toggle for switching between songs without refreshing the page
6. Better design... my elements are pretty on their own but the alignments are sort of off
 - the artist photo needs to come further off of the edge of the page
 - the quotes are too long and should jump to next line at certain threshold
 - elements render in a choppy way
 - the lone animation i have on my song title fades when you click on the album as well lolol hilarious
 - there definitly could be some more fun animations
 - i was actually trying to add the lyrics embed from the songs api but i didnt like how it would shift the page down and add a scroll
7. I was on the verge of actually building a library of all of Tom's by parsing the genius search api but scratched it for the due date
8. Make an object for the media (songs and videos) loads rather than using all of those conditionals
9  Assuming i make a library, parse api in efficent way


Thats it for now :)
