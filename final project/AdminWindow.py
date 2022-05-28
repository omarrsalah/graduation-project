import email
from tkinter import *
import tkinter
import tkinter.messagebox
from db_setup import *

def btn_clicked():
    print("Button Clicked")
    #add step functionality
    #addtouser=adduser(entry1.get(email), entry0.get(password), entry2.get(type))
    #ddtouser=adduser(entry1.get(), email)(entry0.get(), password)(entry2.get(),type)
    addtouser=adduser(entry1.get(),entry0.get(),entry2.get())
    #Note change all buttons down there to lambda:btn_clicked(stepNo)
    print(adduser)
    tkinter.messagebox.showinfo("Users","User added sucessfully")



window = Tk()

window.geometry("1000x600")
window.configure(bg = "#004fac")
canvas = Canvas(
    window,
    bg = "#004fac",
    height = 600,
    width = 1000,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

entry0_img = PhotoImage(file = f"AdminEntryimg_textBox0.png")
entry0_bg = canvas.create_image(
    322.5, 569.0,
    image = entry0_img)

entry0 = Entry( #password entry
    window,
    show="*",
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry0.place(
    x = 167.0, y = 551,
    width = 311.0,
    height = 34)

entry1_img = PhotoImage(file = f"AdminEntryimg_textBox1.png")
entry1_bg = canvas.create_image(
    322.5, 518.0,
    image = entry1_img)

entry1 = Entry( #email entry
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry1.place(
    x = 168.0, y = 500,
    width = 309.0,
    height = 34)

entry2_img = PhotoImage(file = f"typetextbox.png")
entry2_bg = canvas.create_image(
    691.5, 535.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#ffffff",
    highlightthickness = 0)

entry2.place(
    x = 651.0, y = 515,
    width = 81.0,
    height = 38)

background_img = PhotoImage(file = f"Adminbackground.png")
background = canvas.create_image(
    499.5, 293.5,
    image=background_img)
canvas.create_text(
    577.5, 535.0,
    text = "Type:",
    fill = "#ffffff",
    font = ("Alata-Regular", int(20.0)))

img0 = PhotoImage(file = f"add.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: btn_clicked(),
    relief = "flat")

b0.place(
    x = 775, y = 497,
    width = 186,
    height = 79)

#img1 = PhotoImage(file = f"submit.png")
#b1 = Button(
   # image = img1,
  #  borderwidth = 0,
  #  highlightthickness = 0,
  #  command = lambda: btn_clicked(email,password),
  ##  relief = "flat")

#b1.place(
   # x = 555, y = 497,
  #  width = 191,
  #  height = 79)

window.resizable(False, False)
window.mainloop()
