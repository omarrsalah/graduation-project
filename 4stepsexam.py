from tkinter import *
import webbrowser
import time

def step1():
    l["text"] = "Change the paragraph font to Arial"
    
    
def step2():
    l["text"] = "Change the font size to 36"
def step3():
    l["text"] = "Set the background color of the document as RED using page color option"
def step4():
    l["text"] = "Using WordArt ,write the following  “THANK YOU” .Use any style you wish and give it a font size of 20."

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#393c4b")
canvas = Canvas(
    window,
    bg = "#393c4b",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"stepsbackground.png")
background = canvas.create_image(
    550.0, 197.5,
    image=background_img)

img0 = PhotoImage(file = f"stepsimg0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = step2,
    relief = "flat")

b0.place(
    x = 5, y = 530,
    width = 79,
    height = 38)

img1 = PhotoImage(file = f"stepsimg1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = step1,
    relief = "flat")

b1.place(
    x = 5, y = 300,
    width = 79,
    height = 38)

img2 = PhotoImage(file = f"stepsimg2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = step3,
    relief = "flat")

b2.place(
    x = 5, y = 370,
    width = 79,
    height = 38)

img3 = PhotoImage(file = f"stepsimg3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = step4,
    relief = "flat")

b3.place(
    x = 5, y = 450,
    width = 79,
    height = 38)
# Create label
l = Label(window, text = "Change the paragraph font to Arial",)
l.config(font =("Calibri", 14))
l.pack(pady=40)

l.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')

window.resizable(False, False)
window.mainloop()
