from tkinter import *
from tkinter import filedialog
import subprocess
import os
import sys
import csv
import getpass
import pathlib
import threading #used for future uses
import webbrowser

################################################################################################################
#for easier purposes of editing the file, i put all the changable needed variable lists on the top.
#these are the filenames choosen from python from specific paths
easystages = ["Print.py", "variables1.py", "variables2.py", "variables3.py", "Variable changes 1.py",
                     "List options.py","Input.py", "If function.py", "Loops.py", "functions.py",
                     "String options.py", "Math module and calculations.py", "indexes.py"
                     ]

mediumstages = ["classes.py", "StringManipulation.py", "open.py", "CSV.py", "Dictionnaries.py"]

hardstages = ["Encapsulation.py", "Inheritance.py", "init.py", "Compare.py", "args Kwargs.py"]

modulestages = ["Modules.py","Timemodule.py", "Turtle.py",  "osmodule.py", "Tkinter part1.py", "Tkinter part2.py",
                "Tkinter part3.py", "Tkinter part4.py", "Sys.py", "Auto-py-to-exe.py", "Specific download.py", "Flask.py",
                "async.py"]

projectstages = ["turtlestar.py", "goatgame.py", "Clock.py", "toDoList.py", "multitabbrowser.py", "Encoder.py", "minesweeper.py"]

bonusstages = ["Lists.py", "Editing files.py", "Folder informations.py"]

################################################################################################################
#same reason here why its on the top
#but these are the visual titles on the pages
easytitles = ["Print Explaination", "Datatypes", "Grouped Data", "Conversion of\nvariables", "string and lists",
              "List Sorting", "Input", "If Function", "Python Loops", "Functions", 
              "String Options", "Mathematical\nOperations","List Indexes"]

mediumtitles = ["Classes", "String manipulation", "Edit files", "CSV Files\nExcel", "Dictionnaries"]

hardtitles = ["Encapsulation\nPrivate class", "Inheritance", "__init__\nFunction", "Compare Objects", "*args\n**kwargs"]

moduletitles = ["Download\nModules","Time Module", "Basic Turtle", "OS Module", "Gui Part 1", "Gui Part 2",
                "Gui Part 3", "Gui Part 4", "System - Sys", "EXE File Conversion", "Not working\nmodules",
                "Flask\nfor Websites", "Asyncio"]

projecttitles = ["Turtle Star", "Goat Game", "Clock To 2030", "To Do List", "Multi Tab Browser", "Encoder", "Minesweeper"]

bonustitles = ["Lists", "File Manipulation", "Folder Research"]
################################################################################################################

#these are the colors of each section
#"can be edited if colors don't fit your needs"
#_______________________________________________________________________________________
easycol = ["DarkTurquoise", "Aqua"]
mediumcol = ["LimeGreen", "Lime"]
hardcol = ["FireBrick", "Red"]
modulecol = ["Teal", "LightSeaGreen"]
projectcol = ["Gold", "Yellow"]
bonuscol = ["Silver", "Gainsboro"]
#_______________________________________________________________________________________

#some variable lines "should not be edited"
Diffcolors = [easycol, mediumcol, hardcol, modulecol, projectcol, bonuscol]
difficulties = ["easy", "medium", "hard", "modules", "projects", "Bonus codes"]
ObjList = []
filename = ""

#Txt File Reader for TKinter.
def readFile(path, name):
    reader = Tk()

    contentOfFile = open(path + "\\" + name, "r")
    fileText = contentOfFile.read()
    contentOfFile.close()

    contentContainer = Text(reader)
    contentContainer.insert('1.0', fileText)
    contentContainer.grid()
    
    contentContainer.configure(state=DISABLED)

    reader.title(name)
    reader.geometry("500x500")
    reader.mainloop()
    



##################################################################################################################
##################################################################################################################
#______________________________Android_Usability_________________________________________________________________#
##################################################################################################################
##################################################################################################################

editClick = ""
editVal = None
showCode = None

#android specific kill window
def killwindow(Object):
    Object.destroy()

