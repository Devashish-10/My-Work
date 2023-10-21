import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.model_selection import train_test_split
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/iris.csv")
data=data.dropna(axis=0,how="any",inplace=False)
print(data.shape)
x=data[["sepal_length","sepal_width","petal_length","petal_length"]]
y=data["species"]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8)
clf=DecisionTreeClassifier()
clf.fit(x_train,y_train)
prediction=clf.predict(x_test)
print("Predictions: ",prediction)
print("Original :",y_test)
AS=accuracy_score(y_test,prediction)
print("Accuracy Score: ",AS)
CS=confusion_matrix(y_test,prediction)
print("Confusion matrix:\n ",CS)
