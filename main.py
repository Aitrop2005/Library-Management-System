from tkinter import *
from tkinter import messagebox
import sqlite3

root = Tk()
root.title("Library Management System")
root.geometry("700x500")

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    qty = qty_entry.get()

    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO books(title,author,quantity) VALUES(?,?,?)",
        (title, author, qty)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo("Success", "Book Added")

def view_books():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()

    listbox.delete(0, END)

    for row in rows:
        listbox.insert(
            END,
            f"{row[0]} | {row[1]} | {row[2]} | Qty: {row[3]}"
        )

    conn.close()

def delete_book():
    book_id = id_entry.get()

    conn = sqlite3.connect("library.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM books WHERE id=?", (book_id,))

    conn.commit()
    conn.close()

    messagebox.showinfo("Deleted", "Book Removed")

Label(root, text="Book ID").pack()
id_entry = Entry(root)
id_entry.pack()

Label(root, text="Title").pack()
title_entry = Entry(root)
title_entry.pack()

Label(root, text="Author").pack()
author_entry = Entry(root)
author_entry.pack()

Label(root, text="Quantity").pack()
qty_entry = Entry(root)
qty_entry.pack()

Button(root, text="Add Book", command=add_book).pack()
Button(root, text="View Books", command=view_books).pack()
Button(root, text="Delete Book", command=delete_book).pack()

listbox = Listbox(root, width=80)
listbox.pack()

root.mainloop()
