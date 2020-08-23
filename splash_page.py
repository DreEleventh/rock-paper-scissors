# This is the first page of the application 
# From here you have the option to either "register" or "login"

import tkinter as tk 

# Importing user built modules 
from register_page import register_window
from login_page import login_window

window = tk.Tk()

# Defining the window and some corresponding elements 
window.title("Rock Paper Scissors Splash-Page")
window.geometry("800x500")
window.resizable(0, 0)

# Importing the splash image and setting the backgroud color
splash_pic = tk.PhotoImage(file="splash_img.png")
window["background"] = "#390009"

# Setting the splash image on the page 
tk.Label(window, bg="#390009", image=splash_pic).pack(ipadx=200, ipady=20)

# Defining the frame that holds the login and register buttons 
button_frame = tk.Frame(bg="#390009")
button_frame.pack(fill=tk.X, ipadx=10, ipady=10)

# Defining the login button and it corresponding elements
login_bnt = tk.Button(master=button_frame, text="Login", bg="gold", command=login_window)
login_bnt.pack(side=tk.RIGHT, padx=10, ipadx=10)

# Defining the register button and its corresponding elements 
register_bnt = tk.Button(master=button_frame, text="Register", bg="gold", command=register_window)
register_bnt.pack(side=tk.RIGHT, padx=10, ipadx=10)

window.mainloop()
