'''Implement a program that checks if a given year is a leap year or not.
The program should prompt the user to enter a year and then output
whether it's a leap year or not based on the leap year rules.
'''
#state
year=int(input("Enter the year"))
#behavior
if(year>=1000 and year<=9999):
    if(year%4==0 and (year%100!=0 or year% 400==0)):
        print(year ," year is leap year")
    else:
        print(year," year  is not leap year")
else:
    print("Invalid input")
