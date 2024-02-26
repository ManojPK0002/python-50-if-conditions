'''Write a program that prompts the user to enter three names.
Your program should display the names in descending order.'''
"""name1=input("Enter the name1")
name2=input("Enter the name2")
name3=input("Enter the name3")
name = [name1,name2,name3]
name.sort(reverse=True)

for i in name:
    print(i)"""
name1=input("Enter the name1")
name2=input("Enter the name2")
name3=input("Enter the name3")
if(name1> name2 and name1>name3):
    if (name1>name3):
        print(name1)
        if name2>name3:
            print(name2)
            print(name3)
        else:
            print(name3)
            print(name2)
elif(name2>name3 and name2>name1):
   if(name2>name1):
       print(name2)
       if name3 > name1:
           print(name3)
           print(name1)
       else:
           print(name1)
           print(name3)
elif(name3>name1 and name3>name2):
    if(name3>name2):
        print(name3)
        if(name1>name2):
            print(name1)
            print(name2)
        else:
            print(name2)
            print(name1)
