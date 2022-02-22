from tkinter import * #module
import random #module

ws = Tk()
ws.title('Josh Glynns Game') #name of he game
ws.geometry('600x400') #this is the size of the window of the game
ws.config(bg='#0000FF') #this is the colour of the background in hexadecimal code

ranNum = random.randint(0, 10) #the random number is chosen between 0 and 10
chance = 5 #variable #amount of attempts
var = IntVar()
disp = StringVar()

def check_guess():
    global ranNum
    global chance
    usr_ip = var.get()
    if chance > 0: #if statement
        if usr_ip == ranNum:
            msg = f'You won! {ranNum} is the right answer.' #if the number the player inputed is correct this message is displayed
        elif usr_ip > ranNum:
            chance -= 1
            msg = f'{usr_ip} is larger than the random number. You have {chance} attempt left.' #if the number that is chosen is > the random number then this message will be displayed
        elif usr_ip < ranNum: #else if
            chance -= 1
            msg = f'{usr_ip} is smaller than the random number. You have {chance} attempt left.'#if the number that is chosen is < the random number then this message will be displayed
        else:
            msg = 'Something went wrong!'
    else:
        msg = f'You Lost! you have {chance} attempt left.'

    disp.set(msg)


Label(
    ws,
    text='Guess My Number!', #title of the game
    font=('comic-sans', 20),
    relief=SOLID,
    padx=10,
    pady=10,
    bg='#FFFFFF'
).pack(pady=(10, 0))

Entry(
    ws,
    textvariable=var,
    font=('comic-sans', 18)
).pack(pady=(50, 10))

Button( 
    ws,
    text='Submit Guess', #use the button to submit the users guess
    font=('comic-sans', 18),
    command=check_guess
).pack()

Label(
    ws,
    textvariable=disp,
    bg='#0000FF', # colour of the label 
    font=('comic-sans', 14)
).pack(pady=(20,0))


ws.mainloop() # infinite loop always put at the end of codes with tkinter
