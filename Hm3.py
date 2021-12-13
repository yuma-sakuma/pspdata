import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import figure
from tkinter import *
from tkinter.ttk import *


df = pd.read_csv("data-firearm.csv")
df.fillna(0,inplace=True)

#combo = Combobox(window)
#combo.grid(column=0,row=0)

cty = []
handGun = []
permit = []
recheck = []

x = 0
y = 0
z = 0

#2-------------------------------------------------------------------------------------------------------------

#window = Tk()
#window.title("handgun")
#window.geometry("1280x720")

#for i in range(len(df)):
#  if df['state'].duplicated().loc[i] == False:
#    txt = Label(window, text=df['state'][i], font=("UD Digi Kyokasho N=B Bold",8))
#    txt.grid(column=0,row=x)
#    x += 1

#for i in range(55):
#  A = 0
#  for j in range(len(df['state'])):
#    if df['state'][j] == df['state'][i]:
#      A += df['handgun'][j]
#  tx = Label(window, text="=", font=("UD Digi Kyokasho N=B Bold",8))
#  tx.grid(column=1,row=y)
#  txthandgun = Label(window, text=A, font=("UD Digi Kyokasho N=B Bold",8))
#  txthandgun.grid(column=2,row=z)
#  y += 1
#  z += 1

#3-------------------------------------------------------------------------------------------------------------

# window = Tk()
# window.title("Allgun")
# window.geometry("1280x1080")

# for i in range(len(df)):
#  if df['state'].duplicated().loc[i] == False:
#    txt = Label(window, text=df['state'][i], font=("UD Digi Kyokasho N=B Bold",8))
#    txt.grid(column=0,row=x)
#    x += 1

# for i in range(55):
#  A = 0
#  for j in range(len(df['state'])):
#    if df['state'][j] == df['state'][i]:
#      A += df['handgun'][j]
#      A += df['long_gun'][j]
#      A += df['other'][j]
#  tx = Label(window, text="=", font=("UD Digi Kyokasho N=B Bold",8))
#  tx.grid(column=1,row=y)
#  txthandgun = Label(window, text=A, font=("UD Digi Kyokasho N=B Bold",8))
#  txthandgun.grid(column=2,row=z)
#  y += 1
#  z += 1

#4-------------------------------------------------------------------------------------------------------------

#window = Tk()
#window.title("Norecheck")
#window.geometry("1280x1080")

#for i in range(len(df)):
#  if df['state'].duplicated().loc[i] == False:
#    txt = Label(window, text=df['state'][i], font=("UD Digi Kyokasho N=B Bold",8))
#    txt.grid(column=0,row=x)
#    x += 1

#for i in range(55):
#  A = 0
#  B = 0
#  for j in range(len(df['state'])):
#    if df['state'][j] == df['state'][i]:
#      A += df['permit'][j]
#      B += df['permit_recheck'][j]
#  permit.append(A)
#  recheck.append(B)

#for n in range(55):
#  m = permit[n]-recheck[n]
#  if m <= 0:
#    m = 0
#  tx = Label(window, text="=", font=("UD Digi Kyokasho N=B Bold",8))
#  tx.grid(column=1,row=y)
#  txthandgun = Label(window, text=m, font=("UD Digi Kyokasho N=B Bold",8))
#  txthandgun.grid(column=2,row=z)
#  y += 1
#  z += 1

#combo['values'] = cty  

window.mainloop()