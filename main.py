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
        home_label.grid(row = 0, column = 0, columnspan = 4, pady = 10)

        wel_label = tk.Label(self, text="""Welome to your language flashcard"""
                              """ application \n where you can begin to learn"""
                               """ the basics to \n French and Spanish""",
                            bg='lightblue',
                            font=('Helvetic',10, 'bold'))
        wel_label.grid(row = 8, column = 0, columnspan = 4, padx=10, pady = 20)


        # Button
        spanish_btn = tk.Button(self, text="Spanish", font=('Helvetica', 15), 
                                 bg="white", borderwidth = 0,
                                command=lambda: controller.show_frame(Spanish))
        french_btn = tk.Button(self, text='France', font=('Helvetica', 15), 
                                bg="white", borderwidth=0,
                              command=lambda: controller.show_frame(French))
        french_btn.grid(row = 2, column = 1, columnspan = 2, padx = 10, pady = 20)
        spanish_btn.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 20)
   
       

class French(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.entry = tk.Entry(self)
        self.entry.grid(row=10, column=1, pady=20)

        self.question_label = tk.Label(self, text="", bg='lightblue')
        self.question_label.grid(row=1, column=1, pady=50)

        self.answer_label = tk.Label(self, text="", bg='lightblue')
        self.answer_label.grid(row=1, column=1, pady=20)
      
        answer_button = tk.Button(self, text="Answer", command=self.answer, 
                                   bg='white', borderwidth=0)
        answer_button.grid(row=15, column=0, padx=20)

        next_button = tk.Button(self, text="Next", command=self.next, 
                                 bg='white')
        next_button.grid(row=15, column=1, padx=20)
        
        hint_button = tk.Button(self, text="Hint", command=self.hint,
                                   bg='white')
        hint_button.grid(row=15, column=2)

        home_button = tk.Button(self, text="Home",
                                 command=lambda: controller.show_frame(Home),
                                 bg='white')
        home_button.grid(row=20, column=0)

    
        self.hint_label = tk.Label(self, text="", bg='lightblue')
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
    hinter = ""
    hint_count = 0

    def hint(self, hinter, hint_count, random_word):
            if hint_count < len(self.words[random_word][1]):
                hinter = hinter + self.words[random_word][1][hint_count]
                self.hint_label.config(text=hinter)
                hint_count += 1 
    

        
class Spanish(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
       
        self.entry = tk.Entry(self)
        self.entry.get().capitalize().strip()
        self.entry.grid(row=10, column=1, pady=20)
        
              


        self.question_label = tk.Label(self, text='', bg='lightblue')
        self.question_label.grid(row=1, column=1, pady=50)

        self.answer_label = tk.Label(self, text="", bg='lightblue')
        self.answer_label.grid(row=1, column=1, pady=20)

        answer_button = tk.Button(self, text="Answer", command=self.answer, 
                                   bg='white')
        answer_button.grid(row=15, column=0, padx=20)

        next_button = tk.Button(self, text="Next", command=self.next,
                                   bg='white')
        next_button.grid(row=15, column=1, padx=20)

        hint_button = tk.Button(self, text="Hint", command=self.hint,
                                  bg='white')
        hint_button.grid(row=15, column=2)
          
        home_button = tk.Button(self, text="Home",
                                 command=lambda: controller.show_frame(Home),
                                  bg='white')
        home_button.grid(row=20, column=0)

        self.hint_label = tk.Label(self, text="",bg='lightblue')
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

        
        
    def next(self):
            self.answer_label.config(text="", font=('Helvetica', 30))
            self.entry.delete(0, 'end')
            self.hint_label.config(text="", font=('Helvetica', 30))

            random_word = randint(0, self.count-1) 

            self.question_label.config(text=self.words[random_word][0],
                                        font=('Helvetica', 30))   
           


    def answer(self):
            answer = self.entry.get().capitalize().strip()
            random_word = randint(0, self.count-1) 
            while len(answer) > 0:
                if answer == self.words[random_word][1]:
                    self.answer_label.config(
                        text=f"""Correct {self.words[random_word][0]} is 
                        {self.words[random_word][1]}""", 
                        font=('Helvetica', 30))
                # Checks whether user enter an invalid answer such as numbers                    
                elif answer.isnumeric():
                    messagebox.showinfo('Please enter a valid answer', 
                                        'Numbers are not an acceptable answer')
                elif answer != self.words[random_word][1]:   
                    self.answer_label.config(
                        text=f"Incorrect! {self.words[random_word][0]} is not \
                        {answer}", font=('Helvetica', 30))
            else:
                # If user does not enter input, messagebox prompts them to 
                if answer == "":
                    messagebox.showinfo('No input entered', 
                                        'Please give an answer')
   
                    
    hinter = ""
    hint_count = 0  

    def hint(self, hinter, hint_count, random_word):
            if hint_count < len(self.words[random_word][1]):
                hinter = hinter + self.words[random_word][1][hint_count]
                self.hint_label.config(text=hinter, font=('Helvetica', 30))
                hint_count += 1    

    
if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
