import praw
from os import system
from gtts import gTTS

reddit = praw.Reddit(
    client_id="Db7VwYDvnQHutRrgtHoxIw",
    client_secret="lfSs5NQPyu-AH4oulUGxBBUoIzUKxA",
    password="*#01Cd01e1*#",
    user_agent="L05T-F15H-BOT",
    username="L05T-F15H",
)

language = 'en'
subreddit = reddit.subreddit("confession")

system("clear")
for submission in subreddit.hot(limit=10):
    print("Title: ", submission.title)
    print("Text: ", submission.selftext)
    print("Score: ", submission.score)
    print("---------------------------------\n")
    myobj = gTTS(text=submission.selftext, lang=language, slow=False)
  
    # Saving the converted audio in a mp3 file named
    # welcome 
    myobj.save(f"{submission.title}.mp3")