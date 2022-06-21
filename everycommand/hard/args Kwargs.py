#in python there is *args and **kwargs

#youv'e probably seen them
#In args and kwargs the most important part is the * and **

#the stars make the variable name "args" and "kwargs" able to contain more than 1 parameter.

#*args and **kwargs can take a couple of variables/values

#but we can change the name of args and kwargs.
#example:


#now you can try removing the star
                 #\/ this small sign
def addAllTogheter(*wholeCalcStuff):
    allCombined = 0
    for each in wholeCalcStuff:
        allCombined += each
    return(allCombined)


print(addAllTogheter(5, 6, 8, 9, 10, 23))

#args takes smaller variable values example "integers, strings, floats and booleans"

#kwargs takes bigger like dictionnaries with "keywords" or simply comparasons

def sayAllOut(**dictionnary):
    for first, second in dictionnary.items():
        print(first, "contains " + second)

        #  \/           \/          \/ same syntax as variables
sayAllOut(a = "hi", b = "hello", c = "yo")


#__________________________________________________________________________

#a arg and kwarg can be also used litterally in the other way too

def takeThreeValue(one, two, three):
    return(one + " then " + two + " then " + three)


whatsIn = "this", "that", "this here"
print(takeThreeValue(*whatsIn))


#___________________________________________________________________________


#it also works by both settings.
def takeThreeValue(*allOfEm):
    for each in allOfEm:
        print(each, " another")


allValues = 3, 5, 10, 23, 35, 54
print(takeThreeValue(*allValues))


#Thanks David for the help
#check him out :

#https://github.com/greyblue9

