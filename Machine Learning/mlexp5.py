import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
data = pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/iris.csv")
x=data[["sepal_length","sepal_width","petal_length","petal_width"]]
y=data["species"]
x_train_val,x_test,y_train_val,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
le=LabelEncoder()
y_train_val=le.fit_transform(y_train_val)
y_test=le.fit_transform(y_test)
clf=LogisticRegression()
clf.fit(x_train_val,y_train_val)
prediction=clf.predict(x_test)
print("Predcitions: ",prediction)
print(" Original: ",y_test)
AS=accuracy_score(y_test,prediction)
print("Accuracy Score: ",AS)
x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=0.25, random_state=42)
le=LabelEncoder()
y_train=le.fit_transform(y_train)
y_val=le.fit_transform(y_val)
clf2=LogisticRegression()
clf2.fit(x_train,y_train)
prediction2=clf2.predict(x_val)
AS2=accuracy_score(y_val,prediction2)
print(" Validation Accuracy Score: ",AS2)
Residual=AS-AS2
print("Residual errors in Validating model: ",Residual)
residuals=np.array(prediction2)-np.array(y_val)
plt.scatter(prediction2, residuals)
plt.axhline(y=0, color='r', linestyle='-')
plt.title('Residual Plot')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.show()
