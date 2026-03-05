'''
]

🔹 DICTIONARY – Coding Questions
1️⃣ Sort dictionary by values
d = {'a': 3, 'b': 1, 'c': 2}


➡ Output: {'b':1, 'c':2, 'a':3}
'''

dict1 = {'a': 3, 'b': 1, 'c': 2}
#dict.items() returns a view object that displays a list of a dictionary's key-value tuple pairs.like[('a', 3), ('b', 1), ('c', 2)]
#sorted() function sorts the items of the dictionary based on the values (x[1]) using a lambda function as the key.
#x[1] means ('a', 3) -> 3, ('b', 1) -> 1, ('c', 2) -> 2
sorted_dict = dict(sorted(dict1.items(), key=lambda x: x[1]))

print(sorted_dict)
print("1-------------------------------------------------------")
'''2️⃣ Find key with maximum value
d = {'math': 90, 'science': 85, 'english': 88}


➡ Output: 'math' '''
marks = {'math': 900, 'science': 85, 'english': 88,'Hindi':100}
key2=max(marks, key=marks.get)
print(key2)

'''🔍 Working

max() normally returns the maximum element

Here, marks is a dictionary → iteration happens over keys

key=marks.get tells Python:

“Compare keys based on their values”

So comparisons happen like this:

math → 900
science → 85
english → 88
Hindi → 100


✔ Highest value = 900
✔ Key = 'math'

✅ Output
math

eg1:
d = {'a': 5, 'b': 10, 'c': 3}
print(max(d))
Output
c
eg2:
max() with Dictionary Values (Using key)
d = {'a': 5, 'b': 10, 'c': 3}
print(max(d, key=d.get))

Output
b
eg3:
data = [('math', 90), ('science', 85), ('english', 88)]
print(max(data, key=lambda x: x[1]))
Output
('math', 90)

eg4:
words = ["apple", "banana", "cherry"]
print(max(words))
Output
cherry

'''


