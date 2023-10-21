import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.metrics import mean_squared_error
data = pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/iris.csv")
x = data[["sepal_length","sepal_width","petal_length","petal_width"]] 
y = data["species"]
x = sm.add_constant(x)
model = sm.OLS(y, x).fit()
print(model.summary())
