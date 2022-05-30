#Encapsulation is making a specific type of variable in a class
class Secretname():
    #a public takes nothing special
    #and an object
    public = "Pascal"
    #the object can contain 2 lines before, making it
    #private *not accessible from outside*
    __private = " Secret"

    def tell():
        return(Secretname.__private)
    #the function has to be inside the class
    #in order to get access to the private value.


#first name isn't private
#it works to simply print it
print(Secretname().public)

#and since the function has the return, printing it whould
#work
print(Secretname.tell())

"print(Secretname().__private)"

#/\
#|| gives out an AttributeError since it doesn't exist

#####################################################################
#theres no need for __init__ and self,                              #
#online tutorials might have them, but its not needed at the first  #
#place.                                                             #
#####################################################################








