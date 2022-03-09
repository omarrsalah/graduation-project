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
def step5():
    l["text"] = "Create page margin: top & bottom; 1.1 inch and right & left; 1.5 inch."
def step6():
    l["text"] = "Create landscape orientation & A4 paper size."
def submit():
    window.destroy()
   
    
window = Tk()

window.geometry("1000x600")
window.configure(bg = "#97a2da")
canvas = Canvas(
    window,
    bg = "#97a2da",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"lastbackground.png")
background = canvas.create_image(
    550.0, 197.5,
    image=background_img)

img0 = PhotoImage(file = f"q4img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = step4,
    relief = "flat")

b0.place(
    x = 315, y = 550,
    width = 72,
    height = 32)

img1 = PhotoImage(file = f"q5img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = step5,
    relief = "flat")

b1.place(
    x = 422, y = 550,
    width = 72,
    height = 32)

img2 = PhotoImage(file = f"q6img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = step6,
    relief = "flat")

b2.place(
    x = 529, y = 550,
    width = 72,
    height = 32)

img3 = PhotoImage(file = f"q1img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = step1,
    relief = "flat")

b3.place(
    x = 21, y = 550,
    width = 72,
    height = 32)

img4 = PhotoImage(file = f"q2img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = step2,
    relief = "flat")

b4.place(
    x = 118, y = 550,
    width = 72,
    height = 32)

img5 = PhotoImage(file = f"q3img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = step3,
    relief = "flat")

b5.place(
    x = 215, y = 550,
    width = 72,
    height = 32)
img6 = PhotoImage(file = f"submit.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = submit,
    relief = "flat")

b6.place(
    x = 865, y = 528,
    width = 111,
    height = 54)
# Create label
l = Label(window, text = "Change the paragraph font to Arial",)
l.config(font =("Calibri", 14))
l.pack(pady=40)

l.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')

window.resizable(False, False)
window.mainloop()
