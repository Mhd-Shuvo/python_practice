fruits = ["apple","banana","orange","grapes","pomegranates"]
# i want to know an index value of an element in a list
print(fruits.index("apple"))
print(fruits.index("pomegranates"))

# i want to add an element using append method
fruits.append(["pears","pomegranates","strawberries"])

print(fruits)

# i want to add an element using insert method
fruits.insert(1,"apricot")
print(fruits)

# i want to add an element using extend method
fruits.extend(["raspberries","avocado"])
print(fruits)

# i want to check an element in a list
print("apple" in fruits)
print("malta"in fruits)