import sqlite3
import time
from tkinter import *
from tkinter.ttk import Treeview
from tkinter.ttk import Button
from tkinter.ttk import Combobox

import options
from style import font
from windowConfig import window

frame_add_questions = Frame(window, padx=10, pady=5)
frame_show_questions = Frame(window, padx=10, pady=5)
frame_table = Frame(frame_show_questions)
frame_under_table = Frame(frame_show_questions)
label_question_info = Label(frame_add_questions, text="", font=font)
vsb = Scrollbar(frame_table)
tree = Treeview(frame_table, column=("c1", "c2", "c3"), show='headings', yscrollcommand=vsb.set)
answers = {"Answer 1": 1, "Answer 2": 2, "Answer 3": 3, "Answer 4": 4}


def show_add_questions_page(frame):
    frame.grid_forget()
    frame_add_questions.pack(expand=True, fill=BOTH)
    window.geometry('{}x{}'.format(600, 700))
    window.resizable(width=True, height=True)
    label_question_info.config(text="", foreground="green")


def show_questions_page(frame):
    frame.grid_forget()
    frame_show_questions.pack(expand=True, fill=BOTH, anchor=N)
    frame_table.pack(expand=True, fill=BOTH)
    frame_under_table.pack(fill=X)
    window.geometry('{}x{}'.format(800, 700))
    window.resizable(width=True, height=True)

    con = sqlite3.connect('teste.db')
    c = con.cursor()

    c.execute('SELECT * FROM questions')

    questions = c.fetchall()
    for i in tree.get_children():
        tree.delete(i)
    for row in questions:
        q = row[1].partition("\n")[0]
        if "\n" in row[1]:
            q += " ..."
        row = [row[0], q, row[6]]
        tree.insert("", END, values=row, tags=('evenrow',))

    con.close()


def load_show_questions_page():
    vsb.pack(fill=Y, side=RIGHT)
    vsb.config(command=tree.yview)
    tree.column("#1", anchor=CENTER, width=40, stretch=NO)
    tree.heading("#1", text="ID")
    tree.column("#2", anchor=W)
    tree.heading("#2", text="Question")
    tree.column("#3", anchor=CENTER, width=80, stretch=NO)
    tree.heading("#3", text="Answer")
    tree.pack(expand=True, fill=BOTH)

    button_remove = Button(frame_under_table, text="Remove selected",
                           command=lambda: remove_question())
    button_remove.pack(pady=(5, 10), anchor=W)

    button_back = Button(frame_under_table, text="< Back", width=8,
                         command=lambda: options.back_to_options_pack(frame_show_questions))
    button_back.pack(pady=10)


def load_add_questions_page():
    label_question = Label(frame_add_questions, text="Question:", font=font)
    label_question.pack(anchor=W)

    entry = Text(frame_add_questions, font=font, height=6)
    entry.pack(expand=True, fill=BOTH)

    label_answer1 = Label(frame_add_questions, text="Answer 1:", font=font)
    label_answer1.pack(pady=(10, 0), anchor=W)

    entry1 = Text(frame_add_questions, font=font, height=1)
    entry1.pack(expand=True, fill=BOTH)

    label_answer2 = Label(frame_add_questions, text="Answer 2:", font=font)
    label_answer2.pack(pady=(10, 0), anchor=W)

    entry2 = Text(frame_add_questions, font=font, height=1)
    entry2.pack(expand=True, fill=BOTH)

    label_answer3 = Label(frame_add_questions, text="Answer 3:", font=font)
    label_answer3.pack(pady=(10, 0), anchor=W)

    entry3 = Text(frame_add_questions, font=font, height=1)
    entry3.pack(expand=True, fill=BOTH)

    label_answer4 = Label(frame_add_questions, text="Answer 4:", font=font)
    label_answer4.pack(pady=(10, 0), anchor=W)

    entry4 = Text(frame_add_questions, font=font, height=1)
    entry4.pack(expand=True, fill=BOTH)

    label_correct_answer = Label(frame_add_questions, text="Correct Answer:", font=font)
    label_correct_answer.pack(pady=(10, 0), anchor=W)

    variable = StringVar(frame_add_questions)

    select = Combobox(frame_add_questions, textvariable=variable, font=font, width=10,
                      values=("Answer 1", "Answer 2", "Answer 3", "Answer 4"))
    select.set("Answer 1")
    select.pack(anchor=W)

    label_question_info.pack(pady=(10, 0), anchor=W)

    button_save = Button(frame_add_questions, text="Save", width=8,
                         command=lambda: save_question(entry, entry1, entry2, entry3, entry4, variable,
                                                       label_question_info))
    button_save.pack(pady=(10, 0))

    button_back = Button(frame_add_questions, text="< Back", width=8,
                         command=lambda: options.back_to_options_pack(frame_add_questions))
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
            or answer3.get("1.0", "end-1c") == "" or answer4.get("1.0", "end-1c") == "":
        label.config(text="Empty fields not allowed.", foreground="red")
    else:
        now = int(time.time())
        con = sqlite3.connect('teste.db')
        c = con.cursor()

        c.execute(f"INSERT INTO questions (question, answer1, answer2, answer3, answer4, correct_answer, date) VALUES "
                  f"(?,?,?,?,?,?,{now})", (question.get("1.0", "end-1c"), answer1.get("1.0", "end-1c"),
                                           answer2.get("1.0", "end-1c"), answer3.get("1.0", "end-1c"),
                                           answer4.get("1.0", "end-1c"), answers.get(correct_answer.get())))
        con.commit()
        con.close()
        label.config(text="Question added.", foreground="green")
        question.delete(1.0, END)
        answer1.delete(1.0, END)
        answer2.delete(1.0, END)
        answer3.delete(1.0, END)
        answer4.delete(1.0, END)
        correct_answer.delete(0, END)
        question.focus()


def remove_question():
    x = tree.selection()[0]

    selected = tree.focus()
    question = tree.item(selected, "values")

    con = sqlite3.connect('teste.db')
    c = con.cursor()

    c.execute(f"DELETE FROM questions WHERE id=" + question[0])
    con.commit()
    tree.delete(x)

    con.close()

