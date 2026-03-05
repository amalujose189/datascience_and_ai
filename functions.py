#normal/positional arguments
def greet(name,place):
  print(name,"is from",place)
greet("Amal","Kerala")
#default arguments
def country_info(country="India"):
  print("country :",country)
country_info()
country_info("USA")
#uses default if no argument is passed

#*args (arbitary positional arguments)

def show_children(*kids):
  print("children :",kids)

show_children("Emil","Tobias","Linus")

#KIDS COLLECTS UNKNOWN NUMBER OF VALUES INTO A TUPLE

def student(fname,loc):
  print(fname," from "+loc)
student(loc="Kerala",fname="Amalu")
#order does not matter because keys are used
print("********************************************************")
#**kwargs(Arbitary keyword arguments)
def student_details(**info):
  print("Name :",info["fname"])
  print("loaction :",info["loc"])
  print("age :",info["age"])
student_details(fname="Amal",loc="Kerala",age=22)

#**info collects unknown keyword arguments into a dictionary

#passing list as Argument
def show_fruits(fruits):
  for fruit in fruits:
    print(fruit)
show_fruits(["apple","banana","cherry"])
#list remains a list inside the function

#return statement
def multiply(x):
  return x*5
result=multiply(4)
print("Result :",result)

#return send value back to the function

#pass statement
def future_function():
  pass  
#function definition cannot be empty,pass used as placeholder

#lambda function
double=lambda x:x*2
print("Double of 5 is",double(10))
#small anonymous one line function