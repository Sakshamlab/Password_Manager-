from tkinter import *
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():


    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)



    password_letter =[random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbol =[random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_number =[random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letter + password_symbol + password_number
    random.shuffle(password_list)

    user_password = "".join(password_list)

    password.insert(0,f"{user_password}")




# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_data():
    website_entry_txt = website.get().title()
    password_entry_txt = password.get()
    email_entry_txt = email.get()
    new_data = {
        website_entry_txt: {
            "Email:": email_entry_txt,
            "Password": password_entry_txt

        }
    }

    if len(website_entry_txt) == 0 or len(password_entry_txt) == 0:
        messagebox.showerror(title="ERROR",message="input in all field is required")

    else:
        try:
            with open("data.json","r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4 )
        else:
            data.update(new_data)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)


    # ---------------------------- UI SETUP ------------------------------- #

screen = Tk()
screen.title("Password Manager")
screen.config(padx=40,pady=40)







canvas = Canvas(height=200,width=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)


website_label = Label(text="Website:")
website_label.grid(row=1, column=0)


email_label = Label(text= 'Email/UserName:')
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)


website = Entry(width=35)
website.grid(row=1, column=1,columnspan=2)
website.focus()

email = Entry(width=35)
email.grid(row=2, column=1,columnspan=2)
email.insert(0, "heysakshamm@gmail.com")

password = Entry(width=25)
password.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password",command= generate_password)
generate_password_button.grid(row=3, column= 2)

add_button = Button(text="Add",width=36, command=save_data)

add_button.grid(row=4, column=1,columnspan=2)

screen.mainloop()