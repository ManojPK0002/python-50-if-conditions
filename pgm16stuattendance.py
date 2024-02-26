'''15 A student will not be allowed to sit in exam if his/her attendence is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print.
percentage of class attended
Is student is allowed to sit in exam or not.
'''
no_of_classes=int(input("Enter the number of classes held "))
no_of_attended=int(input("Enter the number of classes attended "))
print(f"Number of classes held is {no_of_classes}")
print(f"Number of classes attended is {no_of_attended}")
per=(no_of_attended/no_of_classes)*100
print("Percentage of attendence is",per)
if(per>=75):
    print("Student is allowed to sit in exam")
else:
    print("Student is not allowed to sit in exam")