from tkinter import *
from random import choice


names = []


def add_to_list():
    name = name_entry.get().strip()

    if name == "":
        status_label.config(text="لطفاً یک نام وارد کنید.")
        return

    if name in names:
        status_label.config(text="این نام قبلاً اضافه شده است.")
        return

    names.append(name)
    name_entry.delete(0, END)
    # name_entry.focus()

    status_label.config(text=f"{name} اضافه شد — تعداد افراد: {len(names)}")


def draw_winner():
    if len(names) <= 1:
        winner_label.config(text="ابتدا حداقل دو نفر اضافه کنید.")
        return

    winner = choice(names)
    winner_label.config(text=f"برنده: {winner}")


root = Tk()
root.title("برنامه قرعه‌کشی")
root.geometry("500x500")
root.resizable(False, False)

font = ("Vazir", 18, "bold")

name_lbl = Label(root, text="اسامی شرکت‌کنندگان را وارد کنید", font=font).pack(pady=20)

name_entry = Entry(root, font=font, justify="center")
name_entry.pack()
name_entry.focus()

add_btn = Button(root, text="اضافه کردن", font=font, command=add_to_list).pack(pady=15)

draw_winner_btn = Button(root, text="قرعه‌کشی", font=font, command=draw_winner).pack(pady=10)

status_label = Label(root, text="", font=("Vazir", 12))
status_label.pack(pady=10)

winner_label = Label(root, text="", font=font)
winner_label.pack(pady=15)

root.mainloop()