import sqlite3
from tkinter import *
from tkinter.ttk import Button
from windowConfig import window

frame_quiz = Frame(window, padx=5)
question = Label(frame_quiz, text="")
button_next_question = Button(frame_quiz, text="Next question", command=lambda: show_next_question())

con = sqlite3.connect('teste.db')
c = con.cursor()

c.execute('SELECT * FROM questions limit 10')
questions = c.fetchall()

con.close()

question_nr = 1


def load_quiz_page():
    question.pack(anchor=W)
    button_next_question.pack(anchor=SE)


def show_quiz_page():
    window.title(f"Question {question_nr}/{len(questions)}")
    frame_quiz.pack(fill=BOTH)
    window.resizable(width=False, height=False)
    question.config(text=questions[0][1])


def show_next_question():
    global question_nr

    question.config(text=questions[question_nr][1])

    if len(questions) < question_nr:
        question_nr += 1
    else:
        button_next_question.config(text="Submit score")

    window.title(f"Question {question_nr + 1}/{len(questions)}")

