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
            self.show_frame(HomePage)

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
        flashcard_btn = tk.Button(self, text="Flashcards", bg='white', width=10,
                                  height=2, font=('MS Sans Serif', 8),
                                  command=lambda: controller.show_frame(Flashcards))
        create_btn = tk.Button(self, text="Create Subject", bg='white', width=10, height=2, font=('MS Sans Serif', 8),
                               command=lambda: controller.show_frame(CreateSubject))
        flashcard_btn.grid(row=2, column=1, pady=10, padx=20)
        create_btn.grid(row=4, column=1, pady=10, padx=20)


class Flashcards(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        print("h")


class CreateSubject(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
