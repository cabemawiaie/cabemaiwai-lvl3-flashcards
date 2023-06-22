import tkinter as tk
from tkinter import *
from tkinter import ttk


class FlashcardsApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        width = 350
        height = 500

        self.minsize(width, height)
        self.title('Flashcards')

        # creating container
        container = tk.Frame(self, width=350, height=500)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, Flashcards, CreateSubject):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(SignIn)

    #  Show window for the given page name
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        home_label = ttk.Label(self, text="Home")
        home_label.grid(row=0, column=0, pady=10)
        # Buttons
        sign_in_btn = tk.Button(self, text="Sign Up", bg='white', width=10,
                                height=2, font=('MS Sans Serif', 8),
                                command=lambda: controller.show_frame(SignUpForm))
        login_btn = tk.Button(self, text="Login", bg='white', width=10, height=2, font=('MS Sans Serif', 8),
                              command=lambda: controller.show_frame(LoginForm))
        sign_in_btn.pack(padx=5, pady=10)
        login_btn.pack(padx=5, pady=10)


class Flashcards(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # labels
        sign_up_label = ttk.Label(self, text="Sign Up Form")
        sign_up_label.pack(padx=10, pady=10)

        email_label = ttk.Label(self, text='Enter Email:')
        email_label.pack(padx=10, pady=10)

        password_label = ttk.Label(self, text='Enter Password:')
        password_label.pack(padx=10, pady=10)

        confirm_label = ttk.Label(self, text='Confirm Password:')
        confirm_label.pack(padx=10, pady=10)

        # entry boxes
        confirm_entry = tk.Entry(self)
        confirm_entry.pack(padx=10, pady=10)

        email_entry = tk.Entry(self)
        email_entry.pack(padx=10, pady=10)

        password_entry = tk.Entry(self)
        password_entry.pack(padx=10, pady=10)

        submit_btn = tk.Button(self, text='Submit', width=15, command=None)
        submit_btn.pack(padx=10, pady=10)

        # Functions


class CreateSubject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels
        login_label = ttk.Label(self, text="Login Form")
        login_label.grid(row=0, column=0, pady=10)

        email_label = ttk.Label(self, text='Enter Email:')
        email_label.grid(row=1, column=0, pady=10)

        password_label = ttk.Label(self, text='Enter Password:')
        password_label.grid(row=2, column=0, pady=10)

        login_btn = tk.Button(self, text='login', width=15, command=None)
        login_btn.grid(row=2, column=1, pady=10, padx=20)

        # entry boxes
        email_entry = tk.Entry(self)
        email_entry.grid(row=0, column=1, pady=10, padx=20)

        password_entry = tk.Entry(self)
        password_entry.grid(row=1, column=1, pady=10, padx=20)


if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
