#python has classes which can inherit other classes functions

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
print(kiwi.Fly)
print(kiwi.Food)

"print(kiwi.private())"

#on other websites you always see the __init__ and Self which in most cases you don't need to touch
#private class objects tho cannot be inherited, altho its a function it
#whouldn't work.
