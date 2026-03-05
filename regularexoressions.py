'''import re
Str1="my number is 9778240189"
result=re.search(r"\d+",Str1)
#print(result.group())
print(result.group())
print(result.groups())
print(result.end())
print(result.start())
'''
#metacharacters are spc characters used in regex
#^ used to indicating  starting of a string
#1. . (Dot)-any single character newline
import re
'''print(re.findall("h.t", "hat hit hot hut")) #out:['hat', 'hit', 'hot', 'hut']

#2. ^ (Caret)
re.findall("^Hello", "Hello world")'''
'''
#3. $-Matches end of the string
print(re.findall("world$", "Hello world"))

#4. [] (Square Brackets)-Matches any one character inside brackets.
re.findall("[aeiou]", "hello")#['e', 'o']
#Range example:
print(re.findall("[a-z]", "abc123"))
#[^ ]👉 Matches characters NOT inside brackets

print(re.findall("[^0-9]", "abc123"))

test="hello world"
print(re.findall(r"^hello",test))

test="hello world"
print(re.findall(r"world$",test))

print(re.findall(r"a.b","aab aeroplane amby aaabin"))#['aab', 'amb', 'aab']

print(re.findall(r"a+","aaabbbaaaam  aaaap"))#['aab', 'amb', 'aab']

#character class-checking any one
print(re.findall(r"[^aeiou]","educations")) #^ means not 
print(re.findall(r"[aeiou]","educations"))
print(re.findall(r"[^0-9]","educations123"))
print(re.findall(r"[0-9]","educations123"))
print(re.findall(r"[A-Z]","Educations123"))
print(re.findall(r"[^tion]","Educations123"))

'''
Str1="my number is 9778240189"
result=re.search(r"\d",Str1)
print(result.group())

Str2="my number is 9778240189"
result=re.findall(r"\d",Str2)
print(result)

result=re.findall(r"\d+",Str2)
print(result)

result=re.findall(r"\w+",Str2)
print(result)