'''29 Implement a program to check if a given number, is a perfect square.'''
import math
num=int(input("Enter the number"))
s=math.sqrt(num)
if (s==math.floor(math.sqrt(num))):
    print(f"{num} is perfect square")
else:
    print(f"{num} is not a perfect square")