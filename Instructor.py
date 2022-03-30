from tkinter import *
from db_setup import *

def btn_clicked(stepNo):
    print("Button Clicked")
    #add step functionality
    step_result = add_to_step(entry0.get(), stepNo)
    #Note change all buttons down there to lambda:btn_clicked(stepNo)
    print(step_result)

window = Tk()

window.geometry("1000x600")
window.configure(bg = "#a3a3a3")
canvas = Canvas(
    window,
    bg = "#a3a3a3",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"instructorbackground.png")
background = canvas.create_image(
    548.0, 245.5,
    image=background_img)

img0 = PhotoImage(file = f"Addstep3.png") #Step3
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(3),
    relief = "flat")

b0.place(
    x = 644, y = 444,
    width = 132,
    height = 32)

img1 = PhotoImage(file = f"Addstep5.png") # Step5
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(5),
    relief = "flat")

b1.place(
    x = 812, y = 394,
    width = 132,
    height = 32)

img2 = PhotoImage(file = f"Addstep6.png") #Step6
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(6),
    relief = "flat")

b2.place(
    x = 812, y = 444,
    width = 132,
    height = 32)

img3 = PhotoImage(file = f"Addstep1.png") #Step1
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(1),
    relief = "flat")

b3.place(
    x = 644, y = 341,
    width = 132,
    height = 32)

img4 = PhotoImage(file = f"Addstep2.png") #Step2
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(2), #pass the parameter into button clicked
    relief = "flat")

b4.place(
    x = 644, y = 394,
    width = 132,
    height = 30)

img5 = PhotoImage(file = f"Addstep4.png") #Step4
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(4),
    relief = "flat")

b5.place(
    x = 812, y = 341,
    width = 132,
    height = 32)

entry0_img = PhotoImage(file = f"QuestionEntryimg_textBox0.png")
entry0_bg = canvas.create_image(
    286.5, 409.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e4dfdf",
    highlightthickness = 0)

entry0.place(
    x = 18, y = 373,
    width = 537,
    height = 70)

window.resizable(False, False)
window.mainloop()
