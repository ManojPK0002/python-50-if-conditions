'''43 A triangle is valid if the sum of all the three angles is equal to 180 degrees.
 Write a program that asks the user to enter three integers as angles
 and check whether a triangle is valid or not. '''

angle1=int(input("Enter the angle1"))
angle2=int(input("Enter the angle2"))
angle3=int(input("Enter the angle3"))
if (angle1>0 and angle1<=90):
    if(angle2>0 and angle2<=90):
        if(angle3>0 and angle3<=90):
            sum_of_angles=angle1+angle2+angle3
if(sum_of_angles==180):
    print("The triangle is valid")
else:
    print("The triangle is not valid")
