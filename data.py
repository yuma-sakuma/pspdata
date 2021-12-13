from tkinter import *

window = Tk()
x = 1
window.title("?")

window.geometry("400x400")

txt = Label(window, text="Hello User press button", font=("UD Digi Kyokasho N=B Bold",40))
txt.grid(column=0,row=0)

tb = Entry(window, width=20, state="disabled")
tb.grid(column=0,row=2)

def aclick():
    global x
    tbclick = tb.get()
    if x == 35:
        txt.configure(text="Um . . .")
        x += 1
    elif x == 100:
        txt.configure(text="you press button for what?")
        x += 1
    elif x == 101:
        txt.configure(text=tbclick)
    else:
        txt.configure(text=str(x)+" click ago")
        x += 1

def click():
    tbclick = tb.get()
    txt.configure(text=tbclick)

bt = Button(window,text=("click me"),font=("Arail" , 25), bg="red" , fg='black', command=click)
bt.grid(column=0,row=1)

#window.mainloop()