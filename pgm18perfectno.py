'''Create a program to check if a number is a perfect number.2p – 1(2p – 1)'''



n=int(input("enter the number "))
num=0
for i in range(1,n):
    if(n%i==0):
        num=num+i
#print(num)
if(num==n):
    print("perfect")
else:
    print("not p")