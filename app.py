with open("log.txt", 'a+') as f:
    f.write("latest line appended now...\n")
    f.seek(0)
    data=f.read()
    print("current data:\n",data)