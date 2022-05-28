import webbrowser
import time
from tkinter import *
from db_setup import search_step
# import multiprocessing
# from stepsui import *

# time.sleep(5)
def fen(text):
        LIST = []
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")
        query = text
        for j in search(query):
            LIST.append(j)
        return LIST
    
    # Create a messagebox showinfo

def onClick(result):
    webbrowser.open(result[1])    

def helper(str):
    ####
    result = fen(str+"https://support.microsoft.com/en-us/word")
    for r in result:
        print(r)
    # import everything from tkinter module
    # import messagebox from tkinter module
    import tkinter.messagebox
    # create a tkinter root window
    
    root = tkinter.Tk()
    # time.sleep(3)
    # root window title and dimension
    root.title("Do you need help!")
    root.geometry('300x200')
    # Create a Button
    button = Button(root, text="Click Me", command=lambda:onClick(result), height=2, width=10)
    # Set the position of button on the top of window.
    button.place(relx=0.5, rely=0.5, anchor=CENTER)



    root.mainloop()    
####
    # pip install google
    # pip install google-search