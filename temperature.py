'''
Write a program that prompts the user to enter a temperature in Celsius.
Based on the entered temperature, the program should decide whether it's a hot, moderate, or
cold day and display an appropriate message.
'''
temp=float(input("Enter the temperature in celcius"))
if (temp>=30):
    print("It's Hot day")
    print("Wear thin clothes ")
elif(temp>=20 and temp<30):
    print("It's Moderate day")
    print("Wear normal clothes")
elif(temp<20):
    print("It's cold day ")
    print("Wear thick clothes")
