#Heres how to make a PI calculator using classes
#in a class you add functions
#a class is just here for gigantic python codes to cut it into SECTORS.
                                                                #/\ English not programming language

#imagine a class being a whole code part.
#classes are really only good for big python files that have a couple different fields.
class calculatePi():
    #__init__ is the first function to work when a class is created
    #__init__ doesn't neet to be told to execute, it executes automaticly -
    #at the start when the class is created.
    def __init__(Empty):
        #creates all variables that can be used
        global Pi, Augmentor, Exchanger
        Pi = 1
        Augmentor = 1
        Exchanger = False
        
        #calculates pi uppon execution
        #gets closer by 1000 steps every time its executed

                        # \/ i set the parameter being anything really. but whitout it whouldn't work
    def doTheCalculation(Empty):
        global Pi, Augmentor, Exchanger
        for each in range(1000):
            if Exchanger:
                Pi -= 1 / Augmentor
            else:
                Pi += 1 / Augmentor
            Exchanger = not Exchanger
            Augmentor += 2
            
        return(Pi * 4)

#VERY IMPORTANT NOTE:
    #SELF DOESN'T NEED TO BE CALLED SELF.
    #SELF IS NOTHING BUT A PARAMETER AND ANY NAME WHOULD DO.

#this is creating the new class.
FirstObject = calculatePi()
#by creating the item, you execute __init__ directly

print(FirstObject.doTheCalculation())