#very very confusing why tkinter is the only module on android that can copy to clipboard
#but as long as it works... i guess...
def androidcopytoclipboard(filetext, newWindow):
    copyandroid = Tk()
    copyandroid.withdraw()
    copyandroid.clipboard_clear()
    copid = Label(newWindow, text="content has been copied\nto clipboard\nnote: exiting the programm will empty\n" +
                  "your clipboard.")
    copid.grid(row=3)
    copyandroid.clipboard_append(filetext)

#edit localfile
def switchedit(switch):
    global showCode
    global editVal
    global editClick
    if editVal == False:
        editVal = True
        showCode['state'] = NORMAL
        editClick.configure(text="Edit :" + str(editVal))
    elif editVal == True:
        editVal = False
        showCode['state'] = DISABLED
        editClick.configure(text="Edit :" + str(editVal))

#android use
def android(pathfile):
    global showCode
    global editClick
    global editVal
    global openname
    newWindow = Tk()
    newWindow.configure(bg="Grey")
    readedcontent = ""
    with open(pathfile) as f:
        for line in csv.reader(f):
            try:
                allcontent = ",".join(line)
                readedcontent += (str(allcontent) + "\n")
            except:
                readedcontent += "\n"
        content = (readedcontent)
    showCode = Text(newWindow,height = 20)
    showCode.grid(columnspan=3)
    showCode.insert('1.0', content)
    showCode['state'] = DISABLED
    editVal = False
    editClick = Button(newWindow, text="Edit :" + str(editVal),
                       command=lambda showCode = showCode: switchedit(showCode),
                       height = 5, width = 15)
    editClick.grid(row=2, column=0)
    copytoClip = Button(newWindow, text="copy whole text\n to keyboard",
                        command=lambda newWindow = newWindow,
                        showCode = showCode:androidcopytoclipboard(str(showCode.get("1.0", END)), newWindow),
                        height = 5, width = 15)
    copytoClip.grid(row=2, column=1)
    leave = Button(newWindow, text="exit viewer", command=lambda newWindow = newWindow:killwindow(newWindow),
                   height = 5, width = 15)
    leave.grid(row=2, column=2)
    newWindow.title(openname)
    newWindow.mainloop()

openname = ""

##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################

#this selects files from the library
def buildpath(filename, difficulty):
    global openname
    openname = filename
    pathtofiles = ""
    if sys.platform == "win32" or sys.platform == "win64":
        droppedFile = os.getcwd()
        lines = "\\"
    elif sys.platform == "linux":
        droppedFile = str(pathlib.Path(__file__).parent.resolve())
        lines = "/"
    if "everycommand" not in droppedFile:
        droppedFile += "\\everycommand"
    if difficulty == "easy":
        pathtofiles += "easy" + lines + filename
    elif difficulty == "medium":
        pathtofiles += "medium" + lines + filename
    elif difficulty == "hard":
        pathtofiles += "hard" + lines + filename
    elif difficulty == "modules":
        pathtofiles += "modules" + lines + filename
    elif difficulty == "projects":
        pathtofiles += "projects" + lines + filename
    elif difficulty == "Bonus codes":
        pathtofiles += "Bonus" + lines + filename

    pathtofiles = str(droppedFile) + lines + pathtofiles
    #for other platforms \/
    if sys.platform == "win32" or sys.platform == "win64":
        openpython(pathtofiles)
    elif sys.platform == "linux":
        android(pathtofiles)

##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################

#this opens the requested file with the python program.
def openpython(path):
    global filename
    if len(filename) > 0:
        subprocess.call([filename, path])
    else:    
        exists = False
        for i in reversed(range(11)):
            try:
                subprocess.call(["C:\Program Files\Python3" + str(i) + "\Lib\idlelib\idle.bat", path])
                exists = True
                break
            except:
                pass
        if exists == False:
            for i in reversed(range(11)):
                try:
                    subprocess.call(["C:\Python3" + str(i) + "\Lib\idlelib\idle.bat", path])
                    exists = True
                    break
                except:
                    pass
            if exists == False:
                for i in reversed(range(11)):
                    pathtopython = (str("C:\\Users\\" + getpass.getuser() + "\AppData\Local\Programs\Python\Python3") + str(i) + str("\Lib\idlelib\idle.bat"))
                    try:
                        subprocess.call([pathtopython, path])
                        exists = True
                        break
                    except:
                        pass
                if exists == False:
                    information = Tk()
                    InfoText = Label(information, text="Choose the Idle.bat\n(python executer)\nfile to start the program over the\nmanually set path")
                    Infotext.configure(font = ("Lucida Console", 16))
                    InfoText.grid()
                    filename = filedialog.askopenfilename(initialdir = "/",
                                                          title = "Idle.bat",
                                                          filetypes = (("Text files", "*.bat*"), ("all files","*.*")))
                    exists = True
                    subprocess.call([filename, path])
                    information.geometry("400x100")
                    information.mainloop()

