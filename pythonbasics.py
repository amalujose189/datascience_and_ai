#variables
#x=5
#y="john"
#print(x)
#print(y)
#print(type(x))
#print(type(y))
#y="1"
#print(type(y))
#y[2]="2" 
#print(y)# This will raise an error because strings are immutable in Python
 #casting
#x=str(x)
#y=int(y)
#print(type(x))
#print(type(y))
#print(x)
#print(y)

#x=y=z="apple"
#print(x)
#print(y)
#print(z)    


#fruits=["apple","banana","cherry"]
#x,y,z=fruits
#print(x)
#print(y)
#print(z)
#vehicles = ["car", "bike", "bus", "truck"]
#x, y, *z = vehicles
#print(x)
#print(y)
#print(z)

#bus=["BS1","BS2","BS3"]
#X1,Y1=bus[0],bus[1] 
#print(X1)
#print(Y1)


x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = "John"
print(x, y)

#arithmetic operations
x = 12
y = 5
print(x / y)
x = 12
y = 5
#print(x // y)

#membership operators
#x = ["apple", "banana"]
#print("banana" in x)
#x = ["apple", "banana"]
#print("pineapple" not in x)

#text = "Hello World"
#print("H" in text)
#print("hello" in text)
#print("z" not in text)


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)

print(x == y)


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x != y)
print(x is not y)


# list(the collection datatypes)
fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))
fruits[0]="pineapple"
fruits.append("orange")
print(fruits)
print(len(fruits))

tup=("apple", "banana", "cherry")
print(tup)
print(type(tup))
print(tup[1])
#print(tup[1]="orange") # This will raise an error because tuples are immutable in Python
print(len(tup))
#tup.append("orange") # This will raise an error because tuples are immutable in Python
#tup.remove("banana") # This will raise an error because tuples are immutable in Python
#tup.pop() # This will raise an error because tuples are immutable in Python
#tup[0]="orange" # This will raise an error because tuples are immutable in Python
#lst=list(tup)
#print(lst)
#lst[0]="orange"
#print(lst)  

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:5])

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[:4])

#thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
#print(thislist[2:])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

#Index:   0        1        2        3        4        5        6
#Item:  apple   banana   cherry   orange    kiwi    melon   mango
#Neg:    -7       -6       -5       -4        -3       -2       -1

#print(thislist.count("cherry"))

#data = ("Amal", 22, "Python")
#name, age, course = data
#print(name)
#print(age)
#print(course)


#s="sparkss"
#res=s.endswith("s")
#print(res)


