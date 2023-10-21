import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/emails.csv")
data=data.dropna(axis=0,how="any",inplace=False)
x=data.iloc[:,1:3002]
y=data[["Prediction"]]
print(y.value_counts())
y=y.values.ravel()
class_weights={c:1 if c == 'no' else 2.5 for c in y}
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3,random_state=42)
clf=svm.SVC(class_weight=class_weights)
clf.fit(x_train,y_train)
y_predict=clf.predict(x_test)
AS=accuracy_score(y_test,y_predict)
print(AS)