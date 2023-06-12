import tkinter as tk
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

        for F in (SignIn, SignUpForm, LoginForm):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(SignIn)

    #  Show window for the given page name
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class SignIn(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        sign_up_label = ttk.Label(self, text="Sign In Page")
        sign_up_label.pack(padx=10, pady=10)

        # Buttons
        btn_goals = tk.Button(self, text="Goals", bg='white', width=10, height=2, font=('MS Sans Serif', 8),
                              command=lambda: controller.show_frame(SignUpForm))
        btn_to_do = tk.Button(self, text="To Do List", bg='white', width=10, height=2, font=('MS Sans Serif', 8),
                              command=lambda: controller.show_frame(LoginForm))
        btn_to_do.pack(padx=5, pady=10)
        btn_goals.pack(padx=5, pady=10)


class SignUpForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


class LoginForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
