import tkinter
from tkinter import*
import time
red=0
roundtime = 90

def time_counter():
    if roundtime == 90:
        startGame()

def startGame(event):
        
        if timeleft == 30:
            countdown()


def countdown():
        
        global timeleft
        timeleft=30
        if timeleft > 0:

            timeleft -= 1
            
            roundtime.config(text = "Time left: "
                                + str(timeleft))
                                            
            roundtime.after(1000, countdown)  

timeLabel = tkinter.Label( text = "Time left: " +
                (timeleft), font = ('Helvetica', 12))
                
timeLabel.pack() 

root= tkinter.Tk()
root.bind('<Return>', startGame)
root.mainloop()


def scoreboard():
    
        global red
        global green
        global roundtime
        green=0
        y=int(input('Enter green score:'))
        
        green+=y
        return_greenvalues()
        print('red score:')
        print(red)
        print('green score:')
        print(green)
        red=0
        b=int(input('Enter red score:'))
        red+=b
        return_redvalues()
        print('red score:')
        print(red)
        print('green score:')
        print(green)
        
       
def return_redvalues():
    return(red)
def return_greenvalues():
    green=0
    return(green)

time_counter()
