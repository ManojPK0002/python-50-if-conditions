'''
Write a program that accepts three numbers from the user and prints "increasing" if
the numbers are in increasing order,
"decreasing" if the numbers are in decreasing order, and
 "Neither increasing or decreasing order" otherwise.
'''
n1=int(input("Enter the first number"))
n2=int(input("Enter the second number"))
n3=int(input("Enter the third number"))
if(n3>n2>n1):
    print("increasing order")
elif(n3<n2<n1):
    print("decreasing order")
else:
    print("Neither increasing or decreasing order")