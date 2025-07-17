with open("random.txt",'w+') as f:
    f.write("hello student!!!!")
    f.seek(0)
    data=f.read()
    print("previous:",data)
    new_data=data.replace("student","future IT Employees")
    f.seek(0)
    f.write(new_data)
    f.truncate()
with open("random.txt",'r') as f:
    print("Latest:",f.read())