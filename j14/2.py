from tkinter import messagebox

balance = 500

amount = int(input("enter amount"))

if amount > balance:
    messagebox.showerror("mojoodi", "mojoodi hesab e shoma kafi nist")
else:
    balance -= amount
    # messagebox.showinfo("bardasht", f"bardasht anjam shod\nmojoodi : {balance}")
    messagebox.showwarning("bardasht", f"bardasht anjam shod\nmojoodi : {balance}")