import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/mushrooms.csv")
le=LabelEncoder()
for i in data.columns:
    data[i]=le.fit_transform(data[i])
x = data.iloc[:, 1:]
y = data[['class']]
y=y.values.ravel()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.8)
best_n = 0
best_score = 0
for n in range(1,30):
     knn = KNeighborsClassifier(n_neighbors=n)
     knn.fit(x_train, y_train)
     y_pred = knn.predict(x_test)
     score = accuracy_score(y_test, y_pred)
     if score > best_score:
         best_n = n
         best_score = score
print("Best value for n nearest neighbors: ",best_n)
print("Accuracy Score: ",best_score)


