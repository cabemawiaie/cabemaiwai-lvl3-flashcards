import tkinter as tk
from tkinter import ttk


class SignUpWindow(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config(width=350, height=450)
        self.title("Welcome to My Flashcards / Sign up Form")

        self.sign_in_button = ttk.Button(self, text="Sign In",
                                         command=self.open_sign_in)
        self.sign_in_button.place(x=175, y=225)

    def open_sign_in(self):
        self.sign_in_window = SignInWindow()


class SignInWindow(tk.Toplevel):

    def _init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry('350x450')
        self.title("Flashcard Sign In Form")

        self.home_button = ttk.Button(self, text="Home", command=self.destroy)
        self.home_button.place(x=0, y=400)
        self.focus()
        self.grab_set()


if __name__ == "__main__":
    main = SignUpWindow()
    main.mainloop()
