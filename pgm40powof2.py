'''Create a program to check if a number is a power of two.'''
num = int(input("Enter the number to check if it is a power of two: "))


if (num != 0) and ((num & (num - 1)) == 0)  :
    print(f"{num} is a power of two")
else:
    print(f"{num} is not a power of two")