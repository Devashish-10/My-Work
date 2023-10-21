import pandas as pd
import numpy as np
import joblib 
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression,Lasso
from sklearn.metrics import accuracy_score
df=pd.read_csv=("C:/Users/Devashish Uniyal/OneDrive/Desktop/water_potability.csv")
df=df.dropna(axis=0,how="any",inplace=False)
print(df)
correlation_matrix=df.corr()
sns.heatmap(correlation_matrix,annot=True)
plt.show()
x=df[["ph","Hardness","Solids","Chloramines","Sulfate","Conductivity","Organic_carbon","Turbidity","Trihalomethanes"]]
y=df["Potability"]
y = y.values.ravel() 
threshhold=0.35
y=np.where(y>=threshhold,1,0)
x_train,x_test,y_train,y_test=train_test_split(x,y,train_size=0.75,random_state=42)
clf=LogisticRegression()
clf.fit(x_train,y_train)
ls=Lasso().fit(x_train,y_train)
y_pred=ls.predict(x_test)
AS=accuracy_score(y_test,y_pred)*100
print(AS)
filename='water_potability.joblib'
joblib.dump(clf,filename)
loaded_model=joblib.load(filename)
ph=float(input("Enter ph of water:"))
hardness=float(input("Enter hardness value of water:"))
solids=float(input("Enter solids value of water: "))
chloramines=float(input("Enter chloramines value present in water: "))
sulfates=float(input("Enter sulfates value present in water:"))
conductivity=float(input("Enter conductivity value present in the water: "))
organic_carbon=float(input("Enter organic carbon value present in the water:"))
turbidity=float(input("Enter turbidity value present in water:"))
trihalomethanes=float(input("Enter Triahalomethanes present in water:"))
user=[[ph,hardness,solids,chloramines,sulfates,conductivity,organic_carbon,turbidity,trihalomethanes]]
ls_predict=loaded_model.predict(user)
ls_predict=np.where(ls_predict>=threshhold,1,0)
if ls_predict==0:
    print("Not Suitanle for daily purpose")
else:
    print("Suitable for daily purpose")


