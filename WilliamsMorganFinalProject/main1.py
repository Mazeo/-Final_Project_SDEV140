import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *

#page2 = tk.Tk()
#page2.geometry("400x400")

def login():
    username = username_entry.get() #def a user entry for the username  
    password = password_entry.get() #def a user entry for the password

    if username == "user1" and password == "abc123": #if the username and password are correct login will show succesfull
        loginStatus.config(text="Login successful", fg="green")# loginStatus is used to show the effect of the current login entry
    else: #if login is not successful it will show that login failed and that the user should try again
        loginStatus.config(text="Login failed. Try again.", fg="red")

# Create the main Tkinter window
main = tk.Tk()
main.title("Login Form")
main.geometry("400x400")

#Labels used to enter for the user and pass
usernameLabel = tk.Label(main, text = "Username:")# Text used to show the username label
passwordLabel = tk.Label(main, text = "Password:")# text used to show the password label
username_entry = tk.Entry(main)
password_entry = tk.Entry(main, show="*")  # Show '*' for password entry
hintLabel = tk.Label(main, text = "Username is user1")# Gives the user a hint to the username
hintLabel2 = tk.Label(main, text = "Password is abc123") #gives the user a hint to the password




# A login button to login
loginButton = tk.Button(main, text="Login", command=login)

# A label to show the login status
loginStatus = tk.Label(main, text="", fg="black")

# Use the Grid geometry manager to arrange widgets
usernameLabel.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "E")#How the username is arranged on the app
username_entry.grid(row = 0, column = 1, padx = 10, pady = 5)

passwordLabel.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = "E")#how the password is arranged on the app
password_entry.grid(row = 1, column = 1, padx = 10, pady = 5)

hintLabel.grid(row = 4, column = 0)
hintLabel2.grid(row = 5, column = 0)

loginButton.grid(row = 2, column = 0, columnspan = 2, padx = 10, pady = 10)#How the login should be possition in the app
loginStatus.grid(row = 3, column = 0, columnspan = 2, padx = 10, pady = 5)

page2 = tk.Tk()
page2.geometry("400x400")

# Run the Tkinter main loop
main.mainloop()
