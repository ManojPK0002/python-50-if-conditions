'''Create a program to check if a number is a power of two.'''

num=int(input("Enter the number to check if a number is power of two or not"))
for i in range(1,num):
    if pow(2,i) == num :
        print(f"{num}is a power of 2")
        break
else:
    print(f"{num} is not a power of 2")
