'''Write a program to find the prime factors of a number.'''
num=int(input("Enter the number"))
lst=[]
for i in range(num):
    for j in range(2,num+1):
        if (j==2 or (j>2 and j%2!=0) )and num%j==0:
            lst.append(j)
            num//=j
print(lst)

