'''Develop a program to find the smallest among three numbers.'''

n1=int(input("enter the number1"))
n2=int(input("enter the number2"))
n3=int(input("enter the number3"))
if (n1<n2 and n1<n3):
    print(f"{n1} is small")
elif(n2<n1 and n2<n3):
    print(f"{n2} is small")
else:
    print(f"{n3} is small")
