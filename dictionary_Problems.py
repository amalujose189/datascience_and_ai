'''Create a dictionary with 5 employees and their salaries.

Print the highest and lowest salary using dictionary functions.'''

employe={
    'emp1':45000,
    'emp2':60000,
    'emp3':35000,
    'emp4':59000,
}

print(max(employe.values()))
print(min(employe.values()))

'''2️⃣ Update Values

Given a dictionary of student marks, update one subject mark and print the updated dictionary.'''
marks = {"maths": 45, "science": 50, "english": 40}

marks.update({"english":69})
print(marks)


'''3️⃣ Add New Key-Value Pair

Add a new subject "computer": 65 to the above dictionary.'''
marks.update({"computer":65})
print(marks)
print("******************************************")
'''courses = {
    "commerce": {"economics": 34, "accountancy": 59},
    "BCA": {"java": 45, "python": 78}
}
Update economics marks to 80

Update accountancy marks to 88'''

courses = {
    "commerce": {"economics": 34, "accountancy": 59},
    "BCA": {"java": 45, "python": 78}
}
print(courses)
courses["commerce"]["economics"]=80
courses["commerce"]["accountancy"]=88

print(courses)
'''
5️⃣ Use get() Function

Write a program to access the value of a key using the get() method.

What happens if the key does not exist?'''

student = {"name": "Alice", "maths": 85, "science": 90}

# get() with existing key
print(student.get("name"))  # Output: Alice
print(student.get("maths"))  # Output: 85

# get() with non-existing key (returns None)
print(student.get("english"))  # Output: None

# get() with default value
print(student.get("english", "Not Available"))  # Output: Not Available
print(student.get("history", 0))  # Output: 0

'''Iterate Through Dictionary
Print all keys and values from a dictionary using a for loop.'''

for key,value in courses.items():
    print(key," : ",value)

'''Copy Dictionary

Create a copy of a dictionary and show that changes in the copied dictionary do not affect the original.'''
dict1={"a":1,"b":2,"c":3}
dict2=dict1.copy()