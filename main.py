from tkinter import *
from tkinter import messagebox
import string
import random
import pyperclip
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
    if not username_entry.get() or not password_entry.get() or not website_entry.get():
        messagebox.showinfo(title="some required credential are empty", message=f"Please fill all required credential")

    else:

        is_ok = messagebox.showinfo(title=f"{website_entry.get()}", message=f"{website_entry.get()} \n {username_entry.get()} \n"
                                                                            f" {password_entry.get()}")
        if is_ok and username_entry.get() and password_entry.get() and website_entry.get():
            with open("data.txt", mode="a") as user_data:
                user_data.write(f"{website_entry.get()} | {username_entry.get()} | {password_entry.get()} \n")
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
website_entry = Entry(width=75, font=("Helvetica", 15) )
website_entry.grid(pady=10, row = 1, column=1, columnspan=2)

username_entry = Entry(width = 75, font=("Helvetica", 15))
username_entry.grid(pady=10,  row = 2, column=1, columnspan=2)

password_entry = Entry(width=55, font=("Helvetica", 15))
password_entry.grid(pady=10, row = 3, column=1)

#logo
canvas = Canvas(height=200, width=200)
logo = PhotoImage(file = "logo.png")
canvas.create_image(100, 100, image = logo)
canvas.grid(pady=10, row=0, column=1)

#buttons
generate_password_button = Button(text="Generate Password", font=("Helvetica", 15), command=generate_password)
generate_password_button.grid(pady=10, row=3, column=2)

add_button = Button(text="Add", font=("Helvetica", 15), width=95, command = save)
add_button.grid(pady = 10, row = 4, column = 0, columnspan=3)

window.mainloop()