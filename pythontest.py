a=[1,2,3,4,5,6,7,8,9,0]
#print(a[1:])
#print(a[:9])
print(a[::])
print(a[::-1])

b="MachineLearningIsFun"
#print(b[0:7])
#print(b[7:15])
#print(b[15:20])
#print(b[-20])
#print(b[-20:-13])
#print(b[-13:-5])
#print(b[-5:])

#print(b[::-1])


#a=121
#if str(a)==str(a)[::-1]:
#    print("Palindrome")

#a="Hello"
#a=a.replace("e","*")
#print(list(a))
#a[1]
#print(a[0]+"*"+a[2:])




#b="datascience and machine learning"
b="Hello World"
c="aeiou"
ch=" "
for i in b:
    if i in c:
        ch=ch+i
print(ch[::-1])


a="Amalu"
for i in a:
    print(i*3,end="")
print('\n')
b="Hello World"
b=b.replace(" ", "")
c="aeiou"
ch=""
st=""
for i in b:
    if i in c:
        ch=ch+i
    else:
        st=st+i    
print(ch+st)




#b="abc"
#a="xyz"
#a=a[::-1]
#for i in range(3):
   # print(a[i],b[i],end="")

a=[6,9,22,66]
a.sort(reverse=True)
print(a[1])


a=[1,2,2,3,4,5]
b=[]
for i in range(0,len(a)-1):

    if a[i] not in b:
        b.append(a[i])
print(b)

a=[1,2,2,3,4,5,6,6]
b = []  # repeating elements
c = []  # all unique elements

# Find repeating elements
for i in a:
    if a.count(i) > 1 and i not in b:
        b.append(i)

# Find all unique elements
for i in a:
    if i not in c:
        c.append(i)

print("b (repeating elements):", b)
print("c (all unique elements):", c)










