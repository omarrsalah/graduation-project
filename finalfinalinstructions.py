from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("731x363")
window.configure(bg = "#d8d8d8")
canvas = Canvas(
    window,
    bg = "#d8d8d8",
    height = 363,
    width = 731,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"finalfinalbackground.png")
background = canvas.create_image(
    157.0, 181.5,
    image=background_img)

img0 = PhotoImage(file = f"loginimg0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 487, y = 310,
    width = 129,
    height = 44)

window.resizable(False, False)
window.mainloop()
