
from db import c
import login
import options
import questions
from questions import *

import bcrypt as bcrypt

from style import font


# username_add = Entry(frame_add_user, font=font)
# password_add = Entry(frame_add_user, font=font, show="*")
# user_added_info = Label(frame_add_user, text="", font=font, foreground="red")
from windowConfig import window


def admin_show_questions():
    pass


def admin_show_users():
    #frame_options.grid_forget()
    show_users_page()


def show_users_page():
    #frame_show_users.pack()
    c.execute('SELECT * FROM users')
    users = c.fetchall()

    # vsb = Scrollbar(frame_show_users)
    # vsb.pack(fill=Y, side=RIGHT)
    # tree = Treeview(frame_show_users, column=("c1", "c2"), show='headings', yscrollcommand=vsb.set, selectmode="extended")
    # vsb.config(command=tree.yview)
    #
    # tree.column("#1", anchor=CENTER, width=3)
    #
    # tree.heading("#1", text="ID")
    #
    # tree.column("#2", anchor=CENTER)
    #
    # tree.heading("#2", text="User")
    #
    # tree.pack()
    #
    # for row in users:
    #     tree.insert("", END, values=row, tags=('evenrow',))

    #button_back = Button(frame_show_users, text="< Back", font=font, width=8,
    #                     command=lambda: back_to_options(frame_show_users))
    #button_back.grid(column=1, row=2, sticky=W)


def admin_add_questions():
    #frame_options.grid_forget()
    show_add_questions_page()


def admin_add_user():
    #frame_options.grid_forget()
    show_add_user_page()


#question = QuestionPage(frame_add_questions)

def init_question_page():
    pass


def init_login_page():
    pass


def init_options_page():
    pass


def init():
    questions.load_questions_page()
    options.load_options_page()
    login.load_login_page()


init()


def show_add_questions_page():
    pass


def show_add_user_page():
    # frame_add_user.grid()
    #
    # label_username = Label(frame_add_user, text="Username:", font=font)
    # label_username.grid(column=1, row=1, pady=(40, 10), padx=(40, 0))
    #
    # username_add.grid(column=2, row=1, pady=(40, 10), sticky=W)
    #
    # label_password = Label(frame_add_user, text="Password:", font=font)
    # label_password.grid(column=1, row=2, padx=(40, 0))
    #
    # password_add.grid(column=2, row=2, sticky=W)
    #
    # user_added_info.grid(column=2, row=3, sticky=W)
    #
    # button = Button(frame_add_user, text="Add", font=font, width=10,
    #                 command=lambda: add_user(username_add.get(), password_add.get()))
    # button.grid(column=2, row=4, pady=(10, 25))
    # button_back = Button(frame_add_user, text="< Back", font=font, width=8,
    #                      command=lambda: back_to_options(frame_add_user))
    # button_back.grid(column=1, row=5, sticky=S)
    pass


def back_to_options(frame):
    frame.grid_forget()
    #show_admin_option()


def back_to_login_page(frame):
    frame.grid_forget()


def add_user(username, password):
    if username == "" or password == "":
        # user_added_info.config(text="Bad username or password.", foreground="red")
        pass
    else:
        now = int(time.time())
        passwd = bytes(password, encoding='utf-8')
        salt = bcrypt.gensalt()
        password_db = bcrypt.hashpw(passwd, salt)
        c.execute(f"INSERT INTO users (username, password, salt, created_at) VALUES (?, ?, ?, {now})",
                  (username, password_db, salt))
        # con.commit()
        # user_added_info.config(text="User added.", foreground="green")
        # username_add.delete(0, END)
        # password_add.delete(0, END)
        # username_add.focus()

# todo: use this on x
# con.close()


window.mainloop()
