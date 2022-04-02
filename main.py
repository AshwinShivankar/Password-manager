
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(nr_letters)]
    password_sym = [random.choice(symbols) for _ in range(nr_symbols)]
    password_num = [random.choice(symbols) for _ in range(nr_numbers)]

    password_list = password_letter + password_sym + password_num

    random.shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char
    input_3.insert(0, password)
    pyperclip.copy(password)
    # print(f"Your password is: {password}")


# ---------------------------- find PASSWORD ------------------------------- #

def find():
    website = input.get()
    try:
        with open("data.json", "r") as data:
            data_load= json.load(data)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found")
    else:
        if website in data_load:
           email = data_load[website]["email"]
           password = data_load[website]["password"]
           messagebox.showinfo(title=website,message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message=f"no details for {website} exist")
# ---------------------------- UI SETUP ------------------------------- #


def save():
    website = input.get()
    email = input_2.get()
    password = input_3.get()

    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Opps", message="Please don't leave any filed empty")

    else:
        try:
            with open("data.json", "r") as data:
                data_load = json.load(data)

        except FileNotFoundError:
            with open("data.json", "w") as data:
                json.dump(new_data, data, indent=4)

        else:
            data_load.update(new_data)

            with open("data.json", "w") as data:
                json.dump(data_load, data, indent=4)
        finally:
            input.delete(0, END)
            input_3.delete(0, END)


window = Tk()
window.title("Pasword Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock)
canvas.grid(column=1, row=0)

label = Label(text="Website:")
label.grid(column=0, row=1)

label_2 = Label(text="Email/Username:")
label_2.grid(column=0, row=2)

label_3 = Label(text="Password:")
label_3.grid(column=0, row=3)

input = Entry(width=51)
input.focus()
input.grid(column=1, row=1,columnspan=2)

input_2 = Entry(width=51)
input_2.grid(column=1, row=2,columnspan=2)
input_2.insert(0, "ashwin.msh21@gmail.com")

input_3 = Entry(width=51)
input_3.grid(column=1, row=3,columnspan=2)

button = Button(text="Generate Password", command=gen_pass)
button.grid(column=2, row=3)

button_2 = Button(text="Add", width=43, command=save)
button_2.grid(column=1, row=4, columnspan=2)

button_3 = Button(text="Search",width=13,command=find)
button_3.grid(column=2, row=1)

window.mainloop()
