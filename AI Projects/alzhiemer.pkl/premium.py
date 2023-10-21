import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error
from  sklearn.ensemble import RandomForestRegressor
df=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/Medicalpremium.csv")
def remove_outliers(data,column,threshold =1.5):
     Q1=data[column].quantile(0.25)
     Q3=data[column].quantile(0.75)
     IQR=Q3-Q1
     lower_bound=Q1-(threshold*IQR)
     upper_bound=Q3+(threshold*IQR)
     return data[((data[column])>=lower_bound) & ((data[column])<=upper_bound)]
data=remove_outliers(df,"PremiumPrice")
data=data.dropna(axis=0,how="any",inplace=False)
x=data.iloc[:,0:10]
y=data[["PremiumPrice"]]
y=y.values.ravel()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
print(x.shape,y.shape)
reg=KNeighborsRegressor()
reg.fit(x_train,y_train)
y_predict=reg.predict(x_test)
rf_reg = RandomForestRegressor(random_state=42)
rf_reg.fit(x_train, y_train)
y_predict_rf = rf_reg.predict(x_test)
MAE=mean_absolute_error(y_test,y_predict_rf)
MSE=mean_squared_error(y_test,y_predict_rf)
print("Mean Absolute Error: ",MAE)
print("Mean Squared Error: ",MSE)


