filename=input("enter the filename")
with open(filename) as file:
    text=file.read()
    letter=input("enter a char:")
    c=0
    for char in text:
        if char==letter:
            c+=1
print(letter,"appears", c ,"times in the file")
