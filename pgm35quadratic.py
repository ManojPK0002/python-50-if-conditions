'''Develop a program to find the roots of a quadratic equation.ax**2+bx+c
    '''

import math
a=int(input("Enter the a value"))
b=int(input("Enter the b value"))
c=int(input("Enter the c value"))

dis=(b*b-4*a*c)
sq=math.sqrt(abs(dis))
#roots are real and same
if(a==0):
    print("Incorrect equation")
elif dis==0:
    print(-b/2*a)
    print("roots are real and same")
#roots are real and different
elif dis>0:
    print((-b + sq)/2 * a)
    print((-b - sq) / 2 * a)
    print("roots are real and different")
#roots are imaginary
else:
    print(-b/2*a,"+i" ,sq)
    print(-b / 2 * a, "-i",sq)
    print("roots are imaginary")



