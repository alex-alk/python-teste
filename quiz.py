import sqlite3
from tkinter import *
from tkinter.ttk import Button
from tkinter.ttk import Radiobutton
from windowConfig import window

frame_quiz = Frame(window, padx=5)
question = Label(frame_quiz, text="")
button_next_question = Button(frame_quiz, text="Next question", command=lambda: show_next_question())

correct_answers = 0

con = sqlite3.connect('teste.db')
c = con.cursor()

c.execute('SELECT * FROM questions limit 10')
questions = c.fetchall()

con.close()

question_nr = 1

selected = IntVar()
answer1_button = Radiobutton(frame_quiz, text=questions[0][2], value=1, variable=selected)
answer2_button = Radiobutton(frame_quiz, text=questions[0][3], value=2, variable=selected)
answer3_button = Radiobutton(frame_quiz, text=questions[0][4], value=3, variable=selected)
answer4_button = Radiobutton(frame_quiz, text=questions[0][5], value=4, variable=selected)
selected.set(1)


def load_quiz_page():
    question.pack(anchor=W)
    button_next_question.pack(anchor=SE)


def show_quiz_page():
    frame_quiz.pack(fill=BOTH)
    window.title(f"Question {question_nr}/{len(questions)}")
    window.resizable(width=False, height=False)
    question.config(text=questions[0][1])
    answer1_button.pack(anchor=W)
    answer2_button.pack(anchor=W)
    answer3_button.pack(anchor=W)
    answer4_button.pack(anchor=W)


def show_next_question():
    global question_nr
    global correct_answers

    if len(questions) >= question_nr + 1:
        window.title(f"Question {question_nr + 1}/{len(questions)}")

        question_nr += 1
        question.config(text=questions[question_nr-1][1])
        answer1_button.config(text=questions[question_nr-1][2])
        answer2_button.config(text=questions[question_nr-1][3])
        answer3_button.config(text=questions[question_nr-1][4])
        answer4_button.config(text=questions[question_nr-1][5])
        selected.set(1)

        if len(questions) == question_nr:
            button_next_question.config(text="Submit score")

        if selected.get() == questions[question_nr-1][6]:
            correct_answers += 1

    elif len(questions) == question_nr:
        print("Submitted")



