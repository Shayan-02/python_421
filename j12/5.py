from tkinter import *


def show_fullname():
    fname = fname_ent.get()
    lname = lname_ent.get()
    fullname = fname + " " + lname
    fullname_lbl.config(text=fullname)


root = Tk()

main_font = ("vazir", 20, "bold")
secondary_font = ("vazir", 16, "bold")

root.geometry("450x450")
root.title("fullname app")
root.resizable(width=False, height=False)

Label(root, text="نام", fg="blue", font=main_font).pack()
fname_ent = (Entry(root, font=secondary_font))
fname_ent.pack(pady=15)
Label(root, text="نام خانوادگی", fg="blue", font=main_font).pack()
lname_ent = (Entry(root, font=secondary_font))
lname_ent.pack(pady=15)
fullname_btn = Button(root, font=main_font, text="نمایش نام کامل", width=15, bg="lightgreen", command=show_fullname).pack()
fullname_lbl = Label(root, text="", font=main_font, fg="green")
fullname_lbl.pack()


root.mainloop()