import login
import questions
import quiz
import users
import options
from windowConfig import window


def init():
    quiz.load_quiz_page()
    users.load_add_user_page()
    users.load_show_users_page()
    questions.load_show_questions_page()
    questions.load_add_questions_page()
    options.load_options_page()
    login.load_login_page()


init()


window.mainloop()
