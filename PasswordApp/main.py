import tkinter
from tkinter import messagebox
import random
import pyperclip
import json

class PasswordApplication:
    def __init__(self) -> None:
        #SCREEN
        self.window = tkinter.Tk()
        self.window.minsize(height=400, width=600)
        self.window.title("Password Manager")
        self.window.config(padx=20, pady=20)
        #LOGO
        self.canvas = tkinter.Canvas(width=200, height=200)
        self.logo_image = tkinter.PhotoImage(file="PasswordApp/logo.png")
        self.canvas.create_image(100, 100, image=self.logo_image)
        self.canvas.pack()
        #INPUTS
        self.website_input = tkinter.Entry(width=21)
        self.website_input.place(x=175, y=225)
        self.email_input = tkinter.Entry(width=43)
        self.email_input.place(x=175, y=250)
        self.password_input = tkinter.Entry(width=21)
        self.password_input.place(x=175, y=275)
        #BUTTONS
        self.generate_button = tkinter.Button(text="Generate Password", width=17, command=self.generate_password)
        self.generate_button.place(x=309, y=273)
        self.add_button = tkinter.Button(text="Add", width=36, command=self.save_password)
        self.add_button.place(x=175, y=300)
        self.search_button = tkinter.Button(text="Search", width=17, command=self.show_account)
        self.search_button.place(x=309, y=222)
        #TOPICS OF INPUTS
        self.website_label = tkinter.Label(text="Website:")
        self.website_label.place(x=100, y=223)
        self.email_label = tkinter.Label(text="Email/Username:")
        self.email_label.place(x=70, y=248)
        self.password_label = tkinter.Label(text="Password:")
        self.password_label.place(x=100, y=273)
        self.window.mainloop()
    
    
    def generate_password(self):
        self.password_input.delete(0, tkinter.END)
        self.letters = letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.symbols = ['!', '*', '%', '$', '#', '/', '?', '-', '_', '+', '&']
        self.nr_letters = random.randint(8, 10)
        self.nr_numbers = random.randint(2, 4)
        self.nr_symbols = random.randint(2, 4)
        self.password_letters = [random.choice(self.letters) for _ in range(self.nr_letters)]
        self.password_symbols = [random.choice(self.symbols) for _ in range(self.nr_symbols)]
        self.password_numbers = [random.choice(self.numbers) for _ in range(self.nr_numbers)]
        self.password_list = self.password_letters + self.password_symbols + self.password_numbers
        random.shuffle(self.password_list)
        self.password = "".join(self.password_list)
        self.password_input.insert(0, self.password)
        pyperclip.copy(self.password)
    
    
    def save_password(self):
        self.website = self.website_input.get().capitalize()
        self.email = self.email_input.get()
        self.password = self.password_input.get()
        self.new_data = {
            self.website: {
                "email": self.email,
                "password": self.password
            }
        }
        if len(self.website) == 0 or len(self.password) == 0 or len(self.email) == 0:
            messagebox.showinfo(title="OOPS!", message="Please make sure you haven't left any fields empty.")
        else:
            try:
                with open("PasswordApp/data.json", "r") as self.data:
                    self.data_load = json.load(self.data)
            except FileNotFoundError:
                with open("PasswordApp/data.json", "w") as self.data:
                    json.dump(self.new_data, self.data, indent=4)
            else:
                self.data_load.update(self.new_data)
                with open("PasswordApp/data.json", "w") as self.data:
                    json.dump(self.data_load, self.data, indent=4)
            finally:
                self.website_input.delete(0, tkinter.END)
                self.password_input.delete(0, tkinter.END)
                self.email_input.delete(0, tkinter.END)
    
    
    def show_account(self):
        self.get_website = self.website_input.get().capitalize()
        with open("PasswordApp/data.json", "r") as self.show_data:
            self.data_packs = json.load(self.show_data)
            if self.get_website in self.data_packs:
                self.account_data = self.data_packs[self.get_website]
                self.email_data = self.account_data["email"]
                self.password_data = self.account_data["password"]
                messagebox.showinfo(title=f"Account Info of {self.get_website}", message=f"Username/Email: {self.email_data}\nPassword: {self.password_data}")
            else:
                messagebox.showinfo(title="Info", message=f"We can't find your {self.get_website} account.")



PasswordApplication()


