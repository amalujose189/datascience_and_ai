
#circle area
import math
def circleArea(r):
   area=math.pi *r*r
   return area

print(circleArea(5))

print("==============recursive function=================")
'''#syntax:
def function_name(parameters):
    if condition:
        return value
    else:
        return function_name(modified_parameters)
'''

#factorial
def factorial(n):
   if n<=1:
      return 1
   else:
      return n * factorial(n-1)
print(factorial(5))

#addtion

def addition(lst):
   if len(lst)==0:
      return 0
   else:
      return lst[0]+addition(lst[1:])
num=[1,2,3,4,5]
print(addition(num))

#range 5

def addbynum(n):
   if n==0:
      return 0
   else:
      return n + addbynum(n-1)

n=int(input("enter the input"))
if n<0:
   print("sum is not defined")
else:
   print(addbynum(n))

#fibonacci
def fibanacci(n):
   if n==0:
      return 0
   elif n==1:
      return 1
   else:
      return fibanacci(n-1) + fibanacci(n-2)

print(fibanacci(6)) 