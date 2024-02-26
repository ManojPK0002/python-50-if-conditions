'''32 Create a program to calculate the area of different geometric shapes
 (rec=l*b, circle=pi*r*r, triangle=1/2 *b *h).'''
length=int(input("Enter the length of rectangle"))
breadth=int(input("Enter the breadth of rectangle"))
base=int(input("Enter the base of triangle"))
height=int(input("Enter the height of triangle"))
radius=int(input("Enter the radius of circle"))
PI=3.14

rec=(length*breadth)
cir=PI*radius*radius
tri=(base*height)/2
print("area of rec is", rec)
print("area of cir is", cir)
print("area of tri is", tri)
