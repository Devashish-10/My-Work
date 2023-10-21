from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report,confusion_matrix
iris =datasets.load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
LR=LogisticRegression()
LR.fit(x_train,y_train)
pred=LR.predict(x_test)
print("The accuracy of the Logistic regression model is:", LR.score(x_test,y_test)*100,"%")
print(classification_report(y_test,pred))
