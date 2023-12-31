import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import joblib 
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/diabetes_prediction_dataset.csv")
data=data.dropna(axis=0,how='any',inplace=False)
data=pd.get_dummies(data,columns=["gender","smoking_history"])
x=data.iloc[:,0:8]
y=data[["diabetes"]]
y=y.values.ravel()
CR=data.corr()
sns.heatmap(CR,annot=True)
plt.show()
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=42)
clf=svm.SVC()
clf.fit(x_train,y_train)
y_predict=clf.predict(x_test)
AS=accuracy_score(y_test,y_predict)
print(AS)
filename='diabetes_model.pkl'
with open(filename,'wb') as file:
      joblib.dump(clf,file)
loaded_model=joblib.load(filename)
gender=int(input("Enter 1 for female and 0 for male:"))
age=int(input("Enter your age:"))
hypertension=int(input("Enter 1 if patient have hypertension else 0:"))
heart_disease=int(input("Enter 1 if patient have heart disease:"))
smoking=int(input("Enter 1 if patient smoke else 0:"))
bmi=float(input("Enter patients BMI:"))
hb1ac=float(input("Enter patient Hb1ac status:"))
blood_glucose=int(input("Enter patient blood glucose level:"))
user_input=[[gender,age,hypertension,heart_disease,smoking,bmi,hb1ac,blood_glucose]]
prediction=loaded_model.predict(user_input)
if prediction == 1:
      print("Patient has diabetes")
else:
      print("Patient does not have diabetes")