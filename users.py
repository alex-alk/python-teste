import datetime
import sqlite3
import time
from tkinter import *
from tkinter.ttk import Treeview
import bcrypt
import options
from style import font
from windowConfig import window
from tkinter.ttk import Button
from tkinter.ttk import Entry


frame_add_user = Frame(window, padx=10)
frame_show_questions = Frame(window, padx=10, pady=5)
frame_table = Frame(frame_show_questions)
frame_under_table = Frame(frame_show_questions)
label_users_info = Label(frame_add_user, text="", font=font)
vsb = Scrollbar(frame_table)
tree = Treeview(frame_table, column=("c1", "c2", "c3", "c4"), show='headings', yscrollcommand=vsb.set,
                selectmode="browse")


def show_add_user_page(frame):
    frame.grid_forget()
    frame_add_user.grid()
    window.geometry('{}x{}'.format(400, 230))
    window.resizable(width=False, height=False)
    label_users_info.config(text="", foreground="green")


def show_users_page(frame):
    print("showing page")
    frame.grid_forget()
    frame_show_questions.pack(expand=True, fill=BOTH, anchor=N)
    frame_table.pack(expand=True, fill=BOTH)
    frame_under_table.pack(fill=X)
    window.geometry('{}x{}'.format(800, 700))
    window.resizable(width=True, height=True)

    con = sqlite3.connect('teste.db')
    c = con.cursor()

    c.execute('SELECT * FROM users')
    users = c.fetchall()
    con.close()
    for i in tree.get_children():
        tree.delete(i)
    for row in users:
        row = [row[0], row[1], datetime.datetime.fromtimestamp(row[4]).strftime('%Y-%m-%d'), row[5]]
        tree.insert("", END, values=row)


def load_show_users_page():
    vsb.pack(fill=Y, side=RIGHT)
    vsb.config(command=tree.yview)
    tree.column("#1", anchor=CENTER, width=60, stretch=NO)
    tree.heading("#1", text="ID")
    tree.column("#2", anchor=W)
    tree.heading("#2", text="User")
    tree.column("#3", anchor=CENTER, width=100, stretch=NO)
    tree.heading("#3", text="Date added")
    tree.column("#4", anchor=CENTER, width=100, stretch=NO)
    tree.heading("#4", text="Score")
    tree.pack(expand=True, fill=BOTH)

    button_remove = Button(frame_under_table, text="Remove selected",
                           command=lambda: remove_user())
    button_remove.pack(pady=(5, 10), anchor=W)

    button_back = Button(frame_under_table, text="< Back", width=8,
                         command=lambda: options.back_to_options_pack(frame_show_questions))
    button_back.pack(pady=10)


def remove_user():
    x = tree.selection()[0]

    selected = tree.focus()
    question = tree.item(selected, "values")

    con = sqlite3.connect('teste.db')
    c = con.cursor()

    c.execute(f"DELETE FROM users WHERE id=" + question[0])
    con.commit()
    tree.delete(x)

    con.close()


def load_add_user_page():
    username_add = Entry(frame_add_user, font=font)
    password_add = Entry(frame_add_user, font=font, show="*")

    label_username = Label(frame_add_user, text="Username:", font=font)
    label_username.grid(column=1, row=1, pady=(40, 10), padx=(40, 0))

    username_add.grid(column=2, row=1, pady=(40, 10), sticky=W)

    label_password = Label(frame_add_user, text="Password:", font=font)
    label_password.grid(column=1, row=2, padx=(40, 0))

    password_add.grid(column=2, row=2, sticky=W)

    label_users_info.grid(column=2, row=3, sticky=W)

    button = Button(frame_add_user, text="Add", width=10,
                    command=lambda: save_user(username_add, password_add, label_users_info))
    button.grid(column=2, row=4, pady=(10, 25))
    button_back = Button(frame_add_user, text="< Back", width=8,
                         command=lambda: options.back_to_options(frame_add_user))
    button_back.grid(column=1, row=5, sticky=S+W)


def save_user(username, password,  label):
    if username.get() == "" or password.get() == "":
        label.config(text="Bad username or password.", foreground="red")
    else:
        now = int(time.time())
        passwd = bytes(password.get(), encoding='utf-8')
        salt = bcrypt.gensalt()
        password_db = bcrypt.hashpw(passwd, salt)

        con = sqlite3.connect('teste.db')
        c = con.cursor()

        c.execute(f"SELECT * FROM users where username=?", (username.get(),))
        found_user = c.fetchone()

        if not found_user:
            c.execute(f"INSERT INTO users (username, password, salt, created_at) VALUES (?, ?, ?, {now})",
                      (username.get(), password_db, salt))
            con.commit()
            label.config(text="User added.", foreground="green")
        else:
            label.config(text="Username taken.", foreground="red")

        con.close()

        username.delete(0, END)
        password.delete(0, END)
        username.focus()
