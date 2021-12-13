from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("Hm . . . ?")
window.geometry("1280x720")

combo = Combobox(window)
combo["values"] = [1,2,3,4,5,6]
combo.current(0)
combo.grid(column=0,row=0)

window.mainloop()