import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image



class FlashcardsApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        width = 350
        height = 500

        self.minsize(width, height)
        self.title('Flashcard Application')

        # creating container
        container = tk.Frame(self, width=500, height=500)
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home, CreateFlashcards, FlashcardPack):
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

        home_label = tk.Label(self, text="Home")
        home_label.pack(padx=10, pady=10)

        # Buttons
        flashcard_pack_btn = tk.Button(self, text="Create Flashcard Packs", bg='white', width=20,
                                height=10, font=('MS Sans Serif', 8),
                                command=lambda: controller.show_frame(FlashcardPack))
        create_flashcards_btn = tk.Button(self, text="Create Flashcards", bg='white', width=20, height=10, font=('MS Sans Serif', 8),
                              command=lambda: controller.show_frame(CreateFlashcards))
        flashcard_pack_btn.pack(padx=5, pady=10)
        create_flashcards_btn.pack(padx=5, pady=10)


class FlashcardPack(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        pack_label = tk.Label(self, text="Create Your Flashcard Packs")
        pack_label.pack(padx=10, pady=10)

        subject_label = tk.Label(self, text='Please enter the topic you would like for your flashcard pack:')
        subject_label.pack(padx=10, pady=10)
        subject_field = tk.Entry(self)
        subject_field.pack(padx=10, pady=10)

        


        pack = []

        for i in range (len(pack)):
            topic = input('Please enter the topic you would like for your flashcard pack:')
        


        def create_pack():
            for 
            

    

     

class CreateFlashcards(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        flashcard_label = tk.Label(self, text="Create Your Flashcards")
        flashcard_label.pack(padx=10, pady=10)

        

        





if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
