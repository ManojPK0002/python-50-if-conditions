'''Implement a program to calculate simple interest.'''
principle=int(input("Enter the principal amount"))
time=int(input("Enter the year"))
rate=int(input("Enter the rate of interest "))
simple_interest=(principle*time*rate)/100
print("simple interest is",simple_interest)

