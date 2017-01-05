from tkinter import *
from tkinter import messagebox
import pymysql.cursors

top = Tk()

def checkConnection():
	try:
		connection = pymysql.connect(host=E1.get(), user=E2.get(), password=E3.get(), db=E4.get(), cursorclass=pymysql.cursors.DictCursor)
		msg = 'Connection is Ok'
	except:
		msg = 'Connection is Not Ok'
	messagebox.showinfo("Connection Check", msg)


L1 = Label(top, text = "Host").grid(row=0)
E1 = Entry(top, bd =5)
E1.grid(row=0, column=1)

L2 = Label(top, text = "Username").grid(row=1)
E2 = Entry(top, bd =5)
E2.grid(row=1, column=1)

L3 = Label(top, text = "Password").grid(row=2)
E3 = Entry(top, bd =5)
E3.grid(row=2, column=1)

L4 = Label(top, text = "Database").grid(row=3)
E4 = Entry(top, bd =5)
E4.grid(row=3, column=1)

B = Button(top, text ="Check", command = checkConnection).grid(row=4, column=1)

top.mainloop()