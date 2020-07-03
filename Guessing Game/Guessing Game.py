from tkinter import *
from turtle import *
import random
global turns
global x
x = random.randint(1,100)
turns = 0
def guess():
    global x
    global turns
    guessval= int(textbox_input.get())
    textbox_input.delete(END)
    textbox_output.delete(0.0, END)
    textbox_output.insert(END, guessval)


    
    if guessval < x:
        textbox_output.insert(END,'\n That value is too low!')
        turns += 1
        if turns != 9:
            guess()
        elif turns == 9:
            end_game()


    elif guessval > x:
        textbox_output.insert(END,'\n That value is too high!')
        turns += 1
        if turns != 9:
            guess()
        elif turns == 9:
            end_game()

        
    elif guessval == x:
        textbox_output.insert(END,'\n Congrats, you guessed the number Correctly!')



def end_game():
    tboi = Turtle()
    tboi.screen.bgcolor('Black')
    tboi.pendown()
    tboi.hideturtle()
    tboi.pencolor("RED")
    tboi.write('Unlucky \n You ran out of tries', move= True, align="center", font=("Arial", 40, "normal"))



window = Tk()
window.title('Number Guessing Game (Tkinter version)')

window.geometry('500x500')
window.configure(background = 'linen')

input1_label = Label(window, text = 'Please write your guess below in the box provided', bg = 'linen')
input1_label.grid(row = 0, column = 0)
input2_label = Label(window, text = 'Guess:', bg = 'linen')
input2_label.grid(row = 1, column = 0)



output_label= Label(window, text = '\n Output:', bg = 'linen')
output_label.grid(row = 3 , column = 0)


textbox_input= Entry(window, width = 50)
textbox_input.grid(row = 2, column = 0)

textbox_output= Text(window, width = 50)
textbox_output.grid(row = 4, column = 0)


guess_button = Button(window, text = 'Enter', command = guess)
guess_button.grid(row = 1, column = 1)


window.mainloop()
