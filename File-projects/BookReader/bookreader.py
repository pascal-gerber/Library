from tkinter import * #GUI
import docx2txt #docx reading
import os #for searching all files
import pathlib #for getting actual file path
import math #for the squareroot
import natsort #for sorting from 1 to 10

#lists and changable content
file = ""
allFiles = []
allPageContent = []

#current page
currentPage = 0

#just so they exist
contentContainer = None

#searches all docx files out of the files
def addPagesToBook(fileName):
    global window
    global allPageContent
    fileName = natsort.natsorted(fileName)
    for each in fileName:
        try:
            result = docx2txt.process(each)
            allPageContent.append(result)
        except:
            pass

#for interface of changing files
def Swipe(direction):
    global currentPage
    
    if direction == "Back":
        currentPage -= 1
        if currentPage == -1:
            currentPage = len(allPageContent) -1
    elif direction == "Forward":
        currentPage += 1
        if currentPage == len(allPageContent):
            currentPage = 0

    changePageContent(allPageContent[currentPage])


#main interface
def createBook():
    global window
    global contentContainer
    global files
    window = Tk()

    backButton = Button(window, text="<=", command=lambda Swipe = Swipe: Swipe("Back"), width = 10, height = 8)
    backButton.grid(row = 10, column = 0)

    forwardButton = Button(window, text="=>", command=lambda Swipe = Swipe: Swipe("Forward"), width = 10, height = 8)
    forwardButton.grid(row = 10, column = 10)

    #wierd height calculation that should adapt the height of the widget to screen.
    winheight = math.sqrt(window.winfo_screenheight()) - (window.winfo_screenheight()/1000)

    contentContainer = Text(window, width = window.winfo_screenwidth()//20, height = winheight)
    contentContainer.grid(row = 3, column = 0, columnspan = 11)

    currentPage = 0
    
    #for deciding the behaviour/content of the page by the amount of DOCX files
    if len(allPageContent) == 1:
        changePageContent(allPageContent[0], True)
        backButton.configure(state=DISABLED)
        forwardButton.configure(state=DISABLED)
        window.title(files[0])
    elif len(allPageContent) == 0:
        contentContainer.insert('1.0', "Add some files to the current Path (docx) specific.")
        contentContainer.configure(state=DISABLED)
        backButton.configure(state=DISABLED)
        forwardButton.configure(state=DISABLED)
        window.title("Book Reader")
    else:
        changePageContent(allPageContent[0])
        window.title(files[0])

    window.geometry("1000x1100")
    window.mainloop()
    
#write in the Text widget the content of the current page
def changePageContent(pagecontent, onlyOne = None):
    global contentContainer

    pagecontent = files[currentPage] + "\n\n" + pagecontent

    contentContainer.configure(state=NORMAL)
    contentContainer.delete('1.0','end')

    pagecontent = pagecontent.replace(". ",  ".\n")
    if onlyOne == True:
        contentContainer.insert('1.0', pagecontent + "\n\n----------------------\nNote: Theres only one page!")
    else:
        contentContainer.insert('1.0', pagecontent)
    contentContainer.configure(state=DISABLED)

#current path
path = pathlib.Path(__file__).parent.absolute()

#all files in current path
for root, dirs, files in os.walk(path):
    files.remove("bookreader.py")
    if "how to use me.txt" in files:
        files.remove("how to use me.txt")
    if "Module Downloader.bat" in files:
        files.remove("Module Downloader.bat")
    addPagesToBook(files)

#create main interface
createBook()

