import sqlite3 as lite
import sys
from tkinter import *
con=lite.connect('pwsd.db')
cursor=con.cursor()


def authenticate(self,user,passwd):
    cursor.execute("SELECT Name FROM Database WHERE Name=? LIMIT 1;",(user,))
    if(cursor.fetchone()):
        cursor.execute("SELECT Password FROM Database WHERE Password=? LIMIT 1;",(passwd,))
        if(cursor.fetchone()):
            print("accepted")
            #break
        else:
            print("Username or password is incorrect!")
    else:
        print("Username or password is incorrect!")


##        if user in accounts:
##            if(passwd==accounts[user]):
##                print("Access granted")
##                break
    
#accounts={"Aldo":"8dhc*#&", "Bob":"3409&$(DH", "Jill": "123456789"}

