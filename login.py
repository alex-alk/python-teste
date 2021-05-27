from tkinter import *
import bcrypt
from db import c
import options
from style import font
from windowConfig import window


frame_login = Frame(window, padx=40, pady=40)


def show_login_page(frame):
    frame.grid_forget()
    frame_login.grid()


def load_login_page():
    label_username = Label(frame_login, text="Username:", font=font)
    input_username = Entry(frame_login, font=font)
    input_password = Entry(frame_login, font=font, show="*")
    label_error = Label(frame_login, text="", font=font, foreground="red")
    label_password = Label(frame_login, text="Password:", font=font)
    button_login = Button(frame_login, text="Login", font=font, width=10,
                          command=lambda: check_credentials(input_username.get(), input_password.get(), label_error))

    label_username.grid(column=1, row=1, pady=(0, 10))
    input_username.grid(column=2, row=1, pady=(0, 10), sticky=W)
    label_password.grid(column=1, row=2)
    input_password.grid(column=2, row=2, sticky=W)
    label_error.grid(column=2, row=3, sticky=W)
    button_login.grid(column=2, row=4, pady=10, sticky=W)
    frame_login.grid()


def check_credentials(username, password, label_error):
    c.execute('SELECT * FROM users WHERE username=?', (username,))
    user = c.fetchone()
    frame_login.grid_forget()
    options.show_options_page()

    if user:
        user_salt = user[2]
        passwd = bytes(password, encoding='utf-8')
        password = bcrypt.hashpw(passwd, user_salt)

        if user[2] == password:
            frame_login.grid_forget()
            options.show_options_page()
        else:
            label_error.config(text="Wrong username/password.")
    else:
        label_error.config(text="User not found.")