##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################
        

def number(num, difficulty):
    global easystages
    global mediumstages
    global hardstages
    global modulestages
    global projectstages
    global bonusstages
        #_______________________________________Specific Button selector_________________________________
        ########################################Easy#####################################################
    if difficulty == "easy":
                buildpath(easystages[num], "easy")
        ########################################Medium#####################################################
    elif difficulty == "medium":
        buildpath(mediumstages[num], "medium")
        ########################################Hard#####################################################
    elif difficulty == "hard":
        buildpath(hardstages[num], "hard")
        ########################################Modules#####################################################
    elif difficulty == "modules":
        buildpath(modulestages[num], "modules")
        ########################################projects#####################################################
    elif difficulty == "projects":
        buildpath(projectstages[num], "projects")
        ########################################Bonus codes#####################################################
    elif difficulty == "Bonus codes":
        buildpath(bonusstages[num], "Bonus codes")

##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################

        
def destroyLabel():
    global ObjList
    for Obj in ObjList:
        Obj.destroy()
    ObjList = []
#_______________________________________Easy_____________________________________________________        
########################################Easy#####################################################
#there are all the settups for each page

#font for each    
titlefont = ("Bahnschrift", 11)
    
def easySetup():
    global ObjList
    global window

    window.configure(bg=easycol[0])
    titles = easytitles

    Cases = Button(window, text="Correct Capitalising", command = capitalSetup, width = 30, height = 5, bg="grey")
    Cases.grid(row = 0, column = 1, columnspan = 2)
    ObjList.append(Cases)
    
    easytext = Label(window, text="Basic simple knowledge", height = 5, width=65, bg=easycol[0], font = titlefont)
    easytext.grid(row=1, column=0, columnspan=6)
    ObjList.append(easytext)
    
    for easystages in range(len(titles)):
        easy = Button(window, text=titles[easystages], bg=easycol[1],
                      command=lambda number = number, easystages = easystages:number(easystages, "easy"),
                      height = 5, width = 15, wraplength=233)
        easy.grid(row = (int(easystages//4)) + 2, column = easystages - (easystages//4)*4)
        ObjList.append(easy)
#_______________________________________Medium_____________________________________________________
########################################Medium#####################################################
        
def mediumSetup():
    window.configure(bg=mediumcol[0])
    titles = mediumtitles

    showProcess = Button(window, text="OOP and Procedural", command=createShowWindow, width = 30, height = 5, bg="grey")
    showProcess.grid(row=1, column=0, columnspan=6)
    ObjList.append(showProcess)

    mediumtext = Label(window, text="Basic Highter knowledge", height = 5, width=65, bg=mediumcol[0], font = titlefont)
    mediumtext.grid(row=1, column=0, columnspan=6)
    ObjList.append(mediumtext)
    
    for mediumstages in range(len(titles)):
        medium = Button(window, text=titles[mediumstages], bg=mediumcol[1],
                      command=lambda number = number, mediumstages = mediumstages:number(mediumstages, "medium"),
                      height = 5, width = 15)
        medium.grid(row = (int(mediumstages//4)) + 2, column = mediumstages - (mediumstages//4)*4)
        ObjList.append(medium)
#_______________________________________Hard_____________________________________________________
########################################Hard#####################################################
        
def hardSetup():
    window.configure(bg=hardcol[0])
    titles = hardtitles

    hardtext = Label(window, text="Advanced knowledge", height = 5, width=65, bg=hardcol[0], font = titlefont)
    hardtext.grid(row=1, column=0, columnspan=6)
    ObjList.append(hardtext)
    
    for hardstages in range(len(titles)):
        hard = Button(window, text=titles[hardstages], bg=hardcol[1],
                      command=lambda number = number, hardstages = hardstages:number(hardstages, "hard"),
                      height = 5, width = 15)
        hard.grid(row = (int(hardstages//4)) + 2, column = hardstages - (hardstages//4)*4)
        ObjList.append(hard)
#_______________________________________modules_____________________________________________________
########################################modules#####################################################
        
def moduleSetup():
    window.configure(bg=modulecol[0])
    titles = moduletitles
    
    regexButton = Button(window, text="Regex", command = regexSetup, width = 30, height = 5, bg="grey")
    regexButton.grid(row = 0, column = 1, columnspan = 2)
    ObjList.append(regexButton)
    
    moduletext = Label(window, text="Modules", height = 5, width=65, bg=modulecol[0], font = titlefont)
    moduletext.grid(row=1, column=0, columnspan=6)
    ObjList.append(moduletext)
    for modulestages in range(len(titles)):
        module = Button(window, text=titles[modulestages], bg=modulecol[1],
                      command=lambda number = number, modulestages = modulestages:number(modulestages, "modules"),
                      height = 5, width = 15)
        module.grid(row = (int(modulestages//4)) + 2, column = modulestages - (modulestages//4)*4)
        ObjList.append(module)
#_______________________________________projects_____________________________________________________
########################################projects#####################################################
        
def projectSetup():
    window.configure(bg=projectcol[0])
    titles = projecttitles
    
    DataButton = Button(window, text="Data Based Projects", command = dataBasedFilePage, width = 30, height = 5, bg="grey")
    DataButton.grid(row = 0, column = 1, columnspan = 2)
    ObjList.append(DataButton)
    
    projecttext = Label(window, text="Projects", height = 5, width=65, bg=projectcol[0], font = titlefont)
    projecttext.grid(row=1, column=0, columnspan=6)
    ObjList.append(projecttext)
    for projectstages in range(len(titles)):
        project = Button(window, text=titles[projectstages], bg=projectcol[1],
                      command=lambda number = number, projectstages = projectstages:number(projectstages, "projects"),
                      height = 5, width = 15)
        project.grid(row = (int(projectstages//4)) + 2, column = projectstages - (projectstages//4)*4)
        ObjList.append(project)
#______________________________________Bonus codes______________________________________________________    
########################################Bonus codes#####################################################
        
def bonusSetup():
    window.configure(bg=bonuscol[0])
    titles = bonustitles
    Support = Button(window, text="Support communities", command = Supportpage, width = 30, height = 5, bg="grey")
    Support.grid(row = 0, column = 1, columnspan = 2)
    ObjList.append(Support)
    bonustext = Label(window, text="Bonuses and shortcuts\nLife hacks", height = 5, width=65, bg=bonuscol[0], font = titlefont)
    bonustext.grid(row=1, column=0, columnspan=5)
    ObjList.append(bonustext)
    for bonusstages in range(len(titles)):
        bonus = Button(window, text=titles[bonusstages], bg=bonuscol[1],
                      command=lambda number = number, bonusstages = bonusstages:number(bonusstages, "Bonus codes"),
                      height = 5, width = 15)
        bonus.grid(row = (int(bonusstages//4)) + 2, column = bonusstages - (bonusstages//4)*4)
        ObjList.append(bonus)

#______________________________________Capitalisation______________________________________________________    
########################################Capitalisation#####################################################

def capitalSetup():
    capitalTutorial = Tk()

    titles = ("Bahnschrift", 11)
    winColor = "DeepSkyBlue"

    readMeText = """In python theres a specific way to write Variables, objects and functions.
There are 4 different capitalisations generally in programming which the most used is camelCase.
For  variables, classes and functions it is best to use camelCase."""

    Information = Label(capitalTutorial, text=readMeText,  bg=winColor)
    Information.grid(row=0, column=0,  columnspan=2)

    camelText = "camelCase is written like this :\"resultNumber, clickMeButton,  deleteContent and so on\"\nThe first word is always lowecased but every other word is uppercase\nall the words are connected"

    camelTitle = Label(capitalTutorial, text="CamelCase", font=titles,  bg=winColor)
    camelTitle.grid(row=1, column = 0)

    rarityCamel = Label(capitalTutorial, text="Most Common", bg="Goldenrod", height = 3,  width = 15)
    rarityCamel.grid(row=2, column = 0)
    
    camelCase = Label(capitalTutorial, text=camelText,  bg=winColor)
    camelCase.grid(row=3, column = 0)

    PascalTitle = Label(capitalTutorial, text="PascalCase", font=titles,  bg=winColor)
    PascalTitle.grid(row=4, column = 0)

    PascalText = "PascalCase is written like this :\"ResultNumber, ClickMeButton,  DeleteContent and so on\"\nEvery word is capital and connected, simple."

    rarityPascal = Label(capitalTutorial, text="Very common", bg="Turquoise", height = 3,  width = 15)
    rarityPascal.grid(row=5, column = 0)
    
    PascalCase = Label(capitalTutorial, text=PascalText,  bg=winColor)
    PascalCase.grid(row=6, column = 0)
    

    snake_Title = Label(capitalTutorial, text="snake_Case", font=titles,  bg=winColor)
    snake_Title.grid(row=7, column = 0)

    snake_Text = "snake_Case is written like this :\"result_number, click_me_button,  delete_content and so on\"\nno word is capital and everything is connected trought an  underscore \"_\""

    raritysnake_ = Label(capitalTutorial, text="somewhat used", bg="Bisque", height = 3,  width = 15)
    raritysnake_.grid(row=8, column = 0)
    
    snake_Case = Label(capitalTutorial, text=snake_Text,  bg=winColor)
    snake_Case.grid(row=9, column = 0)

    kebabTitle  = Label(capitalTutorial, text="kebab-Case", font=titles,  bg=winColor)
    kebabTitle .grid(row=10, column = 0)

    kebabText = "Kebab works almost the same as snake_case but the only difference is that the \"_\"  is an \"-\""

    raritykebab = Label(capitalTutorial, text="Almost never used", bg="White", height = 3,  width = 15)
    raritykebab.grid(row=11, column = 0)
    
    kebabCase = Label(capitalTutorial, text=kebabText,  bg=winColor)
    kebabCase.grid(row=12, column = 0)

    capitalTutorial.configure(bg=winColor)
    
    if sys.platform == "win32" or sys.platform == "win64":
        capitalTutorial.geometry("600x500")
    elif sys.platform == "linux":
        capitalTutorial.geometry("2000x1000")
    capitalTutorial.title("Capitalisations")
    capitalTutorial.mainloop()

#______________________________________Databased______________________________________________________    
########################################Databased#####################################################

def openPath(place):
    if place == "readMe":
        firstPathStep = str(pathlib.Path(__file__).parent.resolve())
        if "everycommand" not in firstPathStep:
            firstPathStep += "everycommand"
                            
        filePath = firstPathStep + "\\File-projects"
        readFile(filePath, "Description.txt")
    elif place == "transparent":
        desiredPath = (str(pathlib.Path(__file__).parent.resolve()) + "\\File-projects\\IMG to Transparent\\Input")
        subprocess.Popen(r'explorer /select,' + desiredPath)
    elif place == "bookReader":
        desiredPath = (str(pathlib.Path(__file__).parent.resolve()) + "\\File-projects\\BookReader\\bookreader.py")
        subprocess.Popen(r'explorer /select,' + desiredPath)


def dataBasedFilePage():
    showData = Tk()

    UserKnowledge = """this place contains whole programs that can be used/edited by you.
there will be mostly file based programms that need a specific file/save outside of the code."""
    Information = Label(showData, text=UserKnowledge, bg="DarkOrchid")
    Information.grid(row=2, column=1, columnspan=4)
    
    readMeButton = Button(showData, text="Read Me", command=lambda :openPath("readMe"),
                         height=10, width=15, wraplength=9, bg="Purple")
    readMeButton.grid(row=3, column=0)
    

    transparentImages = Button(showData, text="Image\nTransparent", command=lambda :openPath("transparent"),
                         height=10, width=15, wraplength=9, bg="Purple")
    transparentImages.grid(row=3, column=1)

    bookReader = Button(showData, text="Book\nReader", command=lambda :openPath("bookReader"),
                         height=10, width=15, wraplength=9, bg="Purple")
    bookReader.grid(row=3, column=2)
    

    

    showData.configure(bg="DarkOrchid")
    showData.title("File Projects")
    if sys.platform == "win32" or sys.platform == "win64":
        showData.geometry("600x500")
    elif sys.platform == "linux":
        showData.geometry("2000x1000")    
    showData.mainloop()

#______________________________________Support______________________________________________________    
########################################Support#####################################################
clicked = False
About = ""

def reinstall():
    global clicked
    global About
    if clicked == True:
        webbrowser.open_new("https://github.com/pascal-gerber/Library/archive/refs/heads/main.zip")
    clicked = True
    About.configure(text="you need to reinstall\nmy programm?")  

def Supportpage():
    global About
    Support = Tk()

    supportHelp = """in case you need help, there are multiples support platforms
for each of them, you need to make an account and ask nicely for help if you get stuck.
There are some support sites you can visit and ask for help in.
Good Luck to you """ + str(getpass.getuser())
    Information = Label(Support, text=supportHelp, bg="LimeGreen")
    Information.grid(row=2, column=1, columnspan=4)
    FirstSupport = Button(Support, text="Discord", command=lambda openLink = openLink:openLink("https://discord.com/invite/python"),
                         height=10, width=15, wraplength=9, bg="Lime")
    FirstSupport.grid(row=3, column=1)
    SecondSupport = Button(Support, text="Stack Overflow", command=lambda openLink = openLink:openLink("https://stackoverflow.com/questions/ask"),
                         height=10, width=15, wraplength=9, bg="Lime")
    SecondSupport.grid(row=3, column=2)
    ThirtSupport = Button(Support, text="Reddit", command=lambda openLink = openLink:openLink("https://www.reddit.com/r/Python/submit"),
                         height=10, width=15, wraplength=9, bg="Lime")
    ThirtSupport.grid(row=3, column=3)
    FourthSupport = Button(Support, text="Python Discuss", command=lambda openLink = openLink:openLink("https://discuss.python.org/top?period=monthly"),
                         height=10, width=15, wraplength=9, bg="Lime")
    FourthSupport.grid(row=3, column=3)
    About = Button(Support, text="Programm issue", command=reinstall,
                   height=10, width=15, wraplength=9, bg="Lime")
    About.grid(row=3, column=4)
   

    if sys.platform == "win32" or sys.platform == "win64":
        Support.geometry("600x500")
    elif sys.platform == "linux":
        Support.geometry("2000x1000")

    Support.title("Support communities")
    Support.configure(bg="LimeGreen")
    Support.mainloop()
    
##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################

#_________________________________OOP and Procedural______________________________________________________
##########################################################################################################

def createShowWindow():
    Process = Tk()

    Information = """"""
    
    Process.title("OOP and Procedural")
    Process.geometry("500x500")
    Process.mainloop()


##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################

    
#_________________________________Tutorial for regex______________________________________________________
##########################################################################################################


def regexSetup():
    Regex = Tk()

#######################################Information############################################################
    
    Information = Label(Regex, text="regex is a Module that finds\nspecific pattern into the text", bg="BurlyWood")
    Information.grid(row=1, column=1, columnspan=4)

    helptext = ("Cheatset:\n[aeoiu] *finds all the vovels in the text\n" +
                "(hello) *finds the specific words 'hello'\n" +
                "[^aeiou] *excludes all vowels\n\nNow the signs after those blocks\n" +
                "*  will select everything correct and connect them all\n" +
                "+  same but only works for one or more than one\n" +
                "?  will only select one at a time and ignore the empty\n" +
                "{2} will select 2 correct at a time\n\n" +
                "at the end a code will look like that:\n" +
                "[aeiou]*(hello){2}\n\nhere are some links:")

#########################################Buttons########################################################

    cheatSet = Label(Regex, text=helptext, bg="BurlyWood")
    cheatSet.grid(row=2, column=1, columnspan=4)

    FirstRegex = Button(Regex, text="regex101", command=lambda openLink = openLink:openLink("https://regex101.com/"),
                        height=10, width=15, wraplength=9, bg="Moccasin")
    FirstRegex.grid(row=3, column=1)
    SecondRegex = Button(Regex, text="regexr", command=lambda openLink = openLink:openLink("https://regexr.com/"),
                         height=10, width=15, wraplength=9, bg="Moccasin")
    SecondRegex.grid(row=3, column=2)
    cheatsheet = Button(Regex, text="Cheatsheet 1", command=lambda openLink = openLink:openLink("https://medium.com/factory-mind/regex-cookbook-most-wanted-regex-aa721558c3c1"),
                        height=10, width=15, wraplength=9, bg="Moccasin")
    cheatsheet.grid(row=3, column=3)
    secondCheat = Button(Regex, text="Cheatsheet 2", command=lambda openLink = openLink:openLink("https://www3.ntu.edu.sg/home/ehchua/programming/howto/Regexe.html"),
                         height=10, width=15, wraplength=9, bg="Moccasin")
    secondCheat.grid(row=3, column=4)
    pythonRegex = Button(Regex, text="python", command=showpyhton,
                         height=10, width=15, wraplength=9, bg="Moccasin")
    pythonRegex.grid(row=3, column=5) 

    Regex.configure(bg="BurlyWood")
    if sys.platform == "win32" or sys.platform == "win64":
        Regex.geometry("600x500")
    elif sys.platform == "linux":
        Regex.geometry("2000x1000")
    Regex.title("Regex")
    Regex.mainloop()


##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################

def openLink(link):
    webbrowser.open_new(link)
##########################################################################################################
    
def showpyhton():
    if sys.platform == "win32" or sys.platform == "win64":
        droppedFile = os.getcwd()
        lines = "\\"
        if "everycommand" not in droppedFile:
            droppedFile += "\\everycommand"
        
    elif sys.platform == "linux":
        droppedFile = pathlib.Path(__file__).parent.resolve()
        lines = "/"
        
    pathtofiles = str(droppedFile) + lines + "regex" + lines + "Regex.py"

    if sys.platform == "win32" or sys.platform == "win64":
        openpython(pathtofiles)
    elif sys.platform == "linux":
        android(pathtofiles)

##########################################################################################################
#                                           End Of function                                              #
##########################################################################################################


#__________________________________Pages___________________________________________________________________
###########################################################################################################

def switch(Name):
    global ObjList
    global DifficultyUp
    global DifficultyDown
    destroyLabel()

    Number = difficulties.index(Name)
    oneUp = Number + 1
    oneDown = Number - 1
    if oneUp == 6:
        oneUp = 0
    if oneDown == -1:
        oneDown = 5
        
    DifficultyUp.configure(text=difficulties[oneUp],bg = Diffcolors[oneUp][0],
                           command=lambda difficulties = difficulties:switch(difficulties[oneUp]))
    DifficultyDown.configure(text=difficulties[oneDown], bg = Diffcolors[oneDown][0],
                             command=lambda difficulties = difficulties:switch(difficulties[oneDown]))
    if Name == "easy":
        easySetup()
    elif Name == "medium":
        mediumSetup()
    elif Name == "hard":
        hardSetup()
    elif Name == "modules":
        moduleSetup()
    elif Name == "projects":
        projectSetup()
    elif Name == "Bonus codes":
        bonusSetup()
#__________________________________________swap pages function_____________________________________________
###########################################################################################################

def difficultyswitch():
    global window
    global DifficultyUp
    global DifficultyDown
    DifficultyUp = Button(window, text=difficulties[1],
                          command=lambda difficulties = difficulties:switch(difficulties[1]), width = 15, height = 5,
                          bg = Diffcolors[1][0])
    DifficultyUp.grid(row = 0, column = 3)
    DifficultyDown = Button(window, text=difficulties[5],
                            command=lambda difficulties = difficulties:switch(difficulties[5]), width = 15, height = 5,
                            bg = Diffcolors[5][0])
    DifficultyDown.grid(row = 0, column = 0)
    
#_________________________________button changer___________________________________________________________
###########################################################################################################

def createinterface():
    global window
    window = Tk()
    easySetup()
    difficultyswitch()
    window.title("python library")
    window.geometry("1000x1600")
    window.resizable(0, 0)
    window.columnconfigure(0, weight=10)
    window.columnconfigure(1, weight=10)
    window.columnconfigure(2, weight=11)
    window.columnconfigure(3, weight=7)
    window.columnconfigure(4, weight=9)
    window.columnconfigure(5, weight=10)
    window.mainloop()
            
createinterface()
