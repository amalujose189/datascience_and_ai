#runtime errors are exceptions
'''a=10
b=0
print(a/b)
#ZeroDivisionError: division by zero
'''

'''print(int("abc"))
ValueError: invalid literal for int() with base 10: 'abc'
'''

'''a=10
b=5
print(a+b/2)

logic error correct method to get averege is print((a+b)/2)
'''

# to handle error we use exception handling so that it will not display errors ,it will run show msg that we given 
'''try:
    a=10
    b=0
    print(a/b)
except:
    print("error")'''

'''try:
    a=int(input("enter the value of a:"))
    b=10
    print(b/a)
except ValueError:
    print("error")
    '''
'''
try:
    a=int(input("enter the value of a:"))
    b=10
    print(b/a)
except ValueError:
    print("error")
except ZeroDivisionError:
    print(" a can't be zero")
    
'''
'''try:
    a=int(input("enter the value of a:"))
    b=10
    print(b/a)
except (ValueError,ZeroDivisionError):
    print("error" or " a can't be zero")
'''
'''try:
    a=int(input("enter the value of a:"))
    b=10
    print(b/a)
except (ValueError,ZeroDivisionError):
    print("Error occurred! Either invalid input or division by zero.")'''

'''try:
    a=int(input("enter the value of a:"))
    b=10
    result=b/a
except (ValueError,ZeroDivisionError):
    print("Error occurred! Either invalid input or division by zero.")
else:
    print(result)
'''
'''try:
    file=open("exception.txt")
except FileNotFoundError:
    print("file is not found")
finally:
    print("finally executed")'''

'''try:
    file=open("exception.txt")
except FileNotFoundError as e:
    print("Error found:",e)
finally:
    print("finally executed")'''


'''age=int(input("enter the age"))
if age<18:
    raise Exception("age below is not elgible")
else:
    print("access granted")'''
'''age=int(input("enter the age"))
if age<18:
    raise ValueError("age below is not elgible")
else:
    print("access granted")'''


#customize the errors
try:
    age=int(input("enter the age"))
    if age<18:
        raise Exception("age below is not elgible")
    else:
        print("access granted")
except Exception as e:
    print("Error:",e)

