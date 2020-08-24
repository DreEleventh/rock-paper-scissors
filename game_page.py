import tkinter as tk 
import random
from PIL import ImageTk, Image 

player_score = 0 
computer_score = 0 
ties = 0 
rounds = 0  

player_losses = 0 
computer_losses = 0

images = ['01.png', '02.png', '03.png']

def game_window():
    
    window = tk.Tk()
    window.geometry("590x400")
    window.title("Rock-Paper-Scissors")
    window.rowconfigure(8, minsize=60)
    window.columnconfigure([0,1,2,3,4,5, 7, 8, 9], minsize=60)

    window["background"]='#390009'


    optVar = tk.IntVar()
    optVar.set(0)

    # Menu bar and menu items 
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

    rock = tk.Radiobutton(select_option, text="Rock", font=('Verdana', 12), pady=20, variable=optVar, value=1, bg='#390009', fg="gold", command=select_opt)
    rock.grid(row=2, column=0, padx=10)

    paper=tk.Radiobutton(select_option, text="Paper", font=('Verdana', 12), pady=20, variable=optVar, value=2, bg='#390009', fg="gold", command=select_opt)
    paper.grid(row=2, column=1, padx= 10)

    scissors=tk.Radiobutton(select_option, text="Scissors", font=('Verdana', 12), pady=20, variable=optVar, value=3, bg='#390009', fg="gold", command=select_opt)
    scissors.grid(row=2, column=2, padx=10)

    submit_btn = tk.Button(select_option, text="Submit", bg='#390009', fg="gold", command=lambda:[submit(), cnt_rounds()])
    submit_btn.grid(row=3, column=2, padx=30, pady=10)



    player_img = tk.Label(window)
    player_img.grid(row=1, column=2, pady=5)


    # Section holds the scores for the game: Wins, Loses and Ties
    score_frame = tk.LabelFrame(window, text="Scores:", font=('Vardana', 18), bg='#390009', fg="gold",)
    score_frame.grid(row=5, pady=30, padx=10)

    user_score = tk.Label(score_frame, text='Player Wins:', font=('Verdana', 12), bg='#390009', fg="gold",)
    user_score.grid(row=6, column=0, padx=5, pady=5)

    user_points = tk.Label(score_frame, bg='#390009', fg="gold",) 
    user_points.grid(row=7, column=0)

    comp_score = tk.Label(score_frame, text="Compter Wins: ", font=('Verdana', 12), bg='#390009', fg="gold",)
    comp_score.grid(row=6, column=2, padx=5, pady=5)
    comp_points = tk.Label(score_frame, bg='#390009', fg="gold",)
    comp_points.grid(row=7, column=2)

    tie_score = tk.Label(score_frame, text="Ties: ", font=('Verdana', 12), bg='#390009', fg="gold",)
    tie_score.grid(row=6, column=3, padx=5, pady=5)
    tie_points = tk.Label(score_frame, bg='#390009', fg="gold",)
    tie_points.grid(row=7, column=3)

    user_losses = tk.Label(score_frame, text="Player Losses:", font=('Verdana', 12), bg='#390009', fg="gold",)
    user_losses.grid(row=8, column=0, padx=5, pady=5)
    user_losses_cnt = tk.Label(score_frame, bg='#390009', fg="gold",)
    user_losses_cnt.grid(row=9, column=0)

    comp_losses = tk.Label(score_frame, text="Computer losses:", font=('Verdana', 12), bg='#390009', fg="gold",)
    comp_losses.grid(row=8, column=2, padx=5, pady=5)
    comp_losses_cnt = tk.Label(score_frame, bg='#390009', fg="gold",)
    comp_losses_cnt.grid(row=9, column=2)


    window.mainloop()

if __name__ == "__main__":
    game_window()