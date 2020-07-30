"""
Author: Andre McKenzie
ID Number: 20194313
Assignment: 3 - Rook Paper Scissors 
Date Given: May 31, 2020	
Date Due:  August 05, 2020

"""

import tkinter as tk 

def submit_button():
    pass

def login_win(event=None):
    """
    This function handles the process of login in to the 
    program after a user has registered. 
    This function takes the users data, checks if the data is correct.
    The user has 3 chances to login. 3 incorrect logins and the program closes. 
    """
    window = tk.Tk()

    window.title("Rook Paper Scissors - Login")
    window.geometry("350x300")
    window.resizable(0,0)
    tk.Label(master= window, text="Login", font=('Verdana', 20)).grid()

    # Defining the user name label and entry elements 
    user_name = tk.Label(master=window, font=('Verdana', 12),text = "Username: ")
    user_name_input_area = tk.Entry(master=window, width = 20)

    # Defining the user password label and entry elements 
    user_password = tk.Label(master=window, font=('Verdana', 14), text = "Password: ")
    user_password_entry_area = tk.Entry(master=window, width = 20)

    # Difining the submit button
    submitbtn= tk.Button(master=window,text="Submit")

    user_name.grid(row=3)
    user_name_input_area.grid(row=3, column=2, pady=15)

    user_password.grid(row=5)
    user_password_entry_area.grid(row=5, column=2, pady=10)

    submitbtn.grid(row=7, pady=20)

    window.mainloop()

def registration_win(event=None):
    """
    This function handles the registration process. 
    The user enter his/hers information and store it in 
    an internal database i.e a dictionary. 
    """
    window = tk.Tk()

    window.title("Rook Paper Scissors - Registration")
    window.geometry("350x300")
    window.resizable(0,0)
    label_0 = tk.Label(window, text="Registration Form",width=20, font=("bold", 15))
    label_0.place(x=90,y=53)


    label_1 = tk.Label(window, text="FullName",width=20,font=("bold", 10))
    label_1.place(x=100,y=130)

    entry_1 = tk.Entry(window,textvar=Fullname)
    entry_1.place(x=240,y=130)
    label_2 = tk.Label(window, text="Email",width=20,font=("bold", 10))
    label_2.place(x=100,y=180)

    entry_2 = tk.Entry(window,textvar=Email)
    entry_2.place(x=240,y=180)

    tk.Button(window, text="Register",  width=20,bg='green',fg='white').place(x=180,y=380)

    window.mainloop()

def rules(event=None):
    """
    This function displays the game rules. 
    """
    window = tk.Tk()

    window.title("Rook Paper Scissors - Rules")
    window.geometry("650x400")
    window.resizable(0,0)

    txt= tk.Text(master=window)
    txt.tag_configure('big', font=('Verdana', 15, 'bold'))
    
    txt.insert(tk.END, "\n \t\tRook Paper Scirrors Game Rules\n", 'big')

    txt.grid()
    window.mainloop()

def main_screen():
    """
    The main fucntion. Displays the main window of the program.
    This window holds the menu buttons and options and allows the user to access them.
    """
    window = tk.Tk()

    window.title("Rook Paper Scissors - Splash Screen")
    window.geometry("800x550")
    window.resizable(0,0)

    
    # window.configure()

    main_menu = tk.Menubutton(window, text="Main Menu")
    main_menu.menu = tk.Menu(main_menu)
    main_menu["menu"] = main_menu.menu

    # main_menu.menu.add_command(label="File", command=lambda: print("file option"))
    main_menu.menu.add_command(label="Rules", command=rules)
    main_menu.menu.add_command(label="Restart", command=lambda: print("restart option"))

    main_menu.grid(row= 1, column=1)

    user_menu =tk.Menubutton(window, text="User Options")
    user_menu.menu = tk.Menu(user_menu)
    user_menu["menu"] = user_menu.menu 

    user_menu.menu.add_command(label="User Registration", command=registration_win)
    user_menu.menu.add_command(label="Login", command=login_win)

    user_menu.grid(row=1, column=2)

    img_pic = tk.PhotoImage(file="Game.png")
    window["background"]='#390009'
    tk.Label(window,bg='#390009',image=img_pic).grid(row=4,column=0,padx=200,pady=20)

    button = tk.Button(window, text="Press here to play", bg='gold').grid(row=7,column=0,padx=15,pady=15)
    

    window.mainloop()

if __name__ == "__main__":
    main_screen()