marks=int(input("Enter the marks"))

#behavior
if(marks>=0 and marks <=100):#validation
    if(marks>=80):
        print("A+")
    elif(marks>=60 and marks<=79):
        print("A")
    elif(marks>=50 and marks<=60):
        print("B")
    elif(marks>=40 and marks<=50):
        print("C")
    elif(marks<35):
        print("Fail")
    else:
        print("Pass")
else:
    print("Invalid input")