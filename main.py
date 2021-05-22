from tkinter import *

window = Tk()
window.title("Login")
window.minsize(width=370, height=200)
window.resizable(width=False, height=False)
window.config(padx=50, pady=50)

font = ("Arial", 12)


def login_page():
    label_username = Label(text="Username:", font=font)
    label_username.grid(column=1, row=1, pady=(0, 10))

    input_username = Entry(font=font)
    input_username.grid(column=2, row=1, pady=(0, 10))

    label_password = Label(text="Password:", font=font)
    label_password.grid(column=1, row=2)

    input_password = Entry(font=font, show="*")
    input_password.grid(column=2, row=2)

    button_login = Button(text="Login", font=font, width=10)
    button_login.grid(column=2, row=3, pady=20)


login_page()

window.mainloop()
