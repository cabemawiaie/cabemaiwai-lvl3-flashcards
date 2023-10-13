# This will import all the widgets
# and modules which are available in
# tkinter and ttk module
import tkinter as tk
from random import randint
from tkinter import messagebox
from tkinter import ttk


class FlashcardsApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        width = 570
        height = 350

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
            frame.configure(bg='lightblue')
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

        home_label = tk.Label(self, text="Home", bg='lightblue',
                              font=('Helvetic', 30, 'bold'))
        home_label.grid(row=0, column=0, columnspan=4, pady=10)
        wel_msg = ("""Welcome to your language flashcard application"""
                   """\nwhere you can begin to learn French and Spanish!""")
        wel_label = tk.Label(self, text=wel_msg, bg='lightblue',
                             font=('Helvetic', 10, 'bold'))
        wel_label.grid(row=8, column=0, columnspan=4, padx=10, pady=20)

        # Button
        spanish_btn = tk.Button(self, text="Spanish", font=('Helvetica', 15),
                                bg="white", borderwidth=0,
                                command=lambda: controller.show_frame(Spanish))
        french_btn = tk.Button(self, text='French', font=('Helvetica', 15),
                               bg="white", borderwidth=0,
                               command=lambda: controller.show_frame(French))
        french_btn.grid(row=2, column=1, columnspan=2, padx=10, pady=20)
        spanish_btn.grid(row=1, column=1, columnspan=2, padx=10, pady=20)


