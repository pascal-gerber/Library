#indexes have a lot of different ways to be written

#indexes start always with index 0, Every object has indexes.
fruits = ["orange", "apple", "pineapple"]
#         index 0 , index 1 , index 2

onefruit = "Pineapple"

#this is index 1
print(fruits[1], ", index 1 of list 'fruits'")

#the same concept works with strings
print(onefruit[1], ", second letter from word")

#we can add 2 options into the index link.

#-2 is when taken from the end
print(onefruit[2: -2], "both defined")

#if only one option given, the rest will be to one end
print(onefruit[4:], "start defined")

print(onefruit[:4], "end defined")

#theres also a thirt option
#skips letters
print(onefruit[::2], "Pnape")
#that last 2 skips one of 2 letters

#of course this can be used for reversing
print(onefruit[::-1], "reverse string")

#the index is a "slice" object

index = slice(4, 7)

#indexes can still contain up to 3 informations.
print(onefruit[index])

