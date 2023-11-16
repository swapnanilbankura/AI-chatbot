import webbrowser
import time
import random
from tkinter import *

# GUI
root = Tk()
root.title("Chatbot")

BG_GRAY = "#ABB2B9"
BG_COLOR = "#17202A"
TEXT_COLOR = "#EAECEE"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

def send():
    send = "You -> " + e.get()
    txt.insert(END, "\n" + send)
 
    user = e.get().lower()
 
    if (user == "hello"):
        txt.insert(END, "\n" + "Bot -> Hi there, how can I help?")
 
    elif (user == "hi" or user == "hii" or user == "hiiii"):
        txt.insert(END, "\n" + "Bot -> Hi there, what can I do for you?")
    elif (user == "how is the weather today" or user == "what is the temperature" or user == "how is it outside" or user== "what is the temp"):url = "https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671";webbrowser.get('safari').open(url)
        
 
    elif (user == "how are you"):
        txt.insert(END, "\n" + "Bot -> fine! and you")
 
    elif (user == "fine" or user == "i am good" or user == "i am doing good"):
        txt.insert(END, "\n" + "Bot -> Great! how can I help you.")
 
    elif (user == "thanks" or user == "thank you" or user == "now its my time"):
        txt.insert(END, "\n" + "Bot -> My pleasure !")
 
    elif (user == "what do you sell" or user == "what kinds of items are there" or user == "have you something"):
        txt.insert(END, "\n" + "Bot -> We have coffee and tea")
    elif (user == "tell me a joke" or user == "tell me something funny" or user == "crack a funny line" or user == "tell me another joke" or user== "tell me another"):
        L=["What do kids play when their mom is using the phone? Bored games.","What do you call an ant who fights crime? A vigilANTe!","Why are snails slow? Because they’re carrying a house on their back.","What’s the smartest insect? A spelling bee!","How does the ocean say hi? It waves!","What do birds give out on Halloween? Tweets."]
        txt.insert(END, "\n" + "Bot ->" + random.choice(L)) 
    elif (user=="open google"):url = "https://www.google.com";webbrowser.get('safari').open(url)
    elif (user=="open youtube"):url = "https://www.youtube.com";webbrowser.get('safari').open(url)
    elif (user=="open whatsapp"):url = "https://web.whatsapp.com";webbrowser.get('safari').open(url)
    elif (user=="open netflix"):url = "https://www.netflix.com";webbrowser.get('safari').open(url)
    elif (user=="open twitch"):url = "https://www.twitch.com";webbrowser.get('safari').open(url)
    elif (user=="open chess"):url = "https://www.chess.com";webbrowser.get('safari').open(url)
    elif (user=="open apple"):url = "https://www.apple.com";webbrowser.get('safari').open(url)
    elif (user=="open amazon"):url = "https://www.google.com";webbrowser.get('safari').open(url)
    elif (user == "goodbye" or user == "see you later" or user == "see yaa"):
        txt.insert(END, "\n" + "Bot -> Have a nice day!")
    else:
        txt.insert(END, "\n" + "Bot -> Sorry! I didn't understand that")
        e.delete(0, END)


    
     

    




lable1 = Label(root, bg=BG_COLOR, fg=TEXT_COLOR, text="Welcome", font=FONT_BOLD, pady=10, width=20, height=1).grid(
	row=0)

txt = Text(root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
txt.grid(row=1, column=0, columnspan=2)

scrollbar = Scrollbar(txt)
scrollbar.place(relheight=1, relx=0.974)

e = Entry(root, bg="#2C3E50", fg=TEXT_COLOR, font=FONT, width=55)
e.grid(row=2, column=0)

send = Button(root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
			command=send).grid(row=2, column=1)




root.mainloop()

