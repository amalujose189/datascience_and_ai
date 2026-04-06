
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
df_dict=pd.DataFrame(data_list_dict)
df_dict

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