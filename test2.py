from tkinter import *
from tkinter import ttk

root=Tk()
mainframe= ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0,row=0, sticky="N W E S")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)

def view_name(*agrs):
    user_name=str(name.get())
    user.set(user_name)

name= StringVar()
name_entry= ttk.Entry(mainframe,width=10,textvariable=name)
name_entry.grid(column=3, row=1, sticky="W E")

user=StringVar()
ttk.Label(mainframe,textvariable=user).grid(column=2, row=2, sticky="W E")

ttk.Button(mainframe, text="Enter", command=view_name).grid(column=2, row=3, sticky="W E")

ttk.Label(mainframe, text="Enter your name").grid(column=1,row=1,sticky="W E")
ttk.Label(mainframe,text="Welcome to Python").grid(column=1, row=2, sticky="W E")

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)
name_entry.focus()
root.mainloop()