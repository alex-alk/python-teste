import sqlite3
from tkinter import *
import bcrypt
import options
import quiz
from style import font
from windowConfig import window
from tkinter.ttk import Button
from tkinter.ttk import Style
from tkinter.ttk import Entry

s = Style()
s.configure("TButton", font=('Arial', 12))
s.configure("TRadiobutton", font=('Arial', 12))

frame_login = Frame(window, padx=40, pady=40)

user = []


def show_login_page(frame):
    frame.grid_forget()
    frame_login.grid()


def load_login_page():
    label_username = Label(frame_login, text="Username:", font=font)
    input_username = Entry(frame_login, font=font)
    input_password = Entry(frame_login, show="*", font=font)
    label_error = Label(frame_login, text="", font=font, foreground="red")
    label_password = Label(frame_login, text="Password:", font=font)
    button_login = Button(frame_login, text="Login", width=10,
                          command=lambda: check_credentials(input_username.get(), input_password, label_error))
    button_login.bind('<Return>', lambda _: check_credentials(input_username.get(), input_password, label_error))

    label_username.grid(column=1, row=1, pady=(0, 10))
    input_username.grid(column=2, row=1, pady=(0, 10), sticky=W)
    label_password.grid(column=1, row=2)
    input_password.grid(column=2, row=2, sticky=W)
    input_password.bind('<Return>', lambda _: check_credentials(input_username.get(), input_password, label_error))

    label_error.grid(column=2, row=3, sticky=W)
    button_login.grid(column=2, row=4, pady=10, sticky=W)
    frame_login.grid()


def check_credentials(username, password, label_error):
    global user
    con = sqlite3.connect('teste.db')
    c = con.cursor()
    c.execute('SELECT * FROM users WHERE username=?', (username,))
    user = c.fetchone()
    con.close()

    if user:
        user_salt = user[2]
        passwd = bytes(password.get(), encoding='utf-8')
        password_encrypted = bcrypt.hashpw(passwd, user_salt)

        if user[2] == password_encrypted:  # if logged in
            frame_login.grid_forget()
            if user[1] == 'admin':
                options.show_options_page()
            else:
                quiz.show_quiz_page()
        else:
            label_error.config(text="Wrong username/password.")
    else:
        label_error.config(text="User not found.")