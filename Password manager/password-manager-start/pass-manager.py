from tkinter import messagebox
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    from random import randint, choice, shuffle
    import pyperclip
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_list_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_list_symbol + password_list_letter + password_list_number
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    website_info = web_entry.get()
    user_name = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website_info: {
            'user_name':user_name,
            'password':password
        }
    }
    if len(website_info) == 0 or len(user_name) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty")

    is_ok = messagebox.askokcancel(title="OK?",message="Saving??????")
    if is_ok:
        try:
            with open('data.json',mode='r') as data_file:
                #Reading old data
                data = json.load(data_file)
        except FileNotFoundError:#Catch the error that the file is does not exist from the beginning
            with open('data.json',mode='w') as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            # Update old data
            data.update(new_data)
            with open('data.json',mode='w') as data_file:#If data.json is not exist python will auto create it from scratch
               json.dump(data,data_file,indent=4)#using dump() method from json library, dump mean write
        finally:
            web_entry.delete(0,END)
            user_name_entry.delete(0,END)
            password_entry.delete(0,END)

#----------------------------Search pass--------------------------------#
def find_pass():
    website = web_entry.get()#Get whatever the user type in(website name)
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No file found")
    else:
        if website in data:
            email = data[website]['user_name']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details about {website} found")
# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *
window = Tk()
window.title("Password Manager")

window.config(padx=50,pady=50)
canvas = Canvas(height=200,width=190)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,94.5,image=logo_img)
canvas.grid(column=1,row=0)
#Label
website_label = Label(text="Website")
website_label.grid(column=0,row=1)
user_name_label = Label(text="Email/Username")
user_name_label.grid(column=0,row=2)
pass_label = Label(text="Password")
pass_label.grid(column=0,row=3)

#Entry
web_entry = Entry(width=21)
web_entry.grid(column=1,row=1)
user_name_entry = Entry(width=35)
user_name_entry.grid(column=1,row=2,columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)




#Button
search_button = Button(text="Search",width=14,command=find_pass)
search_button.grid(column=2,row=1)
gen_pass_button = Button(text="Generate Password",width=14,command=gen_pass)
gen_pass_button.grid(column=2,row=3)
add_button = Button(text="Add",width=36,command=save_pass)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()