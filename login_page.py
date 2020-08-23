# Allows a previously registered user to login to the program 

import tkinter as tk 
from tkinter import messagebox

loginDict={}

def login_window():
    """This screen allows users to login to the program 
    """
    
    def submit_button(): 
        """
        This sub function handles the user info retrieval and comparison.
        It takes the users login data as input and checkes if it matches
        the user data stored.
        """
        try:
            # Opens the file storing the users data and loads it into memory
            file = open("userInfo.txt", 'r')
            for line in file:
                if ':' in line:
                    key,value = line.split(':', 1)
                    cvalue = len(value)-1
                    value = value[0:cvalue]
                    loginDict[key]=value
                else:
                    pass
            # Assigns the loaded user data to relevant variables
            name = loginDict.get('username')
            code = loginDict.get('password')
            
            # Checks if the information on file matches what the user entered
            if(name==username.get() and code==password.get()):
                # game_win()
                login.destroy()
            else:
                tk.messagebox.showinfo("ERROR", "Incorrect Username or Password")
        except ValueError:
            pass

    login = tk.Tk()

    # Defining the window and some corresponding elements
    login.title("Rock Paper Scissors | Login")
    login.geometry("350x300")
    login.resizable(0, 0)
    login["background"]="#390009"

    # Defining and tracking variables with StringVar()
    username = tk.StringVar()
    password = tk.StringVar()

    # Difining the legend frame that'll hold all the imput fields
    legend = tk.LabelFrame(login, text="Login Page", bg='#390009', fg='gold', width=20, font=("Vardana", 20) )
    legend.grid(row=2, column=0, padx=25, pady=30)

    # Difining the username label and entry field
    userName = tk.Label(legend, text="Username: ", bg='#390009', fg='gold', font=("Vardana", 15))
    userName.grid(row=2, pady=20, padx=3)
    userName_entry = tk.Entry(legend, textvariable=username)
    userName_entry.grid(row=2, column=2, pady=20, padx=3)

    # Difining the password label and entry field
    passWord = tk.Label(legend, text="Password: ", bg='#390009', fg='gold', font=("Vardana", 15))
    passWord.grid(row=3, pady=20, padx=3)
    password_entry = tk.Entry(legend, textvariable=password, show='*')
    password_entry.grid(row=3, column=2, pady=10)

    # Difining the submit button 
    submit_bnt = tk.Button(legend, text='Submit', bg='gold', command=submit_button)
    submit_bnt.grid(row=4, column=0, pady=10)

    login.mainloop()

if __name__ == "__main__":
    login_window()