from tkinter import *
import webbrowser
import time
import searching as srch
from db_setup import *
# import multiprocessing

helpers=[0,0,0,0,0,0]
def step1():
    result = search_step(1,)
    l["text"] = result[1]
    #l["text"] = "Change the paragraph font to Arial"
    if(helpers[0]==0):
        srch.helper("Change the paragraph font to Arial")
    helpers[0]=1
    
def step2():
    #result = search_step(c,2)
    result = search_step(2,)
    l["text"] =result[1]
    if(helpers[1]==0):
    
      srch.helper(result[1])
    helpers[1]=1
def step3():
    result = search_step(3,)
    l["text"] =result[1]
    if(helpers[2]==0):
        srch.helper(result[1])
    helpers[2]=1
def step4():
    result = search_step(4,)
    l["text"] =result[1]
    if(helpers[3]==0):
        srch.helper(result[1])
    helpers[3]=1
def step5():
    result = search_step(5,)
    l["text"] =result[1]
    if(helpers[4]==0):
        srch.helper(result[1])
    helpers[4]=1
def step6():
    result = search_step(6,)
    l["text"] =result[1]
    if(helpers[5]==0):
        srch.helper(result[1])
    helpers[5]=1
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
l = Label(window, text = "Start your experiment by browsing the steps below!",)
l.config(font =("Arial", 15))
l.pack(pady=60)

l.place(relx = 0.5,
                   rely = 0.5,
                   anchor = 'center')

window.resizable(False, False)
window.mainloop()
