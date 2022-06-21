class Parent:
    #just a class that will only be copied somewhat
    def __init__(empty, userText):
        empty.message = userText

    def printmessage(UserMessage):
        print(UserMessage.message)



class Child(Parent):
    def __init__(empty, userText):
        #super makes this init link to the other init.
        #since its in this init, it will select this init becomming the other one
        super().__init__(userText)

    #super is used if you import a module and want to take a specific class out of
    #the module to imitate a module object.
    #with it, you can basicly somewhat CONNECT this code to the Module/Other class construct.
                                        #/\ STRONG WORD
    #so you can use the module class entirely as if all the module code was there in this specific class

#creates the child class
firstExample = Child("This is a inherited class from parent")

#but uses the parent as main class
firstExample.printmessage()


#____________________________________________________________________________________________________________

#in inheritance, private classes also act differently

class pigeon():
    Fly = True
    Food = "Breadcrums"
    #private settings don't work since theyr'e made to be private
    __Secret = "im secret"
    def private():
        print(__Secret)

            #\/ kiwi inherits from pigeon the food
class kiwi(pigeon):
    Fly = False
    
#the changed properties
print(kiwi.Fly, "can a kiwi fly")
print(kiwi.Food, "what does a kiwi eat")

"print(kiwi.private())"

#on other websites you always see the __init__ and Self which in most cases you don't need to touch
#private class objects tho cannot be inherited, altho its a function it
#whouldn't work.
