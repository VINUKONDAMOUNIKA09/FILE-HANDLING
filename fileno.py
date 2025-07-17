import sys
age=int(input("enter age:"))
if age<18:
    print("not eligible to drive....")
    sys.exit()
print("you are eligible.......")