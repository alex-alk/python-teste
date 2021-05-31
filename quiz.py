import sqlite3
from tkinter import *
from tkinter.ttk import Button
from tkinter.ttk import Radiobutton

import login
from style import font
from windowConfig import window

frame_quiz = Frame(window, padx=5)
frame_show_score = Frame(window, padx=5)
question = Label(frame_quiz, text="")
button_next_question = Button(frame_quiz, text="Next question", command=lambda: show_next_question())

correct_answers = 0
selected = IntVar()
answer1_button = Radiobutton(frame_quiz, text="", value=1, variable=selected)
answer2_button = Radiobutton(frame_quiz, text="", value=2, variable=selected)
answer3_button = Radiobutton(frame_quiz, text="", value=3, variable=selected)
answer4_button = Radiobutton(frame_quiz, text="", value=4, variable=selected)

label_show_score = Label(frame_show_score, font=font)

question_nr = 1
questions = []

selected.set(1)


def load_quiz_page():
    global questions
    question.pack(anchor=W)
    button_next_question.pack(anchor=SE)
    con = sqlite3.connect('teste.db')
    c = con.cursor()

    c.execute('SELECT * FROM questions limit 10')
    questions = c.fetchall()
    con.close()
    answer1_button.config(text=questions[0][2])
    answer2_button.config(text=questions[0][3])
    answer3_button.config(text=questions[0][4])
    answer4_button.config(text=questions[0][5])


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
        print(selected.get())
        print(questions[question_nr-1][6])
        if selected.get() == questions[question_nr-1][6]:
            correct_answers += 1
            print("correct answer")

    elif len(questions) == question_nr:
        con = sqlite3.connect('teste.db')
        c = con.cursor()

        score = "{:.1f}".format(correct_answers/len(questions))

        c.execute(f"UPDATE users SET score = {score} where id={login.user[0]}")
        con.commit()
        con.close()

        frame_quiz.pack_forget()
        frame_show_score.pack()
        label_show_score.pack()
        label_show_score.config(text=f"Your score is: {score}")



