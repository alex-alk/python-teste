from tkinter import *
import login
import questions
from style import font
from windowConfig import window

frame_options = Frame(window, padx=5)
print("options")

def load_options_page():

    button_questions = Button(frame_options, text="Manage questions", font=font, width=16,
                              command=lambda: questions.show_questions_page(frame_options))
    button_questions.grid(column=1, row=1, pady=(55, 70), padx=(35, 10))
    button_users = Button(frame_options, text="Manage users", font=font, width=16,
                          command=lambda: login.show_login_page(frame_options))
    button_users.grid(column=2, row=1, pady=(55, 70))

    button_back = Button(frame_options, text="< Back", font=font, width=8,
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
