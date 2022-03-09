import webbrowser
import time
# after 50 sec pop up

time.sleep(1)
def fn(text):
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
  
def onClick():
    webbrowser.open_new(result[0])    

QUESTIONS_LIST = ["change font size ti 24","make the font arial","make font bold"]
if __name__ == "__main__":
####
    result = fn("change font size to 24"+"https://support.microsoft.com/en-us/word")
    for r in result:
        print(r)
    # import everything from tkinter module
    from tkinter import *
    # import messagebox from tkinter module
    import tkinter.messagebox
    # create a tkinter root window
    root = tkinter.Tk()
    # root window title and dimension
    root.title("Do you need help!")
    root.geometry('300x200')
    # Create a Button
    button = Button(root, text="Click Me", command=onClick, height=2, width=10)
    # Set the position of button on the top of window.
    button.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()    
####
    # pip install google
    # pip install google-search