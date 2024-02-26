'''
Write a program that displays the sum of n odd natural numbers.
'''
num=int(input("Enter the number"))
sum=0
for i in range(1,2*num+1,2):
    sum=sum+i
print(sum)
