# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter as tk
import tkinter.font as font
from random import randint
from tkinter import messagebox
from tkinter import ttk


class FlashcardsApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        width = 350
        height = 500

        self.minsize(width, height)
        self.title('Flashcard Application')

        # creating container
        container = ttk.Frame(self, width=500, height=500)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, Spanish, French):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(Home)

    #  Show window for the given page name
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.style = ttk.Style(self)
        self_font = font.Font(family='Helvetica', size=2, weight='bold')
        self.style.configure('TButton', font=self_font)
        self.style.configure('TLabel', font=self_font)

        home_label = ttk.Label(self, text="Home", style='TLabel')
        home_label.grid(row=0, column=2, padx=20, pady=10)

        # Button
        spanish_btn = ttk.Button(self, text="Spanish",
                                 style='TButton',
                                 command=lambda: controller.show_frame(Spanish))
        french_btn = ttk.Button(self, text='France', style='TButton',
                                command=lambda: controller.show_frame(French))
        french_btn.grid(row=1, column=2, padx=10, pady=10)
        spanish_btn.grid(row=2, column=2, padx=10, pady=10)


class French(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.style = ttk.Style(self)

        self.style.configure('TButton', font=('Helvetica', 15))
        self.style.configure('TLabel', font=('Helvetica', 30))
        self.style.configure('Hint.TLabel', font=('Helvetica', 30))
        self.style.map('TButton', foreground=[('pressed', 'blue'), ('active', 'black')])

        self.entry = ttk.Entry(self)
        self.entry.grid(row=10, column=1, pady=20)

        # Labels
        self.question_label = ttk.Label(self, text='', style='TLabel')
        self.question_label.grid(row=1, column=1, pady=50)

        self.answer_label = ttk.Label(self, text="", style='TLabel')
        self.answer_label.grid(row=1, column=1, pady=20)

        self.hint_label = ttk.Label(self, text="", style='Hint.TLabel')
        self.hint_label.grid(row=20, column=1, pady=20)

        # Buttons
        answer_button = ttk.Button(self, text="Answer", command=self.answer, style='TButton')
        answer_button.grid(row=15, column=0, padx=20)

        next_button = ttk.Button(self, text="Next", command=self.next, style='TButton')
        next_button.grid(row=15, column=1, padx=20)

        hint_button = ttk.Button(self, text="Hint", command=self.hint, style='TButton')
        hint_button.grid(row=15, column=2)

        back_button = ttk.Button(self, text="Back",
                                 command=lambda: controller.show_frame(Home),
                                 style='TButton')
        back_button.grid(row=20, column=0)

        self.words = [(('Au Revoir'), ('Goodbye')),
                      (('Bonne nuit'), ('Goodnight')),
                      (('Merci'), ('Thank you')),
                      (('Oui'), ("Yes")),
                      (('Non'), ('No')),
                      (('Bonjour'), ('Hello')),
                      (('Bonsoir'), ('Good evening')),
                      (('Excusez moi'), ('Excuse me'))]

        self.count = len(self.words)

    # Displays a random word from the word list to user when next is clicked
    def next(self):
        global hinter, hint_count
        self.answer_label.config(text="")
        self.entry.delete(0, 'end')
        self.hint_label.config(text="")

        hinter = ""
        hint_count = 0

        global random_word
        random_word = randint(0, self.count - 1)
        self.question_label.config(text=self.words[random_word][0])

    # Depending on the user input, a specific message will be shown
    def answer(self):
        if self.entry.get().capitalize().strip() == self.words[random_word][1]:
            self.answer_label.config(
                text=f"Correct {self.words[random_word][0]} is {self.words[random_word][1]}",
                style='TLabel')
        elif self.entry.get().capitalize() == "":
            messagebox.showinfo('No input entered', 'Please give an answer')
        else:
            self.entry.get().capitalize().strip() != self.words[random_word][1]
            self.answer_label.config(
                text=f"Incorrect! {self.words[random_word][0]} is not {self.entry.get().capitalize()}",
                style='TLabel')
            message_box = messagebox.askyesno('Try again or Skip for now',
                                              f'Would you like to try again?')
            self.entry.delete(0, 'end')

            if message_box:
                message_box.destroy()
            else:
                self.next()

    hinter = ""
    hint_count = 0

    def hint(self):
        global hint_count
        global hinter
        #
        if hint_count < len(self.words[random_word][1]):
            hinter = hinter + self.words[random_word][1][hint_count]
            self.hint_label.config(text=hinter)
            hint_count += 1


class Spanish(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.style = ttk.Style(self)

        self.style.configure('TButton', font=('Helvetica', 15))
        self.style.configure('TLabel', font=('Helvetica', 30))
        self.style.configure('Hint.TLabel', font=('Helvetica', 30))
        self.style.map('TButton', foreground=[('pressed', 'red'), ('active', 'black')])

        self.entry = ttk.Entry(self)
        self.entry.grid(row=10, column=1, pady=20)

        # Labels
        self.question_label = ttk.Label(self, text='', style='TLabel')
        self.question_label.grid(row=1, column=1, pady=50)

        self.answer_label = ttk.Label(self, text="", style='TLabel')
        self.answer_label.grid(row=1, column=1, pady=20)

        self.hint_label = ttk.Label(self, text="", style='Hint.TLabel')
        self.hint_label.grid(row=20, column=1, pady=20)

        # Buttons
        answer_button = ttk.Button(self, text="Answer", command=self.answer, style='TButton')
        answer_button.grid(row=15, column=0, padx=20)

        next_button = ttk.Button(self, text="Next", command=self.next, style='TButton')
        next_button.grid(row=15, column=1, padx=20)

        hint_button = ttk.Button(self, text="Hint", command=self.hint, style='TButton')
        hint_button.grid(row=15, column=2)

        back_button = ttk.Button(self, text="Back",
                                 command=lambda: controller.show_frame(Home),
                                 style='TButton')
        back_button.grid(row=20, column=0)

        self.words = [(('Buenos dias'), ('Good morning')),
                      (('Buenas noches'), ('Good evening')),
                      (('Gracias'), ('Thank you')),
                      (('De nada'), ("You're welcome")),
                      (('Adios'), ('Goodbye')),
                      (('Hola'), ('Hello')),
                      (('Que tal?'), ('How are you')),
                      (('Me llamo'), ('My name is'))]

        self.count = len(self.words)

    def next(self):
        global hinter, hint_count
        self.answer_label.config(text="", style='TLabel')
        self.entry.delete(0, 'end')
        self.hint_label.config(text="", style='TLabel')

        hinter = ""
        hint_count = 0

        global random_word
        random_word = randint(0, self.count - 1)

        self.question_label.config(text=self.words[random_word][0], style='TLabel')

    def answer(self):
        if self.entry.get().capitalize().strip() == self.words[random_word][1]:
            self.answer_label.config(
                text=f"Correct {self.words[random_word][0]} is {self.words[random_word][1]}",
                style='TLabel')
        elif self.entry.get().capitalize() == "":
            messagebox.showinfo('No input entered', 'Please give an answer')
        else:
            self.entry.get().capitalize().strip() != self.words[random_word][1]
            self.answer_label.config(
                text=f"Incorrect! {self.words[random_word][0]} is not {self.entry.get().capitalize()}",
                style='TLabel')
            message_box = messagebox.askyesno('Try again or Skip for now',
                                              f'Would you like to try again?')
            self.entry.delete(0, 'end')

            if message_box:
                message_box.destroy()
            else:
                self.next()

    hinter = ""
    hint_count = 0

    def hint(self):
        global hint_count
        global hinter

        if hint_count < len(self.words[random_word][1]):
            hinter = hinter + self.words[random_word][1][hint_count]
            self.hint_label.config(text=hinter, style='Hint.TLabel')
            hint_count += 1

if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
