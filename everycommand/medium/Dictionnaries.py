#dictionnaries are another type of Variable that exists.
#in dictionnaries you have always a value connected to another.
#as simple as normal variables.
drinksNpeoples = {
    "jack": "Coca cola",
    "Joe": "Ice tea",
    "Mike": "Milk"}

#in dictionnaries you can always print out the other half
#of even the whole page.
print(drinksNpeoples, "| the whole page")

#other half.
print(drinksNpeoples["jack"], "| what is connected to jack")

#wierdly it doesn't work for the other half.
#but the lists themselves always work otherwise.

#_____________________________________________
#deleting from dictionnaries using del
del drinksNpeoples["Joe"]

print(drinksNpeoples, "|Joe has been deleted")

#clearing is another function that exists
drinksNpeoples.clear()
#simple clear command
print(drinksNpeoples, "empty")

#_____________________________________________

#adding is also very simple
drinksNpeoples["Jerome"] = "Rivella"

#theres another way to add objects to it
drinksNpeoples.update({"Jessica": "beer"})
#_____________________________________________

print(drinksNpeoples, "new added peoples")


#you can transform a list into a Dictionnary using
#these 2 lines

hobbys = ["Jack", "Football", "Joe", "Tennis", "Mike", "Skiing"]

#              \/  here goes the list
itter = iter(hobbys)
hobbyDict = dict(zip(itter, itter))


print(hobbyDict, "\n    /\\which was a list before/\\")



