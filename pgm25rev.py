'''25 Implement a program to find the reverse of a given number.'''
num=int(input("Enter the number"))
rev_num = 0

while num != 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10
print("Reversed Number: " ,rev_num)
