# from curses import window
# from curses import window
import tkinter as tk
from random import randint 
import time
import requests
import json

window=tk.Tk()
window.title("chatbot GUI") 
window.configure(bg="#ECECEC")

text_box=tk.Text(window, height=28, width=50, bg="#FFFFFF", fg="#333333", font=("Arial", 12))
text_box.pack(pady=10)


def handle_user_input():
   chatbot()

entry=tk.Entry(window, width=50,font=("Arial", 12))
entry.pack()

button = tk.Button(window, text="send", command=handle_user_input, bg="#428BCA", fg="#FFFFFF", font=("Arial", 12, "bold")) 
button.pack(pady=10)

def chatbot():
  user_input=entry.get().lower()


  db={

'greetings': {
   'triggers': ['hi', 'hey','hello', 'heyya','heyya','kase ho','sup','wassup','yo','ello'],
   'responses': ['Hello there whats your name']
},
'bye':{

'triggers': ['bye', 'cya', 'gtg', 'manish', 'i gtg','gtg bye'],

'responses': [ 'hello manish '],
},

'question':{
  
'triggers': [ 'how are you','kya hal h ' ,'kase ho', 'or btao'],
'responses': [' i am fine what abourt you ' ,'thik hu ji'],
},

'thankyou':{
'triggers': [ 'tysm', 'thanks', 'thank you'],
'responses': ['so problem!', 'You\'re welcome!', 'welcome!'],

},

'good':{
'triggers': [ 'i am study in b tech' 'good','great', 'nice','hoice', 'cool'],
'responses':['good  ','Aursome1', 'Great!'],

},

'ok':{
   'triggers': ['ok', 'okay','aight','ight','k','kk','alright'],
'responses':[ 'okok','Are you sure?','ok','okay.'],
},
'yes':{
   'triggers':['yes','yeah','ye','yea','yep','ya'],
   'responses':['fine','ok.'],
},
'no':{
'triggers':['no','nope','nah','na'],
'responses':['why not ?','okay.'],

},
'bored':{
   'triggers':['i\'m bored','im bored','i am bored'],
   'responses':['say goodbye to your boredom '],
},
'nonyou':{
'triggers':['no u','no you'],
'responses':['no u','no you'],
},
'stutterwords':{
'triggers':["uh","uhm","uh-","uhm-","uhh"],
'responses':["hm","?","What?"],
},
'lol':{
'triggers':["lol","lmao","haha","hahaha","hehe","xd"],
'responses':["Haha!","funny","right?","xD"],
},
  }
  if user_input in db['greetings']['triggers']:
    send_bot_message(random(db['greetings']['responses'])) 
 
  elif user_input in db['bye']['triggers']:
    send_bot_message(random(db['bye']['responses']))

  elif user_input=='tell  me a joke':
    data = requests.get("https://official-joke-api.appspot.com/random_joke")
    joke= json.loads(data.text)
    send_bot_message(f'{joke["setup"]}\n      { joke["punchline"]}')
    
  else:
   send_bot_message("I'm not sure I understand.")
   entry.delete(0,tk.END)


def send_bot_message(message): 
  text_box.insert(tk.END,f'chatbot: {message}\n')
  text_box.see(tk.END) 
  time.sleep(0.2)

def random(array):
   array_length= len(array) 
   rand=randint(0, array_length-1) 
   return array[rand]

send_bot_message("Hi! i'm joking chatbot.What's your name?")
send_bot_message("i can have convversation with you . just type your massaags below and hit send!")
window.mainloop() 