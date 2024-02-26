''' write a program to check if number is an armstrong number'''
num = int(input("Enter the number to check if number is an Armstrong number or not  "))


num_digits = len(str(num))
s=0

for digit in str(num) :
    n=int(digit)**num_digits
    s=s+n


if s== num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")