import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/iris.csv")
x = data[["sepal_length","sepal_width","petal_length","petal_width"]] 
y = data["species"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25,random_state=0)
x_train = sm.add_constant(x_train)
le=LabelEncoder()
y_train2=le.fit_transform(y_train)
y_test2=le.fit_transform(y_test)
model = sm.OLS(y_train2, x_train).fit()
print(model.summary())
x_test = sm.add_constant(x_test)
y_predict=model.predict(x_test)
y_test=y_test.values.reshape(-1,1)
y_predict=y_predict.values.reshape(-1,1)
print(x_test.shape)
print(y_test.shape)
mse=mean_squared_error(y_test2,y_predict)
print("Mean Squared Error: ",mse)

