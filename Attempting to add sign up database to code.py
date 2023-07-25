from tkinter import *
import tkinter as tk
from openpyxl import * 

signupfile = load_workbook('C:\\Users\\cabemaiwaie\\Desktop\\Sign Up Details.xlsx')

sheet = signupfile.active


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

        sign_in_label = tk.Label(self, text="Sign In Page")
        sign_in_label.pack(padx=10, pady=10)

        # Buttons
        sign_in_btn = tk.Button(self, text="Sign Up", bg='white', width=10,
                                height=2, font=('MS Sans Serif', 8),
                                command=lambda: controller.show_frame(SignUpForm))
        login_btn = tk.Button(self, text="Login", bg='white', width=10, height=2, font=('MS Sans Serif', 8),
                              command=lambda: controller.show_frame(LoginForm))
        sign_in_btn.pack(padx=5, pady=10)
        login_btn.pack(padx=5, pady=10)


class SignUpForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        sign_up_label = tk.Label(self, text="Sign Up Form")
        sign_up_label.pack(padx=10, pady=10)

        email_label = tk.Label(self, text='Enter Email:')
        email_label.pack(padx=10, pady=10)
        email_field = tk.Entry(self)
        email_field.pack(padx=10, pady=10)

        password_label = tk.Label(self, text='Enter Password:')
        password_label.pack(padx=10, pady=10)
        password_field = tk.Entry(self)
        password_field.pack(padx=10, pady=10)

        confirm_label = tk.Label(self, text='Confirm Password:')
        confirm_label.pack(padx=10, pady=10)
        confirm_password_field = tk.Entry(self)
        confirm_password_field.pack(padx=10, pady=10)

         # function takes down from sign up form and writes it into the excel file
        def insert():

            # checking if entry is empty 
            if (email_field.get() == "" and
                password_field.get() == "" and
                confirm_password_field.get() == ""):
            
                print("Please fill in all details")
            else:
                # assigning the max row and max column value up to which data is written in an excel sheet to variables
                current_row = sheet.max_row
                current_column = sheet.max.column

                # get method returns user input as string which is written into excel spredsheet at a certain location
                sheet.cell(row=current_row + 1, column=1).value = email_field.get()
                sheet.cell(row=current_row + 1, column=2).value = password_field.get()
                sheet.cell(row=current_row + 1, column=3).value = confirm_password_field.get()

        submit_btn = tk.Button(self, text='Submit', command=insert)
        submit_btn.pack(padx=10, pady=10)
        # functions

        def excel():
            # add headings to excel spreadsheet
            sheet.cell(row=1, column=1).value = "Email"
            sheet.cell(row=1, column=2).value = "Password"
            sheet.cell(row=1, column=3).value = "Confirm Password"

        def focus1(event):
            email_field.focuse_set()

        def focus2(event):
            password_field.focus_set()

        def focus3(event):
            confirm_password_field.focus_set()

        # function clears text entry boxes when called
        def clear():

            email_field.delete(0, END)
            password_field.delete(0, END)
            confirm_password_field.delete(0, END)

        # bind method used to call the next focus function when enter key is pressed 
        email_field.bind("<Return>", focus1)
        password_field.bind("<Return>", focus2)
        confirm_password_field.bind("<Return>", focus3)


        signupfile.save('C:\\Users\\cabemaiwaie\\Desktop\\Sign Up Details.xlsx')
        
        email_field.focus_set()

        clear()

        excel()

        

        
        
        


class LoginForm(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)


if __name__ == "__main__":
    app = FlashcardsApp()
    app.mainloop()
