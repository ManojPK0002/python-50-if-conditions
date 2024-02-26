'''Write a program that asks the user to enter 3 numbers in three variables and
 then displays the largest number.'''
num1=int(input("Enter the number1"))
num2=int(input("Enter the number2"))
num3=int(input("Enter the number3"))
if(num1>num2 and num1>num3):
    print(num1)
elif(num2>num1 and num2>num3):
    print(num2)
else:
    print(num3)
