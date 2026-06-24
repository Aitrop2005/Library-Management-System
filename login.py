from tkinter import *
from tkinter import messagebox

def login():
    username = user.get()
    password = pwd.get()

    if username == "admin" and password == "admin123":
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Login")

root = Tk()
root.geometry("300x200")

Label(root, text="Username").pack()
user = Entry(root)
user.pack()

Label(root, text="Password").pack()
pwd = Entry(root, show="*")
pwd.pack()

Button(root, text="Login", command=login).pack()

root.mainloop()
