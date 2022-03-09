# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:24:41 2022

@author: User
"""

import mysql.connector
from aifc import Error

global conn
try:
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="virtual assist"
            )
    c = conn.cursor()
except Error as e:
        print(e)
        
def check_login(email, password):
    sql = """SELECT * FROM accounts WHERE email = %s AND password = %s"""
    c.execute(sql, (email, password,))
    result = c.fetchone()
    conn.commit()
    print("check_login : ", result)
    return result

def on_move_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAt`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x)+str(y), 'false', 'false', 'false', "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    print("on_move_db inserted successfully")
    
def on_pressed_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAt`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x)+str(y), 'true', 'false', 'false', "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    print("on_pressed_db inserted successfully")
    
def on_released_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAt`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x)+str(y), 'false', 'true', 'false', "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    print("on_released_db inserted successfully")

def on_scroll_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAt`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x)+str(y), 'false', 'false', 'true', "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    print("on_released_db inserted successfully")
    
def on_click_db(uid, x, y, cc, result):
    sql = "INSERT INTO `features`(`uid`, `pointAt`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    c.execute(sql, (uid, str(x)+str(y), 'true', 'false', 'false', cc, str(result)),)
    conn.commit()
    print("on_click_db inserted successfully")    

  
    