'''for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print("\n")'''
'''for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print("\n")'''

'''for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print("\n")'''

'''for i in range(5+1):
    print(" "*(5-i),i* "*")
'''
'''for i in range(5+1):
    print(" "*(5-i),(2*i-1) * "*")'''

'''for i in range(1,5+1):
    print(" "*(5-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print(" "*(5-i),end=" ")
    print()
'''

'''for i in range(5,0,-1):
    print(" "*(5-i),(2*i-1) * "*")'''
rev=""
str="string"
for i in range(len(str)-1,-1,-1):
    rev=rev+str[i]
print(rev)

'''
for i in range(5+1):
    print(" "*(5-i),(2*i-1) * "*")
for i in range(4,0,-1):
    print(" "*(5-i),(2*i-1) * "*")'''