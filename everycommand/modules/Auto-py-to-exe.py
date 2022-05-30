import os
#auto py to exe is purely console based
#altho it is imported like every other module it has litterally only one purpose
#you can use this file for installing/using it but there isnt any specific command that is used for it

#in the auto-py-to-exe module you can either make an exe file from a single python code, or from a whole folder.
#beware, exe files are much bigger than py files, but cannot be read by the user since its binary.

#auto-py-to-exe seems to struggle with some specific modules like PyQt for example
#it is best if it is used on some specific programs.

#BEWARE: sending/using an EXE file isn't easy since most of the time the computer sees it as a potential treath
#and many platforms: example even Mail will not send those for "security mesures".

#you can edit the False to True if you havn't
################ downloaded auto-py-to-exe
install = False# before.
################

if install == True:
    os.system("python -m pip install auto-py-to-exe")
#this code installs the module on your computer

#simply writting auto-py-to-exe on your cmd will open the Gui widget
os.system("auto-py-to-exe")



#in the GUI you can also choose if the programm should be purely window based of command based
#so, beware what programm you want to make an EXE out of and what type it is.
