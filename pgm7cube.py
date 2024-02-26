'''Write a program to display the cube of the given number up to an integer.'''
num =int(input("Enter the number"))
for i in range(1,num+1):
    i=i*i*i

    print(f"cube numbers upto {num} are",i)
