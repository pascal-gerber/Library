#some modules like  pillow don't work properly
#you have to download them manually, unzip them and put them into the module
#folder.
Pillow = "https://github.com/python-pillow/Pillow/archive/refs/heads/main.zip"

import webbrowser

webbrowser.open_new(Pillow)

#the place where they should be unzipped depends where your python module is
#usually it is at
import getpass
path = str("C:\\Users\\" + str(getpass.getuser()) + "\AppData\Local\Programs\Python\Python39\Lib\site-packages\pip") #ignore that \pip folder

import subprocess

#to make it easier heres the code part to open the place.
subprocess.Popen(r'explorer /select, ' + path + '')
