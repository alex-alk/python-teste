import login
import questions
import users
from questions import *
import bcrypt as bcrypt
from windowConfig import window


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


def init():
    users.load_add_user_page()
    users.load_show_users_page()
    questions.load_show_questions_page()
    questions.load_add_questions_page()
    options.load_options_page()
    login.load_login_page()


init()


# todo: use this on x
# con.close()


window.mainloop()
