#in python there are 2 confusing compare methodes that cannot be compared at first view

a = []

#those 2 are
a == a
a is a

#the is and the == are not 100% the same
#here you can see how they work

first = [] #first entity
second = [] #another entity
copyFirst = first #creates a copy of first

print(first is copyFirst, "copy which is the same")
print(first is second, "another entity")
print(first == second, "same value\n")

#this works the same way as classes and objects from classes.
#strings and integers cannot be compared with is.

#lists don't work as most peoples expect.
#if a list is copied its gonna link both lists to another.

#adding a value to one list will do the same to the other
first.append("linked")

print(copyFirst, "since their both linked")
