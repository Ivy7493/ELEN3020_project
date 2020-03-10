from tkinter import *


def DoNothing():
    print("Nothing done")

win = Tk()

# ***** Main Menu *****

menu = Menu(win)
win.config(menu = menu)

subMenu = Menu(menu)
menu.add_cascade(label = "File", menu = subMenu)
subMenu.add_command(label = "New..", command = DoNothing)
subMenu.add_command(label = "New Project..", command = DoNothing)
subMenu.add_separator()
subMenu.add_command(label = "Exit", command = DoNothing)

editMenu = Menu(menu)
menu.add_cascade(label = "Edit", menu = editMenu)
editMenu.add_command(label = "Undo", command = DoNothing)

# ***** Toolbar *****

toolbar = Frame(win, bg = "blue")

insertButt = Button(toolbar, text = "Add fridge", command = DoNothing)
insertButt.pack(side = LEFT, padx = 2, pady = 2)

printButt = Button(toolbar, text = "Display fridge", command = DoNothing)
printButt.pack(side = LEFT, padx = 2, pady = 2)

toolbar.pack(side = TOP, fill = X)

# ***** Status Bar *****

status = Label(win, text = "Example text", bd = 1, relief = SUNKEN, anchor = W)
status.pack(side = BOTTOM, fill = X)

win.mainloop()










