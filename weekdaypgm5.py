'''
Write a program that takes a number from the user and generates an integer between 1 and 7.
 It displays the weekday name.
'''
'''
weekday=int(input("Enter the number from 1 to 7"))
dict={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday",}
if weekday in dict.keys():
    print(dict.values())
'''
weekday=int(input("Enter the number from 1 to 7"))
if(weekday>=1 and weekday<=7):
    if(weekday==1):
        print("Monday")
    elif(weekday==2):
        print("Tuesday")
    elif(weekday==3):
        print("Wednesday")
    elif(weekday==4):
        print("Thursday")
    elif(weekday==5):
        print("Friday")
    elif(weekday==6):
        print("Saturday")
    elif(weekday==7):
        print("Sunday")
else:
    print("Enter the value between 1 to 7")

