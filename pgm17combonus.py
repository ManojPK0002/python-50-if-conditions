'''
A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.

'''
salary=float(input("Enter the salary"))
year_exp=int(input("Enter the year"))
if(year_exp>=5):
    bonus=salary*0.05
    salary=salary+bonus
    print("Salary after bonus is",salary)
else:
    print("Salary is",salary)