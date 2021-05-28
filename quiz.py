from tkinter import *
from windowConfig import window

frame_quiz = Frame(window, padx=5)


def load_quiz_page():
    question = Label(frame_quiz, text="awdawda")
    question.grid(row=1, column=1)
    pass


def show_quiz_page():
    window.title("Question")
    frame_quiz.grid()
    window.resizable(width=False, height=False)
