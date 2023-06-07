# ------------import libraries----------- #
import pandas as pd
from tkinter import *
import random
#-------------Data-----------#
data = pd.read_csv('data/french_words.csv')
# data = data.to_dict() ->Convert a DataFrame to a nested Dict
data = data.to_dict(orient="records")#Oriented data to different format easier to work with->[{col1:val1},{col2:val2},...]
current_card = {}
def check_button():
    global current_card
    current_card = random.choice(data)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill='black')
    canvas.itemconfig(card_background_img,image=card_front_img)
    with open("learned.csv",mode='w') as learned_words:
        pass
def cross_button():
    english_word = current_card["English"]
    canvas.itemconfig(card_title, text="English",fill= "white")
    canvas.itemconfig(card_word, text=english_word,fill="white")
    canvas.itemconfig(card_background_img,image=card_back_img)
#-------------Creating GUI -------------#
BACKGROUND_COLOR = "#B1DDC6"
window = Tk()
window.title("Flashy")
window.config(pady=50,padx=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_back_img = PhotoImage(file='images/card_back.png')#No need to display the image rn cuz this img will be changed after the card flipped
card_front_img = PhotoImage(file='images/card_front.png')#get hold of the image
card_background_img = canvas.create_image(400,263,image=card_front_img)#Display the image
canvas.grid(column=0,row=0,columnspan=2)#Adjust the image to the center
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)#Setting the bg color the same as window to get rid of white border

card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,'italic'))#Creating some texts
card_word = canvas.create_text(400,263,text="Title",font=("Ariel",60,'bold'))

cross_img = PhotoImage(file='images/wrong.png')
check_img = PhotoImage(file='images/right.png')

#----------Button---------------#
idk_button = Button(image=cross_img,command=cross_button)
idk_button.grid(row=1,column=0)
ik_button = Button(image=check_img,command=check_button)
ik_button.grid(row=1,column=1)


























window.mainloop()
