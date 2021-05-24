from tkinter import *
import sqlite3
import bcrypt as bcrypt

window = Tk()
frame_login = Frame(window)
frame_options = Frame(window)
frame_add_user = Frame(window)

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

    # todo: move these
    frame_login.grid_forget()
    show_admin_option()

    if user:
        user_salt = user[2]
        passwd = bytes(input_password.get(), encoding='utf-8')
        password = bcrypt.hashpw(passwd, user_salt)

        if user[2] == password:
            print("OK")
            frame_login.grid_forget()
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


def show_admin_option():
    frame_options.grid()
    button_add_questions = Button(frame_options, text="Add questions", font=font, width=13, command=admin_add_questions)
    button_add_questions.grid(column=1, row=1, pady=10, padx=20)
    button_add_user = Button(frame_options, text="Add user", font=font, width=13, command=admin_add_user)
    button_add_user.grid(column=2, row=1, pady=10)


def admin_add_questions():
    pass


def admin_add_user():
    frame_options.grid_forget()
    show_add_user_page()


def show_add_user_page():
    frame_add_user.grid()
    username = Entry(frame_add_user, font=font)
    password = Entry(frame_add_user, font=font, show="*")
    error = Label(frame_login, text="", font=font, foreground="red")

    label_username = Label(frame_add_user, text="Username:", font=font)
    label_username.grid(column=1, row=1, pady=(0, 10))

    username.grid(column=2, row=1, pady=(0, 10), sticky=W)

    label_password = Label(frame_add_user, text="Password:", font=font)
    label_password.grid(column=1, row=2)

    password.grid(column=2, row=2, sticky=W)

    error.grid(column=2, row=3, sticky=W)

    button = Button(frame_add_user, text="Add", font=font, width=10, command=add_user)
    button.grid(column=2, row=4, pady=10)


def add_user():
    pass


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
