import time
from tkinter import *

import options
from db import c, con
from style import font
from windowConfig import window

frame_questions = Frame(window, padx=10, pady=5)
label_question_info = Label(frame_questions, text="", font=font)
print("questions")


def show_questions_page(frame):
    frame.grid_forget()
    frame_questions.pack(expand=True, fill=BOTH)
    window.geometry('{}x{}'.format(600, 700))
    window.resizable(width=True, height=True)
    label_question_info.config(text="Question added.", foreground="green")


def load_questions_page():
    font = ("Arial", 12)
    label_question = Label(frame_questions, text="Question:", font=font)
    label_question.pack(anchor=W)

    entry = Text(frame_questions, font=font, height=6)
    entry.pack(expand=True, fill=BOTH)

    label_answer1 = Label(frame_questions, text="Answer 1:", font=font)
    label_answer1.pack(pady=(10, 0), anchor=W)

    entry1 = Text(frame_questions, font=font, height=1)
    entry1.pack(expand=True, fill=BOTH)

    label_answer2 = Label(frame_questions, text="Answer 2:", font=font)
    label_answer2.pack(pady=(10, 0), anchor=W)

    entry2 = Text(frame_questions, font=font, height=1)
    entry2.pack(expand=True, fill=BOTH)

    label_answer3 = Label(frame_questions, text="Answer 3:", font=font)
    label_answer3.pack(pady=(10, 0), anchor=W)

    entry3 = Text(frame_questions, font=font, height=1)
    entry3.pack(expand=True, fill=BOTH)

    label_answer4 = Label(frame_questions, text="Answer 4:", font=font)
    label_answer4.pack(pady=(10, 0), anchor=W)

    entry4 = Text(frame_questions, font=font, height=1)
    entry4.pack(expand=True, fill=BOTH)

    label_correct_answer = Label(frame_questions, text="Correct Answer:", font=font)
    label_correct_answer.pack(pady=(10, 0), anchor=W)

    entry_correct_answer = Entry(frame_questions, font=font)
    entry_correct_answer.pack(anchor=W)


    label_question_info.pack(pady=(10, 0), anchor=W)

    button_save = Button(frame_questions, text="Save", font=font, width=8,
                         command=lambda: save_question(entry, entry1, entry2, entry3, entry4, entry_correct_answer,
                                                       label_question_info))
    button_save.pack(pady=(10, 0))

    button_back = Button(frame_questions, text="< Back", font=font, width=8,
                         command=lambda: options.back_to_options_pack(frame_questions))
    button_back.pack(anchor=W)


class Question:
    def __init__(self, question, answer1, answer2, answer3, answer4, correct_answer):
        self.question = question
        self.answer1 = answer1
        self.answer2 = answer2
        self.answer3 = answer3
        self.answer4 = answer4
        self.correct_answer = correct_answer
        self.date = int(time.time())


def save_question(question, answer1, answer2, answer3, answer4, correct_answer, label):
    if question.get("1.0", "end-1c") == "" or answer1.get("1.0", "end-1c") == "" or answer2.get("1.0", "end-1c") == "" \
            or answer3.get("1.0", "end-1c") == "" or answer4.get("1.0", "end-1c") == "" or correct_answer.get() == "":
        label.config(text="Empty fields not allowed.", foreground="red")
    else:
        print()
        now = int(time.time())

        c.execute(f"INSERT INTO questions (question, answer1, answer2, answer3, answer4, correct_answer, date) VALUES "
                  f"(?,?,?,?,?,?,{now})", (question.get("1.0", "end-1c"), answer1.get("1.0", "end-1c"),
                                           answer2.get("1.0", "end-1c"), answer3.get("1.0", "end-1c"),
                                           answer4.get("1.0", "end-1c"), correct_answer.get()))
        con.commit()
        label.config(text="Question added.", foreground="green")
        question.delete(1.0, END)
        answer1.delete(1.0, END)
        answer2.delete(1.0, END)
        answer3.delete(1.0, END)
        answer4.delete(1.0, END)
        correct_answer.delete(0, END)
        question.focus()
