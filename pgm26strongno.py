'''Write a Java program to check if a given number, is a strong number.'''



number = int(input("Enter the number"))
sum_of_factorial = 0
digits = str(number)
for digit in digits:
    factorial = 1
    for i in range(1, int(digit) + 1):
        factorial *= i
    sum_of_factorial += factorial

# Check if the sum of the factorial of the digits is equal to the number itself
if sum_of_factorial == number:
    print(f"{number} is a strong number")
else:
    print(f"{number} is not a strong number")