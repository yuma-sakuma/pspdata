from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Hm . . . ?")
window.geometry("1280x720")

chk_state = IntVar()
chk_state.set(1)

chackb= Checkbutton(window, text="Choose partfinder")
chackb.grid(column=0,row=0)

window.mainloop()