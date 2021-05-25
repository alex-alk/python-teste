import time
from tkinter import *
from windowConfig import window

frame_questions = Frame(window, padx=40, pady=40)
print("questions")


def show_add_question_page(frame):
    frame.grid_forget()
    QuestionPage.frame_add_questions.pack(expand=True, fill=BOTH)
    QuestionPage.window.geometry('{}x{}'.format(600, 700))
    QuestionPage.window.resizable(width=True, height=True)


def load_questions_page():
    font = ("Arial", 12)
    label_question = Label(frame_questions, text="Question:", font=font)
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

    entry_correct_answer = Entry(frame_add_questions, font=font)
    entry_correct_answer.pack(anchor=W)

    button_save = Button(frame_add_questions, text="Save", font=font, width=8,
                         command=lambda: self.save_question(entry, entry1, entry2, entry3, entry4,
                                                            entry_correct_answer))
    button_save.pack(pady=(10, 0))

    button_back = Button(frame_add_questions, text="< Back", font=font, width=8,
                         command=lambda: self.back_to_options_pack(frame_add_questions))
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


class QuestionPage:
    frame_add_questions = None
    window = None

    def __init__(self, app_window, app_frame_add_questions):
        super().__init__()
        window = app_window


    def save_question(self, question, answer1, answer2, answer3, answer4, correct_answer):
        if question == "" or answer1 == "" or answer2 == "" or answer3 == "" or answer4 == "" or correct_answer == "":
            # question_info.config(text="Empty fields not allowed.", foreground="red")
            pass
        else:
            now = int(time.time())

            # c.execute(
            # f"INSERT INTO questions (question, answer1, answer2, answer3, answer4, correct_answer, date) VALUES "
            # f"(?,?,?,?,?,?,{now})",
            # (question, answer1, answer2, answer3, answer4, correct_answer))
            # con.commit()
            # question_info.config(text="Question added.", foreground="green")
            # username_add.delete(0, END)
            # password_add.delete(0, END)
            # username_add.focus()
