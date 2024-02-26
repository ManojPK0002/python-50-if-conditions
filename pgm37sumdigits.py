'''Create a program to calculate the sum of digits of a given number.
'''
num=int(input("Enter the number"))
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    num=num//10
print(sum)
