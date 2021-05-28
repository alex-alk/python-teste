from tkinter import *
import login
import questions
import users
from windowConfig import window
from tkinter.ttk import Button

frame_options = Frame(window, padx=5)


def load_options_page():

    button_questions = Button(frame_options, text="Add a question", width=16,
                              command=lambda: questions.show_add_questions_page(frame_options))
    button_questions.grid(column=1, row=1, pady=(45, 0), padx=(35, 10))
    button_show_users = Button(frame_options, text="Show users", width=16,
                               command=lambda: users.show_users_page(frame_options))
    button_show_users.grid(column=2, row=1, pady=(45, 0))
    button_questions = Button(frame_options, text="Show questions", width=16,
                              command=lambda: questions.show_questions_page(frame_options))
    button_questions.grid(column=1, row=2, pady=(5, 40), padx=(35, 10))
    button_add_users = Button(frame_options, text="Add users", width=16,
                              command=lambda: users.show_add_user_page(frame_options))
    button_add_users.grid(column=2, row=2, pady=(5, 40))

    button_back = Button(frame_options, text="< Back", width=8,
                         command=lambda: login.show_login_page(frame_options))
    button_back.grid(column=1, row=3, sticky=W+S)


def show_options_page():
    window.title("Dashboard")
    frame_options.grid()
    window.geometry('{}x{}'.format(400, 200))
    window.resizable(width=False, height=False)


def back_to_options(frame):
    frame.grid_forget()
    show_options_page()


def back_to_options_pack(frame):
    frame.pack_forget()
    show_options_page()
