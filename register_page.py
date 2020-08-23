# A program that'll allow a user to register with the proram 

import tkinter as tk 
from tkinter import messagebox

def register_window(): 
    """
    Allows for the registration of a usier. 
    The user will be asked to enter their fullname, username, and password    
    """
    def register_user():
        pass
    window = tk.Tk()

    window.title("Rock-Paper-Scissors | Registration ")
    window.geometry("350x350")
    window.resizable(0, 0)
    window["background"]="#390009"

    fulname = tk.StringVar()
    username = tk.StringVar()
    password = tk.StringVar()
    
    legend = tk.LabelFrame(master=window, text="Registration Form", bg="#390009", fg='gold', width=20, font=("Vardana", 20))
    legend.grid(row=2, column=0, padx=25, pady=30)

    fulname_label= tk.Label(legend, text="Fullname: ", bg='#390009', fg='gold', font=("Vardana", 15))
    fulname_label.grid(row=3, column=0, padx=3, pady=20)

    fulname_entry = tk.Entry(legend, textvariable=fulname, width=20)
    fulname_entry.grid(row=3, column=1, padx=3, pady=20)

    username_label = tk.Label(legend, text="User Name: ", bg='#390009', fg='gold', font=("Vardana", 15))
    username_label.grid(row=4, column=0, padx=3, pady=20)

    username_entry = tk.Entry(legend, textvariable=username, width=20)
    username_entry.grid(row=4, column=1, padx=3, pady=20)

    password_label = tk.Label(legend, text="Password: ", bg='#390009', fg='gold', font=("Vardana", 15))
    password_label.grid(row=5, column=0, padx=3, pady=20)

    password_entry = tk.Entry(legend, width=20, textvariable=password, show="*")
    password_entry.grid(row=5, column=1, padx=3, pady=20)

    sumbit_bnt = tk.Button(legend, text='Submit', bg='gold', command="###")
    sumbit_bnt.grid(row=6, padx=3, pady=10)

    window.mainloop()



if __name__ == "__main__":
    register_window()
