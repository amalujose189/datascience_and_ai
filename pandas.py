
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
