import math

a=float(input("enter ENTP marks out of 100:"))
b=float(input("enter UHV marks out of 100:"))
c=float(input("enter DS marks out of 100:"))
d=float(input("enter AI marks out of 100:"))
e=float(input("enter OS marks out of 100:"))

total=(a+b+c+d+e)
per=(total/5)

if per>=75:
     print("Distinction")
elif per < 75 and per >= 60:
     print("First class")
elif per < 60  and per >= 50:
     print("second class")
elif per <50  and per >= 35:
     print("pass class")
elif per <35  :
     print("Fail")

print(total)
