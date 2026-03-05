'''  list=[1,2,3,4,5,6,2,7,3,8,10,2]
unique1 = []
repeating=[]
def remove_duplicates(input_list):
    
    for i in input_list:
        if i not in  unique1:
            unique1.append(i)
        else: 
            if i not in repeating:
               repeating.append(i)
remove_duplicates(list)
print(unique1)
print(repeating)

lst=[2,3,4,5,4,2,3,3,3]
dict1={}
for i in lst:
    if lst.count(i)>1:
        dict1[i]=lst.count(i)
 '''

list=[1,2,3,4,5,6,2,7,3,8,10,2]
list.sort()
print(list)
list.sort(reverse=True)
print(list)

list.reverse()
print(list)
print(list[::-1])

# Merge two lists
print("\n--- Merging Two Lists ---")
list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

# Method 1: Using + operator
merged1 = list1 + list2
print("Method 1 (+ operator):", merged1)

# Method 2: Using extend()
merged2 = list1.copy()
merged2.extend(list2)
print("Method 2 (extend()):", merged2)

# Method 3: Using unpacking
merged3 = [*list1, *list2]
print("Method 3 (unpacking):", merged3)