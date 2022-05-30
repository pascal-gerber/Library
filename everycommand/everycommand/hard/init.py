#__init__ allows to add parameters to a class whitout making a new function
#the class will be able to be executed with a parameter whitout needing to
#execute any specific function since __init__ will take it automaticly.
class MyClass:
    def __init__(self, v):
        self.test = v
    def beta(self):
        return self.test
    
a = MyClass(8)
print(a.beta(), "__init__ function")

#self is here to create certain entities with certain ID's which can be compared.
#if __init__ is used, theres always gonna be a self as well.
#class variables are defined by Self.

####################################################

#same as top

class MyClass:
    def alpha(self, v):
        self.val = v
    def beta(self):
        return self.val
a = MyClass()
a.alpha(8)
print(a.beta(), "beta function")
