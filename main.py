import time
from tkinter import *
import sqlite3
from tkinter.ttk import Treeview

import bcrypt as bcrypt
import tksheet

window = Tk()
frame_login = Frame(window, padx=40, pady=40)
frame_options = Frame(window, padx=40, pady=40)
frame_add_user = Frame(window)
frame_show_users = Frame(window)
frame_add_questions = Frame(window)

frame_login.grid()
window.title("Login")
window.minsize(width=400, height=200)
window.resizable(width=False, height=False)
window.config(padx=5, pady=7)

font = ("Arial", 12)

input_username = Entry(frame_login, font=font)
input_password = Entry(frame_login, font=font, show="*")
label_error = Label(frame_login, text="", font=font, foreground="red")

username_add = Entry(frame_add_user, font=font)
password_add = Entry(frame_add_user, font=font, show="*")
user_added_info = Label(frame_add_user, text="", font=font, foreground="red")

con = sqlite3.connect('teste.db')
c = con.cursor()


def check_credentials():

    c.execute('SELECT * FROM users WHERE username=?', (input_username.get(),))
    user = c.fetchone()

    # todo: move these
    frame_login.grid_forget()
    show_admin_option()
    window.title("Dashboard")

    if user:
        user_salt = user[2]
        passwd = bytes(input_password.get(), encoding='utf-8')
        password = bcrypt.hashpw(passwd, user_salt)

        if user[2] == password:
            window.title("Dashboard")
            frame_login.grid_forget()
        else:
            label_error.config(text="Wrong username/password.")
    else:
        label_error.config(text="User not found.")


def show_login_page():
    label_username = Label(frame_login, text="Username:", font=font)
    label_username.grid(column=1, row=1, pady=(0, 10))

    input_username.grid(column=2, row=1, pady=(0, 10), sticky=W)

    label_password = Label(frame_login, text="Password:", font=font)
    label_password.grid(column=1, row=2)

    input_password.grid(column=2, row=2, sticky=W)

    label_error.grid(column=2, row=3, sticky=W)

    button_login = Button(frame_login, text="Login", font=font, width=10, command=check_credentials)
    button_login.grid(column=2, row=4, pady=10, sticky=W)


show_login_page()


def show_admin_option():
    frame_options.grid()
    button_add_questions = Button(frame_options, text="Add questions", font=font, width=13, command=admin_add_questions)
    button_add_questions.grid(column=1, row=1, pady=10, padx=20)
    button_add_user = Button(frame_options, text="Add user", font=font, width=13, command=admin_add_user)
    button_add_user.grid(column=2, row=1, pady=10)
    button_add_user = Button(frame_options, text="Show questions", font=font, width=13, command=admin_show_questions)
    button_add_user.grid(column=1, row=2, pady=10)
    button_add_user = Button(frame_options, text="Show users", font=font, width=13, command=admin_show_users)
    button_add_user.grid(column=2, row=2, pady=10)
    button_back = Button(frame_options, text="< Back", font=font, width=8,
                         command=lambda: back_to_login_page(frame_add_user))
    button_back.grid(column=1, row=3, sticky=W)


def admin_show_questions():
    pass


def admin_show_users():
    frame_options.grid_forget()
    show_users_page()


def show_users_page():
    frame_show_users.pack()
    c.execute('SELECT * FROM users')
    users = c.fetchall()

    vsb = Scrollbar(frame_show_users)
    vsb.pack(fill=Y, side=RIGHT)
    tree = Treeview(frame_show_users, column=("c1", "c2"), show='headings', yscrollcommand=vsb.set, selectmode="extended")
    vsb.config(command=tree.yview)

    tree.column("#1", anchor=CENTER, width=3)

    tree.heading("#1", text="ID")

    tree.column("#2", anchor=CENTER)

    tree.heading("#2", text="User")

    tree.pack()

    for row in users:
        tree.insert("", END, values=row, tags=('evenrow',))

    #button_back = Button(frame_show_users, text="< Back", font=font, width=8,
    #                     command=lambda: back_to_options(frame_show_users))
    #button_back.grid(column=1, row=2, sticky=W)


def admin_add_questions():
    frame_options.grid_forget()
    show_add_questions_page()


def admin_add_user():
    frame_options.grid_forget()
    show_add_user_page()


def show_add_questions_page():
    frame_add_questions.pack()

    label_question = Label(frame_add_questions, text="Question:", font=font)
    label_question.pack()

    entry = Entry(frame_add_questions, font=font)
    entry.place(heigth=100)

    #button_back = Button(frame_add_questions, text="< Back", font=font, width=8,
    #                     command=lambda: back_to_options(frame_add_questions))
    #button_back.grid(column=1, row=5, sticky=S)


def show_add_user_page():
    frame_add_user.grid()

    label_username = Label(frame_add_user, text="Username:", font=font)
    label_username.grid(column=1, row=1, pady=(40, 10), padx=(40, 0))

    username_add.grid(column=2, row=1, pady=(40, 10), sticky=W)

    label_password = Label(frame_add_user, text="Password:", font=font)
    label_password.grid(column=1, row=2, padx=(40, 0))

    password_add.grid(column=2, row=2, sticky=W)

    user_added_info.grid(column=2, row=3, sticky=W)

    button = Button(frame_add_user, text="Add", font=font, width=10,
                    command=lambda: add_user(username_add.get(), password_add.get()))
    button.grid(column=2, row=4, pady=(10, 25))
    button_back = Button(frame_add_user, text="< Back", font=font, width=8,
                         command=lambda: back_to_options(frame_add_user))
    button_back.grid(column=1, row=5, sticky=S)


def back_to_options(frame):
    frame.grid_forget()
    show_admin_option()


def back_to_login_page(frame):
    frame.grid_forget()
    show_login_page()


def add_user(username, password):
    if username == "" or password == "":
        user_added_info.config(text="Bad username or password.", foreground="red")
    else:
        now = int(time.time())
        passwd = bytes(password, encoding='utf-8')
        salt = bcrypt.gensalt()
        password_db = bcrypt.hashpw(passwd, salt)
        c.execute(f"INSERT INTO users (username, password, salt, created_at) VALUES (?, ?, ?, {now})",
                  (username, password_db, salt))
        con.commit()
        user_added_info.config(text="User added.", foreground="green")
        username_add.delete(0, END)
        password_add.delete(0, END)
        username_add.focus()

# todo: use this on x
# con.close()


window.mainloop()
