from tkinter import *
import math
#Todo List.

def CreateInterface(): 
##################################################Buttons##########################################################
#_________________________________________________Buttons_________________________________________________________#
    global allElements
    global window
    Placement = 0
    
    saveButton = Button(window, text="save file", command=save, height = 5, width = 20, bg = "SkyBlue")
    saveButton.grid(row = 0, column = 0)
    allElements.append(saveButton)

    reloadButton = Button(window, text="Reload Page", command=reloadPage, height = 5, width = 20, bg = "MediumSpringGreen")
    reloadButton.grid(row = 0, column = 1)
    allElements.append(reloadButton)

    addNewEntry = Entry(window)
    addNewEntry.grid(row = 0, column = 3)
    allElements.append(addNewEntry)

    addNewButton = Button(window, text="Add text", command=lambda addNewEntry = addNewEntry: addNew(addNewEntry.get()),height = 5, width = 20, bg = "Orchid")
    addNewButton.grid(row = 0, column = 2)
    allElements.append(addNewButton)

    exitButton = Button(window, text="Exit without\nSaving", command=exitPage, height = 5, width = 20, bg = "Red")
    exitButton.grid(row = 0, column = 5)
    allElements.append(exitButton)

    prettyMargin = Label(window, height= 3, width = 10)
    prettyMargin.grid(row = 1, column = 4)
    allElements.append(prettyMargin)

    for eachElement in toDoContent:
        Done = Button(window, text=eachElement, height = 5, width = 20)
        Done.grid(row = (int(Placement//5)) + 2, column = Placement - (Placement//5)*5)
        Done.configure(command=lambda eachElement = eachElement, Done=Done: delete(eachElement, Done))
        allElements.append(Done)
        Placement += 1

def reloadPage():
    global allElements
    for everyElement in allElements:
        everyElement.destroy()
    CreateInterface()

def addNew(newBlock): 
    toDoContent.append(newBlock)
    reloadPage()

def exitPage():
    global window
    window.destroy()

def save():
    with open("todo.txt", "w") as save:
        dataToSave = "\n".join(toDoContent)
        save.write(dataToSave)

def delete(Stuff, visualButton):
    global toDoContent
    toDoContent.remove(Stuff)
    visualButton.destroy()

with open("todo.txt", "r") as data:
    content = data.read()
    if len(content) == 0:
        toDoContent = ""
    else:
        toDoContent = content.split("\n")



allElements = []
        
window = Tk()


CreateInterface()


window.title("To do list")
window.mainloop()
