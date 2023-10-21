import joblib
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/calorieburnedcounter.csv")
def remove_outliers(data,column,threshold=1.5):
     Q1=data[column].quantile(0.25)
     Q3=data[column].quantile(0.75)
     IQR=Q3-Q1
     lower_bound=Q1 - (threshold*  IQR)
     upper_bound=Q3 + (threshold*IQR)
     return data[(data[column]>=lower_bound) & (data[column]<=upper_bound)]
data=remove_outliers(data,"Calories")
data=data.dropna(axis=0,how='any',inplace=False)
x=data.iloc[:,:12]
y=data[['Calories']]
y=y.values.ravel()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
calclf=LinearRegression()
calclf.fit(x_train,y_train)
y_pred=calclf.predict(x_test)
for i in range(0,278):
     print((y_test[i]," ----------- ",y_pred[i] ))
MSE=mean_squared_error(y_test,y_pred)
print(MSE)
filename='calories_burned_model.joblib'
joblib.dump(calclf,filename)
load_calclf=joblib.load(filename)
tsteps=int(input("Enter Total steps walked:"))
tdist=int(input("Enter total distance covered:"))
trackerdist=int(input("Enter tracker distance recorded:"))
logged_activity_distance=int(input("Enter logged activity distance:"))
vactive_dist=int(input("Enter distance you travelled very actively:"))
mactive_dist=int(input("Enter distance you travelled moderately active:"))
lactive_dist=int(input("Enter distance you travelled lightly active:"))
sactive_dist=int(input("Enter distance you travelled sedenteraly active:"))
vactive_min=int(input("Enter the time limit in which you travlled very actively:"))
factive_min=int(input("Enter the time limit in which you were fairly active:"))
lactive_min=int(input("Enter lightly active duration:"))
sactive_min=int(input("Enter the duration in which you were sedenterely active:"))
user_input=[[tsteps,tdist,trackerdist,logged_activity_distance,vactive_dist,mactive_dist,lactive_dist,sactive_dist,vactive_min,factive_min,lactive_min,sactive_min]]
prediction=load_calclf.predict(user_input)
print("You burned approximately:",prediction)
