import tkinter
import random
from tkinter import messagebox

colours = ['Red','Blue','Green','Pink','Black',
           'Yellow','Orange','White','Purple','Brown']

score = 0
timeleft = 30

def startGame(event):
    if timeleft == 30:
        countdown()

    nextColour()

def nextColour():
    global score
    global timeleft

    if timeleft > 0:
        e.focus_set()

        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(colours)

        label.config(fg = str(colours[1]), text = str(colours[0]))

        scoreLabel.config(text="Score: " + str(score))

    else:
        end_game()

def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text = "Time left: " + str(timeleft))

        timeLabel.after(1000, countdown)
    else:
        end_game()

def end_game():
    messagebox.showinfo("Game Over", "Your final score is: " + str(score))
    play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
    if play_again:
        reset_game()
    else:
        root.destroy()

def reset_game():
    global score, timeleft
    score = 0
    timeleft = 30
    scoreLabel.config(text="Score: " + str(score))
    countdown()

root = tkinter.Tk()

root.title("COLORGAME")
root.geometry("375x200")

instructions = tkinter.Label(root, text="Type in the colour"
                             "of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

e = tkinter.Entry(root)

root.bind('<Return>', startGame)
e.pack()

e.focus_set()

root.mainloop()
