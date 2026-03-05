'''
Remove duplicates from a list
lst = [1, 2, 3, 2, 4, 1]


➡ Output: [1, 2, 3, 4]
'''
lst = [1, 2, 3, 2, 4, 1]
lst2=[]
for i in lst:
   if i not in lst2:
      lst2.append(i)
print(lst2)
print("1-------------------------------------------------------")
'''2️⃣ Find the second largest element
lst = [10, 20, 4, 45, 99]


➡ Output: 45'''

lst = [10, 20, 4, 45, 99]
lst.sort(reverse=True)
print(lst[1])
print("2-------------------------------------------------------")
'''3️⃣ Count occurrences of each element
lst = [1, 2, 2, 3, 3, 3]


➡ Output: {1:1, 2:2, 3:3}'''
dict={}
lst = [1, 2, 2, 3, 3, 3]
for i in lst:
   if i not in dict:
      dict[i]=lst.count(i)
print(dict)
print("3-------------------------------------------------------")
'''4️⃣ Reverse a list without using reverse()
lst = [1, 2, 3, 4]
'''
lst = [1, 2, 3, 4]
reversed_lst=lst.reverse()  #This will reverse the list in place and return None
#reversed_lst=lst[::-1] #This will create a new list that is the reverse of the original list
print(lst)

lst2=["apple","banana","cherry"]
reversed_lst2=lst2[::-1]
print(reversed_lst2)
for i in lst2:
    i_reverse=i[::-1]
    print(i_reverse)

print("4-------------------------------------------------------")
'''5️⃣ Separate even and odd numbers
lst = [1, 2, 3, 4, 5, 6]


➡ Output:
Even → [2, 4, 6]
Odd → [1, 3, 5]'''

lst= [1, 2, 3, 4, 5, 6]
even_lst=[]
odd_lst=[]
for i in lst:
    if i%2==0:
        even_lst.append(i)
    else:
        odd_lst.append(i)
print("Even →",even_lst)
print("Odd →",odd_lst)
print("5-------------------------------------------------------")

''''

🔹 SET – Coding Questions
1️⃣ Find common elements (intersection)
set1 = {1, 2, 3}
set2 = {2, 3, 4}


➡ Output: {2, 3}'''
set1 = {1, 2, 3}
set2 = {2, 3, 4}
intersection=set1.intersection(set2)
print(intersection)
print("1-------------------------------------------------------")
'''2 Remove duplicates from list using set
lst = [1, 2, 2, 3, 3]'''
lst = [1, 2, 2, 3, 3]
unique_lst=set(lst)
print(unique_lst)
print("2-------------------------------------------------------")
'''5️⃣ Check if two sets are disjoint
set1 = {1, 2}
set2 = {3, 4}'''
set1 = {1, 2}
set2 = {3, 4}
disjoint=set1.isdisjoint(set2)
print(disjoint)
print("5-------------------------------------------------------")
'''
1️⃣ Find maximum and minimum in a tuple
t = (5, 2, 9, 1)
'''
t = (5, 2, 9, 1)
max_value=max(t)
min_value=min(t)
print("Maximum:",max_value)
print("Minimum:",min_value)
'''
2️⃣ Convert tuple to list and list to tuple
t = (1, 2, 3)
'''
t = (1, 2, 3)
list1=list(t)
print("List:",list1)
tuple1=tuple(list1)
print("Tuple:",tuple1)
'''4️⃣ Unpack tuple elements
t = (10, 20, 30)'''
t = (10, 20, 30)
print("Tuple:",t)
a,b,c=t
print("Unpacked values:",a,b,c)

'''
5️⃣ Check if element exists in tuple
t = (1, 2, 3, 4)
'''

'''t = (1, 2, 3, 4)
element=5
if element in t:
    print(element,"exists in tuple")
else:
    print(element,"does not exist in tuple") 
'''
print(list("abc"))