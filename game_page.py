import tkinter as tk 
import random
from PIL import ImageTk, Image 

import sys 
import os

player_score = 0 
computer_score = 0 
ties = 0 
rounds = 0  

player_losses = 0 
computer_losses = 0

images = ['01.png', '02.png', '03.png']


def rules(event=None):
    """
    Displays the game rules. 
    """
   
    display_rules = """
                    Rook Paper Scirrors Game Rules


    Select one of the 3 options: Rock, Paper or Scissors. Once selected 
    click the submit button to submit you answer. A pictorial representation
    of your option will then be dicplayed. You have 10 rounds and the game 
    will then end.
                    """
    window = tk.Tk()

    window.title("Rook Paper Scissors - Rules")
    window.geometry("550x350")
    window.resizable(0,0)

    txt= tk.Text(master=window)
    txt.tag_configure('big', font=('Verdana', 10))
    
    txt.insert(tk.END, display_rules, 'big')
    txt.configure(state='disabled')
    txt.pack()
    
    window.mainloop()

def re_spring():
    """Restarts the program when 'Restart is clicked in the file menue
    """
    python = sys.executable
    os.execl(python, python, * sys.argv)

def game_window():


    def submit():
        """Fuction that displays the players and computers score"""
        global player_score
        global computer_score 
        global ties
        global player_losses
        global computer_losses
        
        option = optVar.get()

        # Generates a randome number and stores it in variable computer_opt
        computer_opt = random.randint(1, 3)

        if option == computer_opt:
                ties = ties + 1 
                tie_points.config(text = str(ties))
        elif((option - computer_opt) % 3 == 1):
            player_score = player_score + 1
            computer_losses= computer_losses + 1
            user_points.config(text = str(player_score))
            comp_losses_cnt.config(text = str(computer_losses))
        elif ((option - computer_opt) % 3 !=1):
            computer_score = computer_score + 1
            player_losses = player_losses + 1
            comp_points.config(text= str(computer_score))
            user_losses_cnt.config(text= str(player_losses))


    def select_image():
        """This sub function that displays the players game selection"""
        # Accepts the users game option selection and assigns it tp a variable
        game_opt = optVar.get()
        # Selecting an image depending on the option given
        if game_opt == 1: 
            img = images[0]
        elif game_opt == 2: 
            img = images[1]
        else: 
            img = images[2]

        # Displaying the selected image to the user
        img = Image.open(img)
        img = ImageTk.PhotoImage(img)
        player_img.img = img 
        player_img['image'] = img    


    def cnt_rounds(): 
        """Sub function that tracts the rounds played and ends the 
        game when the player losses or wins 10 times 
        """
        global rounds
        rounds = rounds + 1
        if player_score == 10 or player_losses == 10: 
            window.destroy()


    # Defining the window and some corresponding elements
    window = tk.Tk()
    window.geometry("590x400")
    window.title("Rock-Paper-Scissors")
    window.rowconfigure(8, minsize=60)
    window.columnconfigure([0,1,2,3,4,5, 7, 8, 9], minsize=60)

    window["background"]='#390009'


    optVar = tk.IntVar()
    optVar.set(0)

    # Defining the menu bar and menu items 
    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Rules", command=rules)
    filemenu.add_command(label="Restart", command=re_spring)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    window.config(menu=menubar)

    # Section that holds the options rock paper scissors 
    select_option = tk.LabelFrame(window, text="Select option: ", font=('Vardana', 18), bg='#390009', fg="gold",)
    select_option.grid(row=1, pady=30, padx=10)
    # Difining the rock redio button
    rock = tk.Radiobutton(select_option, text="Rock", font=('Verdana', 12), pady=20, variable=optVar, value=1, bg='#390009', fg="gold", command=select_image)
    rock.grid(row=2, column=0, padx=10)
    # Difining the paper redio button
    paper=tk.Radiobutton(select_option, text="Paper", font=('Verdana', 12), pady=20, variable=optVar, value=2, bg='#390009', fg="gold", command=select_image)
    paper.grid(row=2, column=1, padx= 10)
    # Difining the scissors redio button
    scissors=tk.Radiobutton(select_option, text="Scissors", font=('Verdana', 12), pady=20, variable=optVar, value=3, bg='#390009', fg="gold", command=select_image)
    scissors.grid(row=2, column=2, padx=10)
    # Difining the submit button
    # Lambda functions allow for the envoking of two funtions when the submut button it pressed
    submit_btn = tk.Button(select_option, text="Submit", bg='#390009', fg="gold", command=lambda:[submit(), cnt_rounds()])
    submit_btn.grid(row=3, column=2, padx=30, pady=10)


    # Code that'll display correcponding image to whatever option the user selected
    player_img = tk.Label(window)
    player_img.grid(row=1, column=2, pady=5)


    # Section holds the scores for the game: Wins, Losses and Ties
    score_frame = tk.LabelFrame(window, text="Scores:", font=('Vardana', 18), bg='#390009', fg="gold",)
    score_frame.grid(row=5, pady=30, padx=10)

    # Difining the users score counter label and counter
    user_score = tk.Label(score_frame, text='Player Wins:', font=('Verdana', 12), bg='#390009', fg="gold",)
    user_score.grid(row=6, column=0, padx=5, pady=5)
    user_points = tk.Label(score_frame, bg='#390009', fg="gold",) 
    user_points.grid(row=7, column=0)

    # Difining the computers score label and counter
    comp_score = tk.Label(score_frame, text="Compter Wins: ", font=('Verdana', 12), bg='#390009', fg="gold",)
    comp_score.grid(row=6, column=2, padx=5, pady=5)
    comp_points = tk.Label(score_frame, bg='#390009', fg="gold",)
    comp_points.grid(row=7, column=2)

    # Difining the tie score label and counter
    tie_score = tk.Label(score_frame, text="Ties: ", font=('Verdana', 12), bg='#390009', fg="gold",)
    tie_score.grid(row=6, column=3, padx=5, pady=5)
    tie_points = tk.Label(score_frame, bg='#390009', fg="gold",)
    tie_points.grid(row=7, column=3)

    # Difining the users losses label and counter
    user_losses = tk.Label(score_frame, text="Player Losses:", font=('Verdana', 12), bg='#390009', fg="gold",)
    user_losses.grid(row=8, column=0, padx=5, pady=5)
    user_losses_cnt = tk.Label(score_frame, bg='#390009', fg="gold",)
    user_losses_cnt.grid(row=9, column=0)

    # Difining the computers losses label and counter
    comp_losses = tk.Label(score_frame, text="Computer losses:", font=('Verdana', 12), bg='#390009', fg="gold",)
    comp_losses.grid(row=8, column=2, padx=5, pady=5)
    comp_losses_cnt = tk.Label(score_frame, bg='#390009', fg="gold",)
    comp_losses_cnt.grid(row=9, column=2)


    window.mainloop()

if __name__ == "__main__":
    game_window()