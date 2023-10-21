import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression,Lasso,Ridge
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error 
from sklearn.preprocessing import StandardScaler
data=pd.read_excel("C:/Users/Devashish Uniyal/OneDrive/Desktop/HousingData.xlsx")
def remove_outliers(data,column,threshold =1.5):
     Q1=data[column].quantile(0.25)
     Q3=data[column].quantile(0.75)
     IQR=Q3-Q1
     lower_bound=Q1-(threshold*IQR)
     upper_bound=Q3+(threshold*IQR)
     return data[((data[column])>=lower_bound) & ((data[column])<=upper_bound)]
data=remove_outliers(data,"MEDV")
data=data.dropna(axis=0,how="any",inplace=False)
x=data.iloc[:,0:14]
y=data[["MEDV"]]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8)
reg=LinearRegression()
reg.fit(x_train,y_train)
prediction=reg.predict(x_test)
print("Without Regularization")
print("Mean Absolute Error: ",mean_absolute_error(y_test,prediction))
print("Mean Squared Error",mean_squared_error(y_test,prediction))
print("With Regularization")
ls=Lasso().fit(x_train,y_train)
ls_predict=ls.predict(x_test)
rd=Ridge().fit(x_train,y_train)
rd_predict=rd.predict(x_test)
print("Mean Squared Error after Lasso: ",mean_squared_error(y_test,ls_predict))
print("Mean Absolute Error after Lasso: ",mean_absolute_error(y_test,ls_predict))
print("Mean Squared Error after Ridge: ",mean_squared_error(y_test,rd_predict))
print("Mean Absolute Error after Ridge: ",mean_absolute_error(y_test,rd_predict))

