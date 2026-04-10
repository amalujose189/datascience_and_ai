
'''
 ModelBuilding 
 ModelEvaluation
  Prediction/Testing 
 Deployment
  MonitoringandMaintenance
  DocumentationandReporting

a pandas dataframe is a 2 dimensiona data structure ,like a 2 dimensional array or a table with rows and columns

'''
import pandas as pd
data={
    "name":["amal","binu","charles","ajh"],
    "age":[50,None,45,45],
    "city":["delhi","mumbai","chennai","htt"]


}
df_dict=pd.DataFrame(data)
df_dict

#creating a dataframe from a list of dictionaries
data_list_dict=[
    
    { "Name":"John","Age":30,"city":"pune"} ,
    { "Name":"Priya","Age":28,"city":"Bangalore"} ,
    { "Name":"Ali","Age":35,"city":"Hyderabad"}   
]
df_list_dict=pd.DataFrame(data_list_dict)
df_list_dict

#creating a dataframe from a numpy array
import numpy as np
arr=np.array([[1,"Laptop",45000],
[2,"Mouse",500],
[3,"Keyboard",1500]])
print(arr)
df_np=pd.DataFrame(arr,columns=["ID","Product","Price"])
df_np

import pandas as pd 
df4=pd.DataFrame({
    "Name":["John","Priya","Alex","Sara"],
    "Age":[25,30,22,28],
    "city":["Delhi","Chennai","Mumbai","pune"]
},
index=["a","b","c","d"]
)
df4
#using loc  we can acces using names
df4.loc["b"]
#selecting multiple rows
df4.loc[["a","d"]] #multiple rows
df4.loc["b","Age"] #rows and column


df4.loc[["a","c"],["Name","city"]] #multiple rows and columns
#slicing
df4.loc["a":"c"]

df4.loc[df4['Age']>25]
#iloc
#select a single row by number
df4.iloc[1]
#row 1 --->priya
#select multiple rows
df4.iloc[[0,2]]

#select row+column by number
df4.iloc[1,1] #age of row 1 
#30
#row ^ & column slicing
df4.iloc[0:3,0:2] #rows 0 t0 2,column 0 t0 1
df_dict.shape

df_dict.shape

df_dict.index
df_dict.dtypes
df_dict.describe()#summary -mean ,count,standard deviation,min,max,iqr  range  ,25 % ,75%,50% below data in box plot
#apply only to numerical values
df_dict.info()#to check the non null count
#adding new columns
df_dict["salary"]=[50000,60000,55000,60000]
df_dict

new_row={"Name":"Sara","Age":32,"City":"Pune","Salary":5200}
df_dict.loc[len(df_dict)]=new_row
df_dict

df_dict.drop("salary",axis=1) # remove column
df_dict.drop(4,axis=0)# remove rows

#for multiple row df_dict.drop([4,5],axis=0)
df_dict["age"].mean()
df_dict["age"].median()
df_dict["age"].mode()

#aggregation
df_dict.agg({"Age":["mean","min","max","std"]})# also by describe
df_dict.isnull() #checking null values
df_dict.isnull().sum()
#find the total null values
#df_dict.dropna() #remove rows of null values
#df_dict.dropna(axis=1)
#drop columns with nulls

df_dict.fillna(0) #fill the null values with 0

df_med=df_dict.copy()
df_med["age"].fillna(df_med["age"].mean(),inplace=True)
df_med["age"].fillna(df_med["age"].median(),inplace=True)#do this seperately
df_med["age"].fillna(df_med["age"].mode(),inplace=True)

z=df_dict["age"].mode()
print(type(z))
#mode will store as series of data .it is not recommend
df_c=pd.DataFrame(
    {
        "col1":[10,None,30,50],
        "col2":[None,,None,15,None]

    }
)
print("Forward Fill:")#fill with before row value
print(df_c.ffill())
print("Backward fill")
print(df_c.bfill())
df_c


#binding in data manipulation means combining multiple datasets
#three methods are concatenation ,merging and join
#row wise concatenation
import pandas as pd 
df1=pd.DataFrame({
    "Name":["John","Priya"],
    "Age":[25,30]

})
df2=pd.DataFrame({
    "Name":["Alex","Sara"],
    "Age":[22,28]
})
result=pd.concat([df1,df2],axis=0)
print(result)
#it will combine dataframes

#column wise concatenation
df3=pd.DataFrame({"City":["Delhi","Chennai","Mumbai","Pune"]})
result1=pd.concat([df1,df3],axis=1)
print(result1)

#merging using common "ID" column
dfA=pd.DataFrame({
    "ID":[1,2,3],
    "Name":["John","Priya","Alex"]

})
dfB=pd.DataFrame({
    "ID":[1,2,4],
    "Salary":[50000,60000,55000]

})
result=pd.merge(dfA,dfB,on="ID",how="inner")
result

#left join
pd.merge(dfA,dfB,on="ID",how="left")

#right join
pd.merge(dfA,dfB,on="ID",how="right")


#join function same like merge
dfA=pd.DataFrame({
    "Name":["John","Priya","Alex"]
},index=[1,2,3])

dfB=pd.DataFrame({
    "Salary":[50000,60000,55000]

},index=[1,2,4])
df_join=dfA.join(dfB,how="left")
df_join

