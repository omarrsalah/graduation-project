from tkinter import *
import random
from pynput.mouse import Listener
from pynput import mouse
import win32api
import time
import csv
import docx
import webbrowser

s = webbrowser.open("The expirement Model Answer wordfile.docx")

o = open('dataset.csv', 'w', newline='')
 
writer = csv.writer(o)
writer.writerow(['Point At X', 'Point At Y', 'Pressed At X', 'Pressed At Y', 'Released At X', 'Released At Y', 
                  'Scrolled At X', 'Scrolled At Y'])
 

def on_move(x, y):
    writer.writerow([x, y, 'false', 'false', 'false', 'false', 'false', 'false'])

    

def on_click(x, y, button, pressed):
    if pressed:
        writer.writerow([x, y, 'true', 'true', 'false', 'false', 'false', 'false']);

    else:
        writer.writerow([x, y, 'false', 'false', 'true', 'true', 'false', 'false']);


def on_scroll(x, y, dx, dy):
    writer.writerow([x, y, 'false', 'false', 'false', 'false', 'true', 'true']);

def main():
# Collect events until released
    with mouse.Listener(
        on_move=on_move,
        on_click=on_click,
        on_scroll=on_scroll) as listener:
        listener.join()

# ...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_move=on_move,
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
