'''
Write a program to get a number from the user and print whether it is positive or negative.
'''
number=int(input("Enter the number"))
if (number>=1):
    print(f"{number} is positive")
elif(number<=-1):
    print(f"{number} is negative")
else:
    print("It is zero")