'''
1.recursive fun to count digits of a number

def countdigit(n):
    if n==0:
        return 0
    else:
        return 1+countdigit(n//10)
num=int(input("enter the number"))
print(countdigit(num))
'''
'''
2.recursive fun to sum of digit

def sumdigit(n):
    if n==0:
        return 0
    else:
        return (n%10)+sumdigit(n//10)
num=int(input("enter the number"))
print(sumdigit(num))
'''



'''
3.check if a list sorted using recursive fun

def is_sorted(lst):
    # Base condition: 0 or 1 element
    if len(lst) <= 1:
        return True
    
    # Base condition: First > Second means not sorted
    if lst[0] > lst[1]:
        return False
    
    # Recursive case
    return is_sorted(lst[1:])
print(is_sorted([1, 2, 3, 4]))   
print(is_sorted([1, 5, 3]))      
print(is_sorted([5]))            
print(is_sorted([]))             
'''


'''
4.reverse a string

def reverstr(s):
   
    if len(s) == 0:
        return ""
    
    return s[-1] + reverstr(s[:-1])

print(reverstr("amalu"))
###
'''


'''

check the palindrome or not
'''
def is_palindrome(s):
    
    if len(s) <= 1:
        return True
    

    if s[0] != s[-1]:
        return False
    
  
    return is_palindrome(s[1:-1])