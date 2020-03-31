from datetime import date
from tkinter import *
from tkcalendar import *
from tkinter import messagebox

root = Tk()

def cal_func():
    
    def calValue():
        messagebox.showinfo("your date is: ", cal.get_date())

    top = Toplevel(root)
    cal = Calendar(top, selectmode = "day", year = date.today().year, month=date.today().month, day=date.today().day)
    cal.pack()
    b3 = Button(top, text = "Click Me ", command = calValue)
    b3.pack()

def date_func():
    top = Toplevel(root)
    Label(top, text = "Select date").pack(padx = 10, pady = 10)
    ent = DateEntry(top, width = 15, background = "blue", foreground = "red", borderwidth = 3)
    ent.pack(padx = 10, pady = 10)


b1 = Button(root, text = "Calendar", command = cal_func)
b2 = Button(root, text = "DateEntry", command = date_func)

b1.pack()
b2.pack()
#tk.Button(window_Collection, text = 'Add New Collection', 
#                            command = AddCollection).grid(row = 9, column=1)


mainloop()
