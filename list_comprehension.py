'''
syntax:
newlist=[expression for item in iterable if condition==True]
'''

#squares:square every number in the list
square=[x**2 for x in [1,2,3,4,5]]
print(square)

#evens: keep only numbers divisible by 2

even=[ x for x in range(11) if x%2==0]
print(even)

#short names:keep names with 3 letters or fewer
names=["Alice","Bob","Charlie","Dave","Eve"]
shortname=[i for i in names if len(i)<=3]
print(shortname)

#uppercase:convert all string to caps
caps=[ word.upper() for word in ["Alice","ANU","soma"]]
print(caps)

#problem
#create tuple inside list

a=[(x,y) for x in range(3) for y in range(3)]
print(a)