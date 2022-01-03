import tkinter as tk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import os
def openword():
    my_program = filedialog.askopenfilename()

    os.system('"%s"' % my_program)
def btn_clicked():
    if entry0.index("end") == 0:
        validatemail()
        return
    if not entry0.get():
        btn_clicked()
        
    if entry1.index("end") == 0:
            validatepass()
            return
    if not entry1.get():
         btn_clicked()
    tkinter.messagebox.showinfo("Login","Login Success, Welcome!")
    b1.place(
        x = 766, y = 505,
        width = 213,
        height = 72)
    
def validatemail():
        tkinter.messagebox.showinfo("Login","Please enter a valid e-mail")
def validatepass():
            tkinter.messagebox.showinfo("Login","Please enter a valid password")

window = tk.Tk()

window.geometry("1000x600")
window.configure(bg = "#293335")
canvas = tk.Canvas(
    window,
    bg = "#293335",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = tk.PhotoImage(file = f"background.png")
background = canvas.create_image(
    508.5, 228.0,
    image=background_img)

entry0_img = tk.PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
    166.0, 367.0,
    image = entry0_img)

entry0 = tk.Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)


entry0.place(
    x = 22, y = 351,
    width = 288,
    height = 30)

entry1_img = tk.PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    166.0, 456.0,
    image = entry1_img)

entry1 = tk.Entry(
    window,
    show="*",
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 22, y = 440,
    width = 288,
    height = 30)

img0 = tk.PhotoImage(file = f"img0.png")
b0 = tk.Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 28, y = 500,
    width = 102,
    height = 38)
img1 = PhotoImage(file = f"img1.png")
b1 = tk.Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = openword,
    relief = "flat")


window.resizable(False, False)
window.mainloop()
