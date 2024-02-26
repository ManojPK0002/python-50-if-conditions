'''Create a program to calculate the average of N numbers.'''
num =int(input("Enter the number"))
sum=0
for i in range(1,num+1):
    sum=sum+i
avg=sum/num
print(avg)

