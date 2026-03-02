from math import *
from fractions import Fraction
print("Basic calculator")
choice= int(input("what you want? \n 1)add \n 2)sub \n 3)mult \n 4)div \n 5)checking n is odd or not \n 6) finding roots of quadractic eqation:"))

def ixis():
  print("enter a and b")
  a=float(input("Enter a numero:"))
  b=float(input("Enter another numero:"))
  return a,b
if choice == 1:
 # The things in here is a result of the mess i did i keep learning and updating so yeah this things are simply like a foot print
 #  print("choose a and b")  
  # a= float(input("Enter a num"))
 #  b=float(input("Enter another num"))  
   a,b=ixis()
   print(a + b)
elif choice == 2:
  #print("choose a and b")
  #a=float(input("Enter a numero:"))
  #b=float(input("enter another numero:"))
  a,b=ixis()
  print( a - b)
elif choice== 3:
 # print("enter a and b")
  #a=float(input("Enter a numero:"))
  #b=float(input("Enter another numero"))
  a,b=ixis()
  print(a * b)
elif choice== 4:
  a,b=ixis()
  c= (a / b)
  print(c)
 # if c.is_integer():
 #   print(c)
 #   else:
 # z= Fraction(c).limit_denominator()
#  print(z)

else:
  print("invalid operation")
  
 