from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def click_me_clicked():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_clicked():

    email = email_username_entry.get()
    website = website_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please dont leave any fields empty!")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

#----------------------------- SEARCH PASSWORDS ------------------------ #
def search_clicked():
    website = website_entry.get()
    exists = False

    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error!", f"No data file found!")
    else:
        if website in data:
            searched_password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(f"{website}",
                                f"Email: {email}\n"
                                f"Password: {searched_password}\n")
        else:
            messagebox.showerror("Error!", f"No data for {website}!")


# ---------------------------- GUI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window,width=200, height=200)
password_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=password_image)
canvas.grid(row = 0, column = 1)

#labels
website_label = Label(text="Website:", font=(FONT_NAME, 10, "bold"), anchor = "e")
website_label.grid(row = 1, column = 0, sticky = "e")

website_label = Label(text="Email/Username:", font=(FONT_NAME, 10, "bold"), anchor = "e")
website_label.grid(row = 2, column = 0, sticky = "e")

website_label = Label(text="Password:", font=(FONT_NAME, 10, "bold"), anchor = "e")
website_label.grid(row = 3, column = 0, sticky = "e")

#entries
website_entry = Entry(width = 26)
website_entry.grid(row = 1, column = 1)
website_entry.focus()

email_username_entry = Entry(width = 35)
email_username_entry.grid(row = 2, column = 1, columnspan = 2)
email_username_entry.insert(0, "ica_smekerica")

password_entry = Entry(width = 26)
password_entry.grid(row = 3, column = 1)


#buttons
button_generate = Button(text="Generate", width = 7,command = click_me_clicked)
button_generate.grid(row = 3, column = 2)

button_add = Button(text="Add", width = 30,command = add_clicked)
button_add.grid(row = 4, column = 1, columnspan = 2)

button_search = Button(text="Search", width = 7,command = search_clicked)
button_search.grid(row = 1, column = 2)














window.mainloop()