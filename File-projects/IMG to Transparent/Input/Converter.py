from PIL import Image
import os
import pathlib
import math

allFiles = []

file = ""



output = ("\\".join(str(pathlib.Path(__file__).parent.absolute()).split("\\")[:-1])) + "\\output"
path = pathlib.Path(__file__).parent.absolute()

def convertImage(pathway):
    if pathway[-3:] == ".py":
        pass
    else:
        print(pathway)
        img = Image.open(pathway)
        img = img.convert("RGBA")

        width, height = Image.open(pathway).size
        
      
        datas = img.getdata()
    
        newData = []

        #Filter strenght
        Red = 240
        Green = 240
        Blue = 240

        print(len(datas)/width)

        lineStart = False

        count = -1
          
        for row in range(width):
            for column in range(height):
                count += 1
                item = datas[count]
                if item[0] > Red and item[1] > Green and item[2] > Blue:
                    newData.append((255, 255, 255, 0))
                else:
                    newData.append(item)


      
        img.putdata(newData)
        img.save(os.path.join(output, file), "PNG")
        print("Successful")



for root, dirs, files in os.walk(path):
    for file in files:
        convertImage(os.path.join(root + "\\" + file))

