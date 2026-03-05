'''from functools import reduce


list1=[1,2,3,4,5,6,7,8,9,10]
mapped_list=list(map(lambda x:x*2,list1)) #map function to double each element-modied value of list returned
filtered_list=list(filter(lambda x:x%2==0,list1))#filter function to get even numbers-only those elements returned which satisfy condition
reduced_value=reduce(lambda x,y:x+y,list1)#reduce function to get sum of all elements-reduce the list to a single value by applying a binary function cumulatively to the items of the list
print("Mapped List:",mapped_list)   
print("Filtered List:",filtered_list)
print("Reduced Value:",reduced_value)'''

'''def lastelement(lst):
    for i in lst:  #this is wrong because it will return the last element of the list not the last letter of each string in the list
        return i[-1] #The issue is that your lastelement function is designed incorrectly for use with map.
        break'''

'''When map(lastelement, list1) runs:

It passes "apple" (a single string) to the function
The loop iterates: i = 'a' (first character)
It immediately returns i[-1] which is 'a'[-1] = 'a' (first character!)
'''
list1=["apple","banana","cherry"]
def lastelement(item):
    return item[-1]
mapped1=list(map(lastelement,list1))
print(mapped1)
print("-----------------------------------------------------------")

list1=["apple","banana","cherry"]
mapped=list(map(lambda x:x[-1],list1))
#last letter of each string in list1

print(mapped)


'''
program to check if word is palindrome or not using lambda function
word.reverse() -> x[::-1] - Strings don't have .reverse() method. Use slicing to reverse.
Use the parameter x - The lambda now accepts x and uses it in the condition.
Call the lambda - Changed print(palindrome) to print(palindrome(word)) to actually execute the function.
'''

#method1

word=input("enter an word:")
palindrome=lambda x:"palindrome" if x==x[::-1] else "not palindrome"
print(palindrome(word))#calling the lambda function


word2=input("enter  word2:")
print(word2.count("b"))
'''
word2 is a string, and strings are iterable.

So Python treats it like this:

"madam" → ['m', 'a', 'd', 'a', 'm']
'''
word2=["madam","hello","racecar"]
palindrome1=list(map(lambda x:"palindrome" if x==x[::-1] else "not palindrome",word2))
print(palindrome1)
palindrome2=list(map(lambda x: x==x[::-1],word2))
print(palindrome2)
palindrome3=list(filter(lambda x:x==x[::-1],word2))
print(palindrome3)