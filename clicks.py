import win32api 
import time 
import csv
 
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128 
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128 
sumLeft = 0
sumRight = 0
p=open('m.csv','a',newline='')
f=csv.writer(p)
f.writerow(['sum of left click in each coloumn','sum of right click in each coloumn'])

while True: 
    a = win32api.GetKeyState(0x01) 
    b = win32api.GetKeyState(0x02) 
 
    if a != state_left:  # Button state changed 
        state_left = a 
        # print(a) 
        if a < 0: 
            sumLeft = sumLeft+1
            f.writerow([str(sumLeft),str(sumRight)]) 
        else: 
            print('Left Button Released') 
 
    if b != state_right:  # Button state changed 
        state_right = b 
        # print(b) 
        if b < 0: 
            sumRight = sumRight+1
            f.writerow([str(sumLeft),str(sumRight)]) 
        else: 
            print('Right Button Released') 
    time.sleep(0.001) 