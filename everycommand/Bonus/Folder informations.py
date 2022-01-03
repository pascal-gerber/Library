import os
import pathlib
#you need the OS and pathlib to read what is all in this folder

path = pathlib.Path(__file__).parent.absolute()
#this is the path where the file is located at

#root is the path and files is the filename.
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root + "\\" + file))
        #it will print all files in the path and the same can
        #be used for codes you want to use
