#dictionnaries are another type of Variable that exists.
#in dictionnaries you have always a value connected to another.
#as simple as normal variables.
DrinksNpeoples = {
    "jack": "Coca cola",
    "Joe": "Ice tea",
    "Mike": "Milk"}

#in dictionnaries you can always print out the other half
#of even the whole page.
print(DrinksNpeoples, "| the whole page")

#other half.
print(DrinksNpeoples["jack"], "| what is connected to jack")

#wierdly it doesn't work for the other half.
#but the lists themselves always work otherwise.

#_____________________________________________
#deleting from dictionnaries using del
del DrinksNpeoples["Joe"]

print(DrinksNpeoples, "|Joe has been deleted")

#clearing is another function that exists
DrinksNpeoples.clear()
#simple clear command
print(DrinksNpeoples, "empty")

#_____________________________________________

#adding is also very simple
DrinksNpeoples["Jerome"] = "Rivella"

#theres another way to add objects to it
DrinksNpeoples.update({"Jessica": "beer"})
#_____________________________________________

print(DrinksNpeoples, "new added peoples")










