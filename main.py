import time
from tkinter import *
import sqlite3

import bcrypt as bcrypt

window = Tk()
frame_login = Frame(window)
frame_login.grid()
window.title("Login")
window.minsize(width=400, height=200)
window.resizable(width=False, height=False)
window.config(padx=50, pady=50)

font = ("Arial", 12)

input_username = Entry(frame_login, font=font)
input_password = Entry(frame_login, font=font, show="*")
label_error = Label(frame_login, text="", font=font, foreground="red")


def check_credentials():
    con = sqlite3.connect('teste.db')
    c = con.cursor()

    c.execute('SELECT * FROM users WHERE username=?', (input_username.get(),))
    user = c.fetchone()

    if user:
        user_salt = user[2]
        passwd = bytes(input_password.get(), encoding='utf-8')
        password = bcrypt.hashpw(passwd, user_salt)

        if user[2] == password:
            print("OK")
        else:
            label_error.config(text="Wrong username/password.")
    else:
        label_error.config(text="User not found.")

    con.close()


def show_login_page():
    label_username = Label(frame_login, text="Username:", font=font)
    label_username.grid(column=1, row=1, pady=(0, 10))

    input_username.grid(column=2, row=1, pady=(0, 10), sticky=W)

    label_password = Label(frame_login, text="Password:", font=font)
    label_password.grid(column=1, row=2)

    input_password.grid(column=2, row=2, sticky=W)

    label_error.grid(column=2, row=3, sticky=W)

    button_login = Button(frame_login, text="Login", font=font, width=10, command=check_credentials)
    button_login.grid(column=2, row=4, pady=10)


show_login_page()


# c.execute('''CREATE TABLE IF NOT EXISTS users
#              (id INTEGER PRIMARY KEY, username TEXT, password TEXT, salt TEXT, created_at INTEGER)''')

#now = int(time.time())

#passwd = b"admin"

#salt = bcrypt.gensalt()
#password = bcrypt.hashpw(passwd, salt)

#c.execute(f"INSERT INTO users (username, password, salt, created_at) VALUES ('admin', ?, ?, {now})", (password, salt))


#con.commit()
#con.close()
window.mainloop()
