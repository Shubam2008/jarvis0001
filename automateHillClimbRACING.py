from tkinter import*
from time import sleep
import pyautogui
from pynput.keyboard import Key,Controller

keyboard = Controller()
t = Tk()

def go():
    sleep(1.5)
    pyautogui.press("enter")
    sleep(1)
    keyboard.press(Key.right)

def re():
    sleep(1.5)
    pyautogui.press("enter")
    go()

    
   

t.title("GameAuto")
t.geometry("200x150")
t.configure(bg="lightblue")

t1 = Button(text=" Start  ",command=go)
t1.configure(bg="lightgreen")
t1.pack()


t2 = Button(text="again",command=re)
t2.configure(bg="lightgreen")
t2.pack()



t.mainloop()         



###first f all tk window apper
## second click on butoon 
# after one second game will automate
#after losing match click on new  button 
# repeat it 














