import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[5,9,2,7,10]
plt.plot(x,y)
plt.xlabel("Days")
plt.title("Daily Sales")
plt.show()

x=[1,2,3,4,5]
plt.subplot(1,2,1)
plt.plot(x,[i*i for i in x]) #squares
plt.subplot(1,2,2)
plt.plot(x,[i*i*i for i in x])
plt.show()#cubes


x=[10,20,30,40,50]
y=[15,25,35,30,45]
plt.scatter(x,y)
plt.xlabel("Age")
plt.ylabel("income")
plt.title("age vs income")
plt.show()

x=[10,20,30,40,50]
y=[15,25,35,30,45]
sizes=[100,200,300,250,150]
plt.scatter(x,y,s=sizes,alpha=0.5)
plt.title("Bubble chart")
plt.show()

days=["mon","tue","wed","thu","fri"]
sales=[120,100,160,140,200]
plt.bar(days,sales)
plt.title("sales by day")
plt.show()

marks=[10,20,30,40,20,30,10,50,60,70,20,30,40]
plt.hist(marks,bins=5)
plt.title("student marks distribution")
plt.show()


categories=['A','B','C','D']
values=[30,20,25,25]
plt.pie(values,labels=categories,autopct="%0.1f%%")# autopct to display values after decimal and % symbol
plt.show()

import pandas as pd
df=pd.read_csv("iris.csv")
print(df)

plt.plot(df.index,df['SepalLengthCm'])
plt.title("Sepal Length Trend")
plt.xlabel("index")
plt.ylabel("Sepal Length")
plt.show()
