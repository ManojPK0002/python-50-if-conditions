'''Write a program to calculate the monthly telephone bills as per the following rule:
Minimum Rs. 200 for up to 100 calls.
Plus Rs. 0.60 per call for next 50 calls.
Plus Rs. 0.50 per call for next 50 calls.
Plus Rs. 0.40 per call for any call beyond 200 calls.
'''

"""charge_150=0.60
charge_200=0.50
charge_200plus=0.40
"""

min_charge=200
call=int(input("Enter the number of calls done"))

if call<=100:
    print("The telephonic bill is ",min_charge)
elif call>100 and call<=150:
    bill_100_150 = min_charge + (call - 100) * 0.60
    print("The telephonic bill is",bill_100_150)
elif (call>150 and call<=200):
    m1=50*0.60
    m2=(call-150)*0.50
    bill_150_200=min_charge+m1+m2
    print("The telephonic bill is", bill_150_200)
else:
    n1=50*0.6
    n2=50*0.5
    n3=(call-200)*0.4
    bill_200=min_charge+n1+n2+n3
    print("The telephonic bill is ",bill_200)



