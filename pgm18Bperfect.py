'''Create a program to check if a number is a perfect number.2p – 1(2p – 1)'''
#num=int(input("Enter the number"))


n=int(input("enter the "))
num=0
for i in range(1,n):
    if(n%i==0):
        num=num+i
        print(i)
#print(num)
if(num==n):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not perfect number")