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
                                     font=('Helvetic',30, 'bold'))
        home_label.grid(row=0, column=8, pady=10)

        # Button
        spanish_btn = tk.Button(self, text="Spanish", font=('Helvetica', 15), 
                                 bg="white",
                                command=lambda: controller.show_frame(Spanish))
        french_btn = tk.Button(self, text='France', font=('Helvetica', 15), 
                                bg="white",
                              command=lambda: controller.show_frame(French))
        french_btn.grid(row=2, column=0)
        french_btn.grid_rowconfigure(1, weight=1)
        french_btn.grid_columnconfigure(1, weight=1)
        spanish_btn.grid(row=4, column=8, pady=10)
       

class French(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.entry = ttk.Entry(self)
        self.entry.grid(row=10, column=1, pady=20)

        self.question_label = ttk.Label(self, text="", style='TLabel')
        self.question_label.grid(row=1, column=1, pady=50)

        self.answer_label = ttk.Label(self, text="", style='TLabel')
        self.answer_label.grid(row=1, column=1, pady=20)
      
        answer_button = ttk.Button(self, text="Answer", command=self.answer, 
                                   style='TButton')
        answer_button.grid(row=15, column=0, padx=20)

        next_button = ttk.Button(self, text="Next", command=self.next, 
                                 style='TButton')
        next_button.grid(row=15, column=1, padx=20)
        
        hint_button = ttk.Button(self, text="Hint", command=self.hint,
                                  style='TButton')
        hint_button.grid(row=15, column=2)

        home_button = ttk.Button(self, text="Home",
                                 command=lambda: controller.show_frame(Home),
                                 style='TButton')
        home_button.grid(row=20, column=0)

        
        self.style = ttk.Style(master=self.parent)
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.map('TButton', bg='lightblue')
        self.style.configure('TLabel', font=('Helvetica', 30))
        self.style.configure('Hint.TLabel', font=('Helvetica', 15))
    
        self.hint_label = ttk.Label(self, text="", style='Hint.TLabel')
        self.hint_label.grid(row=20, column=1, pady=20)
        
        self.words = [(('Au Revoir'), ('Goodbye')),
                (('Bonne nuit'), ('Goodnight')),
                (('Merci'), ('Thank you')),
                (('Oui'), ("Yes")),
                (('Non'), ('No')),
                (('Bonjour'), ('Hello')),
                (('Bonsoir'), ('Good evening')),
                (('Excusez moi'), ('Excuse me'))]
        
        self.count = len(self.words)
    
    hinter = ""
    hint_count = 0

    def next(self):
            self.answer_label.config(text="")
            self.entry.delete(0, 'end')
            self.hint_label.config(text="")
            random_word = randint(0, self.count-1)   
            self.question_label.config(text=self.words[random_word][0]) 
            return random_word  
    
    def check(self):  
        answer = self.entry.get().capitalize().strip()
        # Checks whether user enter an invalid answer such as numbers
        if answer == int(answer):
            messagebox.showinfo('Please enter a valid answer', 
                                     'Numbers are not an acceptable answer')
        else:
            # If user does not enter input, messagebox prompts them to 
            if answer == "":
                messagebox.showinfo('No input entered', 
                                        'Please give an answer')
        return answer
    
    ''' Checks user input and gives feedback accordingly '''
    def answer(self, answer, random_word):
            while answer > 0:
                self.check()
                if answer == self.words[random_word][1]:
                    self.answer_label.config(
                        text=f"""Correct {self.words[random_word][0]} is""" 
                        """{self.words[random_word][1]}""", style='TLabel')
                else:
                    answer != self.words[random_word][1]
                    self.answer_label.config(
                        text=f"Incorrect! {self.words[random_word][0]} is not \
                        {answer}", style='TLabel'
                    )
        
    def hint(self, hinter, hint_count, random_word):
            if hint_count < len(self.words[random_word][1]):
                hinter = hinter + self.words[random_word][1][hint_count]
                self.hint_label.config(text=hinter)
                hint_count += 1 
                return hint_count
    

        
class Spanish(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.style = ttk.Style(master=self.parent)

        self.style.configure('TButton', font=('Helvetica', 30))
        self.style.configure('TLabel', font=('Helvetica', 30))
        self.style.configure('Hint.TLabel', font=('Helvetica', 15))

        self.entry = ttk.Entry(self)
        self.entry.grid(row=10, column=1, pady=20)

        self.question_label = ttk.Label(self, text='', style='TLabel')
        self.question_label.grid(row=1, column=1, pady=50)

        self.answer_label = ttk.Label(self, text="", style='TLabel')
        self.answer_label.grid(row=1, column=1, pady=20)

        answer_button = ttk.Button(self, text="Answer", command=self.answer, 
                                   style='TButton')
        answer_button.grid(row=15, column=0, padx=20)

        next_button = ttk.Button(self, text="Next", command=self.next,
                                  style='TButton')
        next_button.grid(row=15, column=1, padx=20)

        hint_button = ttk.Button(self, text="Hint", command=self.hint,
                                  style='TButton')
        hint_button.grid(row=15, column=2)
          
        home_button = ttk.Button(self, text="Home",
                                 command=lambda: controller.show_frame(Home),
                                 style='TButton')
        home_button.grid(row=20, column=0)

        self.hint_label = ttk.Label(self, text="", style='Hint.TLabel')
        self.hint_label.grid(row=20, column=1, pady=20)
        
        self.words = [(('Buenos dias'), ('Good morning')),
                (('Buenas noches'), ('Good evening')),
                (('Gracias'), ('Thank you')),
                (('De nada'), ("You're welcome")),
                (('Adios'), ('Goodbye')),
                (('Hola'), ('Hello')),
                (('Que tal?'), ('How are you')),
                (('Me llamo'), ('My name is'))]
        
        self.count = len(self.words)

    hinter = ""
    hint_count = 0 

    def next(self):
            self.answer_label.config(text="", style='TLabel')
            self.entry.delete(0, 'end')
            self.hint_label.config(text="", style='TLabel')

            random_word = randint(0, self.count-1) 

            self.question_label.config(text=self.words[random_word][0],
                                        style='TLabel')   
            return random_word  
                                                    
    def check(self):  
        answer = self.entry.get().capitalize().strip()
        # Checks whether user enter an invalid answer such as numbers
        if answer == int(answer):
            messagebox.showinfo('Please enter a valid answer', 
                                     'Numbers are not an acceptable answer')
        else:
            # If user does not enter input, messagebox prompts them to 
            if answer == "":
                messagebox.showinfo('No input entered', 
                                        'Please give an answer')
        return answer
    
    def answer(self, answer, random_word):
            while answer > 0:
                self.check()
                if answer == self.words[random_word][1]:
                    self.answer_label.config(
                        text=f"""Correct {self.words[random_word][0]} is""" 
                        """{self.words[random_word][1]}""", style='TLabel')
                else:
                    answer != self.words[random_word][1]
                    self.answer_label.config(
                        text=f"Incorrect! {self.words[random_word][0]} is not \
                        {answer}", style='TLabel'
                    )
                                            
    def hint(self, hinter, hint_count, random_word):
            if hint_count < len(self.words[random_word][1]):
                hinter = hinter + self.words[random_word][1][hint_count]
                self.hint_label.config(text=hinter, style='Hint.TLabel')
                hint_count += 1    
            return hint_count

    
if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
