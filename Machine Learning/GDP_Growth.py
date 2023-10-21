import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error,mean_squared_error
df=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/India_GDP_1960-2022.csv")
x=df.iloc[:,1:4]
y=df[["Growth %"]]
plt.plot(x,y)
plt.show()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
LR=LinearRegression()
LR.fit(x_train,y_train)
y_predict=LR.predict(x_test)
plt.scatter(y_test,y_predict)
plt.xlabel("Predicted Gdp")
plt.ylabel("Actual Gdp")
plt.show()
mse=mean_squared_error(y_test,y_predict)
mae=mean_absolute_error(y_test,y_predict)
print("MSE:",mse)
print("MAE:",mae)