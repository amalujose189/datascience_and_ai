'''
14.check the number is palindrome or not using for loop


number=int(input("enter a number:"))
reverse=0

while number!=0:
     digit=number%10
     reverse=reverse*10+digit
     number=number//10
if reverse==number:
     print("palindrome")
else:
     print("not palindrome")
'''

'''
check given number is prime or not

flag=0
num=int(input(" enter the number"))
for i in range(2,num//2+1):
    if num%i==0:
        flag=1
        break
if flag==1:
    print("number is not prime ")   
else:
    print("number is prime")

'''

'''

16 .find reverse of a number
number=int(input("enter a number:"))
reverse=0

while number!=0:
     digit=number%10
     reverse=reverse*10+digit
     number=number//10
print(reverse)

'''

'''
17.print given numbers into words

dict={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
number=int(input("enter a number:"))
reverse=0
String1=""
for i in str(number):
   String1=String1+" "+dict[int(i)]
print(String1)
'''

'''
18.reverse a string

string2=input("enter a string:")
reverse=""
for i in range(len(string2)-1,-1,-1):
    reverse=reverse+string2[i]
print(reverse)
'''

'''
19.fibanacci series

n=int(input("enter the number of terms:"))
a=0
b=1
for i in range(1,n+1):
    print(a)
    nextitem=a+b
    a=b
    b=nextitem
'''
  

'''
20.print floyd  triangle  

num=int(input("enter the num "))
n=1
for i in range(num):
    for j in range(i+1):
        print(n,end=" ")
        
        n=n+1
    print("\n")
'''


'''
21.fibanacci series

num=int(input("enter the number"))
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)
'''



'''22. print prime numbers upto a given limit
limit=int(input(" ENTER THE LIMIT"))
for i in range(2, limit + 1):
    is_prime = True
    
    for num in range(2, i // 2 + 1):
        if i % num == 0:
            is_prime = False
            break
    
    if is_prime:
        print(i, end=" ")

print()  
'''

'''23.multipliaction table of a given number
num=int(input(" enter the number"))
for i in range(1,11):
    print(i,"*",num,"=",i*num)'''

'''24.sum of 10 numbers
sum=0
for i in range(10):
    num=int(input("enter a number:"))
    sum=sum+num
print("sum of 10 numbers is:",sum)
'''

'''25.print days of week using switch case
day = int(input("Enter number (1-7): "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid input! Please enter 1-7.")'''



'''25.print days of week using switch case
for i in range(1,8):
    match i:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
            '''
''' 26.check whether the string is palindrome or not
Str1=input("Enter a string: ")
#reverse=Str1[::-1]
reverse=""
for i in range(len(Str1)-1,-1,-1):
    reverse=reverse+Str1[i]
if Str1==reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
    '''

