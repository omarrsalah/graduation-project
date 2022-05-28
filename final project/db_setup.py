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


def adduser(email, password, type):
    print(email)
    print(password)
    sql = """INSERT INTO accounts(email, password,type) VALUES (%s,%s,%s)"""
    c.execute(sql, (email,password,type))
    result = c.fetchone()
    conn.commit()
    print("User Added: ", result)
    return result        
def check_login(email, password):
    sql = """SELECT * FROM accounts WHERE email = %s AND password = %s"""
    c.execute(sql, (email, password,))
    result = c.fetchone()
    conn.commit()
    print("check_login : ", result)
    return result

#insert tep text and number into db needs validation
def add_to_step(stepText, stepNo):
    print(stepText)
    print(stepNo)
    sql = """INSERT INTO `steps`(`stepText`, `stepNo`) VALUES (%s,%s)"""
    c.execute(sql, (stepText, stepNo))
    result = c.fetchone()
    conn.commit()
    print("add to step: ", result)
    return result


def search_step(stepNo):
    
    print(stepNo)
    sql = """SELECT * FROM `steps` WHERE stepNo = %s"""
    c.execute(sql, (stepNo,))
    result = c.fetchone()
    conn.commit()
    print("selected step: ", result)
    return result

def on_move_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAtX`, `pointAtY`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x), str(y), "0", "0", "0", "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    # print("on_move_db inserted successfully")
    
def on_pressed_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAtX`, `pointAtY`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x), str(y), "1", "0", "0", "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    # print("on_pressed_db inserted successfully")
    
def on_released_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAtX`, `pointAtY`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x), str(y), "0", "1", "0", "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    # print("on_released_db inserted successfully")

def on_scroll_db(uid, x, y, rr):
    sql = "INSERT INTO `features`(`uid`, `pointAtX`, `pointAtY`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    val = (uid, str(x), str(y), "0", "0", "1", "0", str(rr))    
    c.execute(sql, val)
    conn.commit()
    print("on_released_db inserted successfully")
    
def on_click_db(uid, x, y, cc, result):
    sql = "INSERT INTO `features`(`uid`, `pointAtX`, `pointAtY`, `pressed`, `released`, `scrolling`, `clicks`, `idleTime`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    c.execute(sql, (uid, str(x), str(y), "1", "0", "0", cc, str(result)),)
    conn.commit()
    # print("on_click_db inserted successfully")    

  
    