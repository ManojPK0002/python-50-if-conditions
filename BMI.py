'''
Create a program that calculates the Body Mass Index (BMI) based on the user's weight and height.
Depending on the calculated BMI, classify the user as underweight, normal weight, overweight, or obese.
An individual would be considered to be underweight if his/her
BMI was in the range of 15 to 19.9, normal weight if the BMI was 20 to 24.9,
overweight if the BMI was 25 to 29.9, and obese if it was 30 to 35 or greater. Using linear regression,
a BMI of 16.9 in men and 13.7 in women represents a complete absence of body fat stores. 31
'''
weight=float(input("Enter the weight"))
height=float(input("Enter the height in m"))

heigh=(height)**2;
#print(heigh)
BMI=weight/heigh;
print(BMI)
if (BMI>=15 and BMI<=19.9):
    print("Underweight")
elif(BMI>=20 and BMI<=24.9):
    print("normal")
elif(BMI>=25 and BMI<=29.9):
    print("overweight")
else:
    print("obese")
