from tkinter import *
import TestUI_Boxes
import TestUI_Fridges
import TestUI_Samples


def Main_Window():

    win = Tk()
    win.geometry("300x300")
    
    def FridgeMenu():
        win.destroy()
        TestUI_Fridges.MainFridge_Window()
        
    def BoxMenu():
        win.destroy()
        TestUI_Boxes.MainBox_Window()

    def SampleMenu():
        win.destroy()
        TestUI_Samples.MainSample_Window()

    def AddFridge():
        #win.destroy()
        TestUI_Fridges.AddFridge_Window()

    def AddBox():
        #win.destroy()
        TestUI_Boxes.AddBox_Window()
                                                                                     

# ***** Main Menu *****

    menu = Menu(win)
    win.config(menu = menu)

    subMenu = Menu(menu)
    menu.add_cascade(label = "File", menu = subMenu)
    subMenu.add_command(label = "Fridge Management", command = FridgeMenu)
    subMenu.add_command(label = "Box Management", command = BoxMenu)
    subMenu.add_command(label = "Sample Management", command = SampleMenu)
    subMenu.add_separator()
    subMenu.add_command(label = "Exit", command = menu.quit)

    editMenu = Menu(menu)
    menu.add_cascade(label = "Edit", menu = editMenu)
    #editMenu.add_command(label = "Undo", command = DoNothing)

# ***** Toolbar *****

    toolbar = Frame(win, bg = "blue")

    insertButt = Button(toolbar, text = "Add fridge", command = AddFridge)
    insertButt.pack(side = LEFT, padx = 2, pady = 2)

    printButt = Button(toolbar, text = "Add box", command = AddBox)
    printButt.pack(side = LEFT, padx = 2, pady = 2)

    toolbar.pack(side = TOP, fill = X)

# ***** Status Bar *****

    status = Label(win, text = "Example text", bd = 1, relief = SUNKEN, anchor = W)
    status.pack(side = BOTTOM, fill = X)

    win.mainloop()










