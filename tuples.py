my_tuple=("apple","banana","cherry")
single_item=("apple",)
print(len(my_tuple))

print(my_tuple[1])
print(my_tuple[-1])

if "apple" in my_tuple:
    print("Yes, 'apple' is in the tuple")
#TUPLE IS IMMUTABLE ,convert to a list to make changes
x=("apple","banana","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)

for fruit in my_tuple:
    print(fruit)

for i in range(len(my_tuple)):
    print(my_tuple[i])
# + to combine tuples
tuple_combined=my_tuple+("orange","mango")

#USE "*" TO multiply the content
tuple_doubled=my_tuple*2
#how many times an item occurs in a tuple
print(my_tuple.count("apple"))
#find the first occurrence of an item
print(my_tuple.index("cherry"))

