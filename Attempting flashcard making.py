import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *
from random import randint
from tkinter import messagebox
import tkinter.font as font



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
            self.configure(bg='lightcyan1')
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

        self.france_photo = PhotoImage(file = r'C:\Users\cabemaiwaie\Desktop\france.png')
        self.france_image = self.france_photo.subsample(2,2)

        self.span_photo =  PhotoImage(file = r'C:\Users\cabemaiwaie\Desktop\span.png')
        self.span_image = self.span_photo.subsample(2,2)

        # Button
        spanish_btn = ttk.Button(self, text="Spanish",
                               style='TButton', image = self.span_image, compound = BOTTOM,
                                command=lambda: controller.show_frame(Spanish))
        french_btn = ttk.Button(self, text='France', style='TButton', image = self.france_image, compound = BOTTOM,
                              command=lambda: controller.show_frame(French))
        french_btn.grid(row=1, column=2, padx=10, pady=10)
        spanish_btn.grid(row=2, column=2,padx=10, pady=10)
       

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
      
        

        answer_button = ttk.Button(self, text="Answer", command=self.answer, style='TButton')
        answer_button.grid(row=15, column=0, padx=20)

        next_button = ttk.Button(self, text="Next", command=self.next, style='TButton')
        next_button.grid(row=15, column=1, padx=20)

        hint_button = ttk.Button(self, text="Hint", command=self.hint, style='TButton')
        hint_button.grid(row=15, column=2)
        
        self.style = ttk.Style(self)
        self.style.configure('TButton', font=('Helvetica', 12))
        self.style.map('TButton', foreground=[('pressed', 'blue'), ('active', 'white')])
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


    def next(self):
            global hinter, hint_count
            self.answer_label.config(text="")
            self.entry.delete(0, 'end')
            self.hint_label.config(text="")

            hinter = ""
            hint_count = 0

            global random_word
            random_word = randint(0, self.count-1)   
            self.question_label.config(text=self.words[random_word][0])   
        
    def answer(self):
             if self.entry.get().capitalize().strip() == self.words[random_word][1]:
                self.answer_label.config(
                    text=f"Correct {self.words[random_word][0]} is {self.words[random_word][1]}", style='TLabel')
             elif self.entry.get().capitalize() == "":
                message_box = message_box.showwarning('No input entered', 'Please give an answer')
             else:
                self.entry.get() != self.words[random_word][1]
                self.answer_label.config(
                    text=f"""Incorrect! {self.words[random_word][0]} is not"""
                    """{self.entry.get().capitalize()}", style='TLabel""")
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
            # write something
            if hint_count < len(self.words[random_word][1]):
                hinter = hinter + self.words[random_word][1][hint_count]
                self.hint_label.config(text=hinter)
                hint_count += 1 
    

        
class Spanish(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.style = ttk.Style(self)

        self.style.configure('TButton', font=('Helvetica', 30))
        self.style.configure('TLabel', font=('Helvetica', 30))
        self.style.configure('Hint.TLabel', font=('Helvetica', 15))



        self.entry = ttk.Entry(self)
        self.entry.grid(row=10, column=1, pady=20)

        self.question_label = ttk.Label(self, text='', style='TLabel')
        self.question_label.grid(row=1, column=1, pady=50)

        self.answer_label = ttk.Label(self, text="", style='TLabel')
        self.answer_label.grid(row=1, column=1, pady=20)

        answer_button = ttk.Button(self, text="Answer", command=self.answer, style='TButton')
        answer_button.grid(row=15, column=0, padx=20)

        next_button = ttk.Button(self, text="Next", command=self.next, style='TButton')
        next_button.grid(row=15, column=1, padx=20)

        hint_button = ttk.Button(self, text="Hint", command=self.hint, style='TButton')
        hint_button.grid(row=15, column=2)

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


    def next(self):
            global hinter, hint_count
            self.answer_label.config(text="", style='TLabel')
            self.entry.delete(0, 'end')
            self.hint_label.config(text="", style='TLabel')

            hinter = ""
            hint_count = 0

            global random_word
            random_word = randint(0, self.count-1)   

            self.question_label.config(text=self.words[random_word][0], style='TLabel')   
        
    def answer(self):
            if self.entry.get().capitalize().strip() == self.words[random_word][1]:
                self.answer_label.config(
                    text=f"Correct {self.words[random_word][0]} is {self.words[random_word][1]}", style='TLabel')
            elif self.entry.get().capitalize() == "":
                message_box.showinfo('No input entered', 'Please give an answer')
            else:
                self.entry.get().capitalize().strip() != self.words[random_word][1]
                self.answer_label.config(
                    text=f"Incorrect! {self.words[random_word][0]} is not {self.entry.get().capitalize()}", style='TLabel')
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
