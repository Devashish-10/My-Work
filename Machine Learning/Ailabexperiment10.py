from sklearn import datasets
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score
iris =datasets.load_iris()
x=iris.data
y=iris.target
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train)
y_pred=knn.predict(x_test)
cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix of knn Model  is: ",cm)
ac=accuracy_score(y_test,y_pred)*100
print("Accuracy of the knn Model is: ",ac)
LR=LogisticRegression()
LR.fit(x_train,y_train)
y_pred=LR.predict(x_test)
cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix of Logistic Regression Model   is: ",cm)
ac=accuracy_score(y_test,y_pred)*100
print("Accuracy of Logistic Regression Model is: ",ac)
svm=make_pipeline(StandardScaler(),SVC())
svm.fit(x_train,y_train)
y_pred=svm.predict(x_test)
cm=confusion_matrix(y_test,y_pred)
print("Confusion matrix of SVM Model   is: ",cm)
ac=accuracy_score(y_test,y_pred)*100
print("Accuracy of SVM Model is: ",ac)
