import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title("title name here")
window.geometry('400x300')

options = ['default option', '1', '2', '3']
val = tk.StringVar(value=options[0])

EEE = ttk.OptionMenu(window, val, val.get(), *options)
EEE.pack()

def update():
  option = val.get()
  if option == "default option":
    print("Invalid Option")
  elif option == "1":
    print("picked 1")
  elif option == "2":
    print("picked 2")
  elif option == "3":
    print("picked 3")
  else:
    print("HOW DID YOU GET HERE")

btn = ttk.Button(master=window, text="Get Output", command=update)
btn.pack()

window.mainloop()
