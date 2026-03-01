from tkinter import *
from tkinter import messagebox
import string
import random

import pyperclip
import json
#---------------------------- search password and username ------------------------------- #
def search():
    try:
        with open("data.json", mode="r") as user_data:
            content = json.load(user_data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data found, It seems you haven't saved anything yet")
    else:
        if website_entry.get():
            try:
                messagebox.showinfo(title="saved credentials are : ",
                                    message=f"Username : {content[website_entry.get()]["username"]} \n"
                                            f"Password : {content[website_entry.get()]["password"]}")
            except KeyError as error_website:
                messagebox.showinfo(title="Not found", message=f"Sorry, Website {error_website} not found")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():

    letters = list(string.ascii_lowercase)
    random.shuffle(letters)

    numbers = [str(n) for n in range(0,10)]
    random.shuffle(numbers)

    symbols = ["!", "@", "#","%"]

    number_of_letters = random.randint(5,8)
    number_of_numbers = random.randint(3,8)
    number_of_symbols = random.randint(0,3)

    random_letters = [letters[n] for n in range(0, number_of_letters + 1)]
    random_numbers = [numbers[n] for n in range(0, number_of_numbers + 1)]
    random_symbols = [symbols[n] for n in range(0, number_of_symbols + 1)]

    password_list = random_numbers + random_symbols + random_letters
    random.shuffle(password_list)

    password = ""
    for n in password_list:
        password += n
    print(password)

    password_entry.insert(0,f"{password}")
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    new_data = {
        website_entry.get() : {
            "username" : username_entry.get(),
            "password" : password_entry.get(),
        }
    }

    if not username_entry.get() or not password_entry.get() or not website_entry.get():
        messagebox.showinfo(title="some required credential are empty", message=f"Please fill all required credential")

    else:
        if username_entry.get() and password_entry.get() and website_entry.get():
            try:
                with open("data.json", mode="r") as user_data:
                    # read
                    content = json.load(user_data)
            except FileNotFoundError:
                with open("data.json", mode="w") as user_data:
                    json.dump(new_data, user_data, indent=4)
            else:
                #update
                content.update(new_data)
                with open("data.json", mode="w") as user_data:
                    #write
                    json.dump(content, user_data, indent=4)
            finally:
                website_entry.delete(0, END)
                username_entry.delete(0, END)
                password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=50, pady=50)
window.focus()
window.title("Password Generator")

#labels
website_label = Label(text="Website : " , font=("Helvetica", 15))
website_label.grid(pady=10, row=1, column=0)

username_label = Label(text="Username/Email : ", font=("Helvetica", 15))
username_label.grid(pady=10, row=2, column=0)

password_label = Label(text="Password : ",font=("Helvetica", 15))
password_label.grid(pady=10, row=3, column=0)

#user inputs
website_entry = Entry(width=50, font=("Helvetica", 15) )
website_entry.grid(pady=10, row = 1, column=1,)

username_entry = Entry(width = 68, font=("Helvetica", 15))
username_entry.grid(pady=10,  row = 2, column=1, columnspan=2)

password_entry = Entry(width=50, font=("Helvetica", 15))
password_entry.grid(pady=10, row = 3, column=1)

#logo
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(pady=10, row=0, column=1)

#buttons
generate_password_button = Button(text="Generate Password", font=("Helvetica", 15), command=generate_password)
generate_password_button.grid(pady=10, row=3, column=2)

add_button = Button(text="Add", font=("Helvetica", 15), width=68, command = save)
add_button.grid(pady = 10, row = 4, column = 1, columnspan=2)

search_button = Button(text="Search", font=("Helvetica", 15),width=16, command=search)
search_button.grid(pady = 10, row = 1, column = 2)

window.mainloop()