from tkinter import *
from tkinter import messagebox

def showFullName():
    firstname = fname_ent.get()
    lastname = lname_ent.get()
    fullname = f"نام کامل شما : {firstname} {lastname}"
    fullname_lbl.config(text=fullname)

bg_color = "#66BFE2"
font=("vazir", 20, "bold")
e_font=("vazir", 16, "bold")

root = Tk()
root.title("برنامه نام")
root.geometry("400x400")
root.resizable(0, 0)
root.config(bg=bg_color)

fname_lbl = Label(root, text="نام", font=font, bg=bg_color).pack()
fname_ent = Entry(root, font=e_font)
fname_ent.pack()

lname_lbl = Label(root, text="نام خانوادگی", font=font, bg=bg_color).pack()
lname_ent = Entry(root, font=e_font)
lname_ent.pack()

fullname_btn = Button(root, text="نمایش نام", font=font, command=showFullName).pack(pady=20)

fullname_lbl = Label(root, text="", font=font, bg=bg_color)
fullname_lbl.pack()

messagebox.showinfo("ورود", "به برنامه خوش آمدید")

root.mainloop()