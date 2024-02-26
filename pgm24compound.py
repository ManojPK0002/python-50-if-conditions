'''Create a program to calculate the compound interest.'''
#formula=p(1+r/100)^n
p=int(input("Enter the principal amount"))
r=float(input("Enter the rate of interest"))
n=float(input("Enter the number of years"))
com=0
com=(p*(1+(r/100))**n)
print(com)