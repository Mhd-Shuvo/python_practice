fruits = ["apple","banana","orange","grapes","pomegranates"]

#i want to remove an element using remove method
fruits.remove("banana")
print(fruits)

#i want to remove an element using pop method
fruits.pop()
print(fruits) # i didnt assign an index value thats why it will delete the last element of the list

fruits.pop(1)
print(fruits)

#i want to remove an element using delete method

del fruits[0]
print (fruits)
del fruits
print (fruits) #this will delete the whole list,thats why its showing error