class French(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.grid_propagate(False)

        self.words = [(('Au Revoir'), ('Goodbye')),
                      (('Bonne nuit'), ('Goodnight')),
                      (('Merci'), ('Thank you')),
                      (('Oui'), ("Yes")),
                      (('Non'), ('No')),
                      (('Bonjour'), ('Hello')),
                      (('Bonsoir'), ('Good evening')),
                      (('Excusez moi'), ('Excuse me'))]

        self.count = len(self.words)
        self.random_word = randint(0, self.count - 1)
        self.hinter = ''
        self.hint_count = 0
        self.answer_count = 0
        self.progress_msg = ''

        self.entry = tk.Entry(self, font=('MS Sans Serif', 14))
        self.entry.grid(row=0, column=3, pady=20, columnspan=2)

        self.label = tk.Label(self, text='Please enter english \n'
                                         'translation here:',
                              font=('MS Sans Serif', 10, 'bold'),
                              bg='lightblue')
        self.question_label = tk.Label(self, text=self.words[self.random_word][0],
                                       font=('MS Sans Serif', 22),
                                       bg='lightblue')
        self.answer_label = tk.Label(self, text="", font=('MS Sans Serif', 15),
                                     bg='lightblue')
        self.progress_label = tk.Label(self, text=self.progress_msg,
                                       font=('MS Sans Serif', 15),
                                       bg='lightblue')
        self.hint_label = tk.Label(self, text="", bg='lightblue',
                                   font=('MS Sans Serif', 15))

        self.progress_label.grid(row=4, column=2, columnspan=2)
        self.label.grid(row=0, column=2, pady=20)
        self.hint_label.grid(row=4, column=1, pady=10, columnspan=2)
        self.question_label.grid(row=2, column=2, columnspan=2, pady=20)
        self.answer_label.grid(row=2, column=3, columnspan=2, pady=20)

        check_button = tk.Button(self, text="Check \n Answer", command=self.check)
        next_button = tk.Button(self, text="Next", command=self.next)
        hint_button = tk.Button(self, text="Hint", command=self.hint)
        home_button = tk.Button(self, text="Home",
                                command=lambda: controller.show_frame(Home))
        skip_button = tk.Button(self, text="Skip", command=self.skip)

        buttons = [check_button, next_button, hint_button, home_button,
                   skip_button]

        for button in buttons:
            button.config(bg='white', borderwidth=2, width=8, height=2,
                          font=('MS Sans Serif', 8))

        next_button.grid(row=5, column=4, padx=5, pady=20)
        hint_button.grid(row=8, column=2, padx=5, pady=10)
        home_button.grid(row=8, column=0, padx=20)
        check_button.grid(row=5, column=2, padx=5, pady=20)
        skip_button.grid(row=8, column=4, padx=5, pady=10)

    '''Shows users how many answers they have gotten correct so far'''
    def progress(self):
        while self.entry.get == self.entry.get().capitalize().strip():
            self.answer_count += 1
            self.progress_msg = (self.progress_msg +
                                 f"You have got {self.answer_count} right so far!")
            self.progress_label.config(text=self.progress_msg,
                                       font=('MS Sans Serif', 10))

    '''Confirms whether user would like to skip flashcard'''
    def skip(self):
        self.entry.delete(0, 'end')
        self.next()

    def next(self):
        if len(self.entry.get()) == 0:
            message_box = messagebox.askyesno('Remember there are hints!',
                                              (f'Are you sure you \n'
                                               'would like to move on?'))
            if message_box:
                self.answer_label.config(text="", font=('MS Sans Serif', 15))
                self.entry.delete(0, 'end')
                self.hint_label.config(text="", font=('MS Sans Serif', 20))

                self.hinter = ""
                self.hint_count = 0

                self.random_word = randint(0, self.count - 1)
                self.question_label.config(text=self.words[self.random_word][0],
                                           font=('MS Sans Serif', 22))
        else:
            self.answer_label.config(text="", font=('MS Sans Serif', 15))
            self.entry.delete(0, 'end')
            self.hint_label.config(text="", font=('MS Sans Serif', 15))

            self.hinter = ""
            self.hint_count = 0

            self.random_word = randint(0, self.count - 1)
            self.question_label.config(text=self.words[self.random_word][0],
                                       font=('MS Sans Serif', 22))
        return self.random_word

    def check_input(self):
        word = self.entry.get()
        # Checks whether user entered an invalid answer with numbers
        for char in word:
            if char.isdigit():
                messagebox.showinfo('Numbers are not an acceptable answer',
                                    'Please enter a valid answer')
            else:
                self.check()

    '''Checks user input and gives feedback accordingly'''

    def check(self):
        answer = self.entry.get().capitalize().strip()
        if len(answer) > 0:
            if answer == self.words[self.random_word][1]:
                self.answer_label.config(
                    text=f"""Correct! {self.words[self.random_word][0]} is
                    {self.words[self.random_word][1]}""",
                    font=('MS Sans Serif', 10))
                return True
            else:
                self.answer_label.config(
                    text=f"""Incorrect, {self.words[self.random_word][0]} is
                                not {answer}""", font=('MS Sans Serif', 10))
                self.entry.delete(0, 'end')
                return False
        else:
            # If user does not enter input, messagebox prompts them to
            messagebox.showinfo('No input entered',
                                'Please give an answer')

    def hint(self):
        if self.hint_count < len(self.words[self.random_word][1]):
            self.hinter = self.hinter + self.words[self.random_word][1][self.hint_count]
            self.hint_label.config(text=f"Hint: {self.hinter}",
                                   font=('MS Sans Serif', 15))
            self.hint_count += 1
            return self.hinter, self.hint_count


class Spanish(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.grid_propagate(False)

        self.words = [(('Buenos dias'), ('Good morning')),
                      (('Buenas noches'), ('Good evening')),
                      (('Gracias'), ('Thank you')),
                      (('De nada'), ("You're welcome")),
                      (('Adios'), ('Goodbye')),
                      (('Hola'), ('Hello')),
                      (('Que tal?'), ('How are you')),
                      (('Me llamo'), ('My name is'))]

        self.count = len(self.words)
        self.random_word = randint(0, self.count - 1)
        self.hinter = ''
        self.hint_count = 0

        self.entry = tk.Entry(self, font=('MS Sans Serif', 18))
        self.entry.grid(row=0, column=2, pady=20, columnspan=2)

        self.label = tk.Label(self, text='Please enter english \n'
                                         'translation here:',
                              font=('MS Sans Serif', 10, 'bold'),
                              bg='lightblue')
        self.question_label = tk.Label(self, text=self.words[self.random_word][0],
                                       font=('MS Sans Serif', 18),
                                       bg='lightblue')
        self.answer_label = tk.Label(self, text="", font=('MS Sans Serif', 15),
                                     bg='lightblue')
        self.hint_label = tk.Label(self, text="", bg='lightblue',
                                   font=('MS Sans Serif', 15))

        self.label.grid(row=0, column=0, pady=20)
        self.hint_label.grid(row=4, column=1, pady=10, columnspan=2)
        self.question_label.grid(row=2, column=1, columnspan=2, pady=20)
        self.answer_label.grid(row=2, column=3, columnspan=3, pady=20)

        answer_button = tk.Button(self, text="Check \n Answer", command=self.answer)
        next_button = tk.Button(self, text="Next", command=self.next)
        hint_button = tk.Button(self, text="Hint", command=self.hint)
        home_button = tk.Button(self, text="Home",
                                command=lambda: controller.show_frame(Home))
        skip_button = tk.Button(self, text="Skip", command=self.skip)

        buttons = [answer_button, next_button, hint_button, home_button,
                   skip_button]

        for button in buttons:
            button.config(bg='white', borderwidth=2, width=8, height=2,
                          font=('MS Sans Serif', 8))

        next_button.grid(row=5, column=4, padx=5, pady=20)
        hint_button.grid(row=8, column=2, padx=5, pady=10)
        home_button.grid(row=8, column=0, padx=20)
        answer_button.grid(row=5, column=2, padx=5, pady=20)
        skip_button.grid(row=8, column=4, padx=5, pady=10)

    def skip(self):
        message_box = messagebox.askyesno('Remember there are hints!',
                                          (f'Are you sure you \n'
                                           'would like to move on?'))
        if message_box:
            self.next()
        else:
            self.entry.delete(0, 'end')

    def next(self):
        if len(self.entry.get()) == 0:
            message_box = messagebox.askyesno('Remember there are hints!',
                                              (f'Are you sure you \n'
                                               'would like to move on?'))
            if message_box:
                self.answer_label.config(text="", font=('MS Sans Serif', 15))
                self.entry.delete(0, 'end')
                self.hint_label.config(text="", font=('MS Sans Serif', 20))

                self.hinter = ""
                self.hint_count = 0

                self.random_word = randint(0, self.count - 1)
                self.question_label.config(text=self.words[self.random_word][0],
                                           font=('MS Sans Serif', 15))
        else:
            self.answer_label.config(text="", font=('MS Sans Serif', 15))
            self.entry.delete(0, 'end')
            self.hint_label.config(text="", font=('MS Sans Serif', 20))

            self.hinter = ""
            self.hint_count = 0

            self.random_word = randint(0, self.count - 1)
            self.question_label.config(text=self.words[self.random_word][0],
                                       font=('MS Sans Serif', 15))
        return self.random_word

    def check_no(self):
        word = self.entry.get()
        # Checks whether user entered an invalid answer with numbers
        for char in word:
            if char.isdigit():
                messagebox.showinfo('Numbers are not an acceptable answer',
                                    'Please enter a valid answer')
            else:
                self.answer()

    '''Checks user input and gives feedback accordingly'''

    def answer(self):
        answer = self.entry.get().capitalize().strip()
        if len(answer) > 0:
            if answer == self.words[self.random_word][1]:
                self.answer_label.config(
                    text=f"""Correct! {self.words[self.random_word][0]} is 
                                     {self.words[self.random_word][1]}""",
                    font=('MS Sans Serif', 10))
            else:
                self.answer_label.config(
                    text=f"""Incorrect, {self.words[self.random_word][0]} is
                              not {answer}""", font=('MS Sans Serif', 10))
                self.entry.delete(0, 'end')
        else:
            # If user does not enter input, messagebox prompts them to
            messagebox.showinfo('No input entered',
                                'Please give an answer')

    def hint(self):
        if self.hint_count < len(self.words[self.random_word][1]):
            self.hinter = self.hinter + self.words[self.random_word][1][self.hint_count]
            self.hint_label.config(text=f"Hint: {self.hinter}",
                                   font=('MS Sans Serif', 10))
            self.hint_count += 1
            return self.hinter, self.hint_count


if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
