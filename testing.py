#import random
import os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import tkinter as tk
window = tk.Tk()
window.geometry("800x600")


booksAvailable = []
class book:
    def __init____init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    # def creation(self):

def bookCreationScreen():
    creationPage = tk.Frame(window)
    mainpage.pack_forget()  
    creationPage.pack()
    window.title("Create Book")
    window.geometry("400x300")
    titleInputTopText = tk.Label(creationPage, text= "please set a title for the work")
    titleInputTopText.grid(row= 1, column= 0)
    titleInput = tk.Entry(creationPage, width=40)
    titleInput.grid(row= 2, column= 0)
    authorInputTopText = tk.Label(creationPage, text= "please set an author for this work")
    authorInputTopText.grid(row= 3, column= 0)
    titleInput = tk.Entry(creationPage, width=40)
    titleInput.grid(row= 4, column= 0)
def mainpage():
    global mainpage
    mainpage = tk.Frame(window)
    mainpage.pack()
    window.title("main menu")
    button1 = tk.Button(mainpage, text='Create', width=50, command= bookCreationScreen)
    button1.grid(row=1, column=0)

mainpage()
window.mainloop()