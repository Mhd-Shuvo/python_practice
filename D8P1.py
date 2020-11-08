name ='dekko ISHO Group'
new_name ='' 
for i in range (len(name)):
    if (name[i].isupper()):
        new_name+=name[i].lower()
    elif (name[i].islower()):
        new_name+=name[i].upper()
    else:
        new_name+=name[i]
print(new_name)