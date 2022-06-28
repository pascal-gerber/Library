#functions are defines by "def"
#a function does specific commands when executed

#syntax of a function
def helloWorld():
    print("hello world")
#this can be called as much as the user wants
    
#this is how you can call a function
helloWorld()
#the name of the function and brackets, simple

#functions can have a setting inside
def printTwice(word):
#word will be the variable that holds the information
#it has been given before
    for i in range(2):
        print(word)
        #prints twice the information

#the content "twice myself" will be stored into the "word" variable
printTwice("twice myself")


#of course you will be able to give multiples settings into the
#function.

def printAsManyTimes(content, number):
    for i in range(number):
        print(content)

#the syntax isnt much different
printAsManyTimes("print me 3 times", 3)

#in functions we have also a "return" function in case we want it to
#become a certain value when written

def hi():
    return("hello world")
#now, printing the function itself will give out the return
#this will if the function itself is printed, print the return content
#or simply always take the return function.

print(hi())
#works for any function


#########################################################################################################
#to give you an idea what def can be used for
#let me make a simple example

def calculate(a, b):
    return(a + b)


print(calculate(20, 40), "calculation")

#Notice: the return function doesnt need specificly a parenthesis
#my personnal preference is to always use parenthesis.




