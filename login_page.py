# Allows a previously registered user to login to the program 

import tkinter as tk 
from tkinter import messagebox

loginDict={}

def login_window():
    """This screen allows users to login to the program 
    """
    
    def submit_button(): 
        """Processes the 
        """
        try:
            file = open("userInfo.txt", 'r')
            for line in file:
                if ':' in line:
                    key,value = line.split(':', 1)
                    cvalue = len(value)-1
                    value = value[0:cvalue]
                    loginDict[key]=value
                else:
                    pass
            name = loginDict.get('username')
            code = loginDict.get('password')
            
            if(name==username.get() and code==password.get()):
                # game_win()
                login.destroy()
            else:
                tk.messagebox.showinfo("ERROR", "Incorrect Username or Password")
                login.quit()
        except ValueError:
            pass

    login = tk.Tk()
    login.title("Rock Paper Scissors | Login")
    login.geometry("350x300")
    login.resizable(0, 0)
    login["background"]="#390009"

    username = tk.StringVar()
    password = tk.StringVar()

    legend = tk.LabelFrame(login, text="Login Page", bg='#390009', fg='gold', width=20, font=("Vardana", 20) )
    legend.grid(row=2, column=0, padx=25, pady=30)

    userName = tk.Label(legend, text="Username: ", bg='#390009', fg='gold', font=("Vardana", 15))
    userName.grid(row=2, pady=20, padx=3)

    userName_entry = tk.Entry(legend, textvariable=username)
    userName_entry.grid(row=2, column=2, pady=20, padx=3)

    passWord = tk.Label(legend, text="Password: ", bg='#390009', fg='gold', font=("Vardana", 15))
    passWord.grid(row=3, pady=20, padx=3)

    password_entry = tk.Entry(legend, textvariable=password, show='*')
    password_entry.grid(row=3, column=2, pady=10)

    submit_bnt = tk.Button(legend, text='Submit', bg='gold', command=submit_button)
    submit_bnt.grid(row=4, column=0, pady=10)

    login.mainloop()

if __name__ == "__main__":
    login_window()