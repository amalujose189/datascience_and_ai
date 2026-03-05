class Car:
    def start(self):
        print('Car started')
c1=Car()
c1.start()

class Student:
    def __init__(self,name,marks):
         self.name=name
         self.marks=marks
    def display(self):
         print(self.name,self.marks)

s1=Student('Rahul',86)
s1.display()

class Animal:
    def speak(self):
        print("Animal makes sound")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
d=Dog()
d.speak()
d.bark()

class Bird:
    def sound(self):
        print('Bird makes sound')
class Sparrow(Bird):
    def sound(self):
        print('sparrow chirps')
class Crow(Bird):
    def  sound(self):
        print("crow caws")
b1=Sparrow()
b2=Crow()
b1.sound()
b2.sound()
class BankAccount:
    def __init__(self,balance):
        self.__balance=balance# private variable
        
    def deposit(self,amount):
        self.__balance+=amount
       
    def get_balance(self):
        return self.__balance
acc=BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())
#print(acc.__balance)#__balance to create variable private so it can't access directly
#difference

class BankAccount1:
    def __init__(self,balance):

        self.balance1=balance
    def deposit(self,amount):
      
       self.balance1+=amount
    def get_balance(self):
        return self.balance1
acc=BankAccount1(1000)
acc.deposit(500)
print(acc.get_balance())
print(acc.balance1)

# we can access private variable only by creating a function
from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
    @abstractmethod
    def check_balance(self):
        pass
class BankATM(ATM):
    def __init__(self,balance):
        self.balance=balance
    def withdraw(self, amount):
        if amount<=self.balance:
           self.balance -= amount
           print('collect your cash')

        else:
            print('insufficient balance')
    def check_balance(self):
        print('available balance:',self.balance)
user1=BankATM(10000)
user1.check_balance()
user1.withdraw(2000)
user1.check_balance()

class Student:
    def __init__(self):
        self.name="Rahul"
    def display(self):
        print('Name',self.name)
s=Student()
print(s.name)
s.display()


class Employee:
    def __init__(self):
        self._salary=50000 # protected variable can be access in child class
class Manager(Employee):
     def show_salary(self):
        print("salary:",self._salary)
m=Manager()
m.show_salary()

#single inheritance
class one:
    def num1(self):
        print("hey")
class two(one):
    def num2(self):
        print("hello")
obj=two()
obj.num1()
obj.num2()

#multi level inheritance 
class grandfather:
    def house(self):
       print("garndfather is owner")
class  father(grandfather):
    def car(self):
        print("father buy car")
class child(father):
    def me(self):
        print("i am owner of both")
obj1=child()
obj1.house()
obj1.car()
obj1.me()
#multiple inheritance
class father:
    def house(self):
       print("father is owner")
class Mother:
    def kitchen(self):
        print("mother is owner of kitchen")
class child(father,Mother):
    def me(self):
        pass
obj1=child()
obj1.house()
obj1.kitchen()


#hierarchical inheritance
class parent:
    def property(self):
        print('parent property')
class Son(parent):
    pass
class Daughter(parent):
    pass
s=Son()
d=Daughter()
s.property()
d.property()

#hybrid inheritance
class A:
    def method(self):
        print("class A")
class B(A):
    pass
class C(A):#upto this hierarchical inheritance after that multiple inheritance
    pass
class D(B,C):
    pass
d=D()
d.method()
print("******************************************")
'''Create a class Cart with:
method add_item()
method remove_item()
method show_items()'''

lst=[]
class Cart:

    def add_item(self,a):
        lst.append(a)
        print("element is added")
    def remove_item(self,a):
        lst.remove(a)
    def show_items(self):
        print(lst)

obj=Cart()
obj.add_item('a')
obj.show_items()
obj.remove_item('a')
obj.show_items()

'''
Create classes:
CreditCard
UPI
PayPal
Each class should implement method pay().
'''
print("******************polymorphism*****************")
class CreditCard:
    def pay(self):
        print("payment using credit card")
class UPI:
    def pay(self):
        print("payment using UPI")

class PayPal:
    def pay(self):
        print("payment using paypal")
 
obj1=CreditCard()
obj1.pay()
obj2=UPI()
obj2.pay()
obj3=PayPal()
obj3.pay()
print("******************polymorphism*****************")
'''Create classes:
Circle
Square
Triangle
Each should have a draw() method.'''

class Circle:
    def draw(self):
        print("now drawing a circle")
class Square:
    def draw(self):
        print("now drawing a Square")

class Triangle:
    def draw(self):
        print("now drawing a Triangle")
 
obj1=Circle()
obj1.draw()
obj2=Square()
obj2.draw()
obj3=Triangle()
obj3.draw()

print("******************over riding*****************")
class Shape:
    def draw(self):
        pass
class Circle(Shape):
    def draw(self):
        print("now drawing a circle")
class Square(Shape):
    def draw(self):
        print("now drawing a Square")
class Triangle(Shape):
    def draw(self):
        print("now drawing a Triangle")
obj1=Circle()
obj1.draw()
obj2=Square()
obj2.draw()
obj3=Triangle()
obj3.draw()



