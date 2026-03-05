#pass by value(immutable type:int) and pass by reference(mutable)
def change_number(x):
    x=x+10 #creates a new value,orginal is not changed
    print("Inside function:",x)
num=5
change_number(num)
print("Outside function:",num)
#output:
#Inside function: 15
#Outside function: 5

#pass by reference example(mutabble type:list)
def change_list(lst):
    lst.append(10) #modifies the original list
    print("Inside function:",lst) 
numbers=[1,2,3]
change_list(numbers)
print("Outside function:",numbers)
#output:
#Inside function: [1, 2, 3, 10]
#Outside function: [1, 2, 3, 10]

''' in list,set like mutable types inside and
 outside function value is changed .for immutable
   value not changed inside and outside function.'''