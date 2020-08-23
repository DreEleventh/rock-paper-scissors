# A program that'll allow a user to register with the proram 

import tkinter as tk 
from tkinter import messagebox

def register_window(): 
    """Allows for the registration of a usier
    """

    window = tk.Tk()

    window.title("Rock-Paper-Scissors | Registration ")
    window.geometry("350x350")
    window.resizable(0, 0)
    window["background"]="#390009"

    fulname = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()


    window.mainloop()



if __name__ == "__main__":
    register_window()
