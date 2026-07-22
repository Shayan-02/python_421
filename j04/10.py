from tkinter import *

name = "علی"
family = "رضایی"
color = "#C967CC"
font=("vazir", 30, "bold")

root = Tk()
root.config(bg=color)

fname_lbl = Label(root, text=name, font=font, fg="blue", bg=color).pack()
lname_lbl = Label(root, text=family, bg=color, font=font).pack()

root.mainloop()