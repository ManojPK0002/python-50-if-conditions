'''
Write a program that reads a floating-point number and prints "zero" if the number is zero. Otherwise, print "positive" or "negative".
Add "small" if the absolute value of the number is less than 1, or "large" if it exceeds 1,000,000.
'''
"""num=float(input("Enter the number"))
#if num==0:
#   print("It is zero")
if (num>=1):
    print("positive")
    if(num>1000000):
        print("Large")
elif(num<1):
    print("small")
    if(num==0):
        print("zero")
    elif(num<0):
        print("negative")"""
# Define a string with only whitespace characters
s1 = "   "

# Define a string with some whitespace characters and some non-whitespace characters
s2 = "Hello,World!"

# Check if the string only contains whitespace characters
if s1.isspace():
    print(s1, "only contains whitespace characters.")
else:
    print(s1, "contains both whitespace and non-whitespace characters.")

# Check if the string only contains whitespace characters
if s2.isspace():
    print(s2, "only contains whitespace characters.")
else:
    print(s2, "contains both whitespace and non-whitespace characters.")