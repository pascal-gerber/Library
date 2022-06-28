#Credits for this file bottom
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

#args takes variable values unordered example
# ["hello world", 4, 4.6, True, ["List", "too"], ("tuples", "and many more") ]
#args = arguments

#kwargs takes specified variables example
# [String = "hello world", Integer = 5, Float = 3.2, List = [1, 2], Tuple = (1, 2) ]
#kwargs = Key word Arguments


#----------------------------------------------------

def Arguments(firstArgument, secondArgument):
    print(firstArgument + secondArgument)

                # \/  \/ those are in a logical order
normalArguments = 43, 23

Arguments(*normalArguments)




def KeyWordArguments(normalInput, **keywords):
    #its a wierd way to write it, but its how it works
    print(keywords["secondArgument"] + keywords["firstArgument"])


KeyWordArguments(normalInput = 21, secondArgument = 32, firstArgument = 21)


#----------------------------------------------------

#made by Pascal
#taught by David

#Thanks David for the help
#check him out :

#https://github.com/greyblue9

