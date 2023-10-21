import numpy as np
import pandas as pd
import tensorflow as tf
from keras.layers import Dense
from keras.models import Sequential
from keras.models import load_model
from keras.optimizers import Adam
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/Gemstone Price Predictor/cubic_zirconia.csv")
def remove_outliers(data,column,threshold =1.5):
     Q1=data[column].quantile(0.25)
     Q3=data[column].quantile(0.75)
     IQR=Q3-Q1
     lower_bound=Q1-(threshold*IQR)
     upper_bound=Q3+(threshold*IQR)
     return data[((data[column])>=lower_bound) & ((data[column])<=upper_bound)]
data=remove_outliers(data,"price")
data=data.dropna(axis=0,how="any",inplace=False)
correlation_threshold=0.4
correalation_with_dependent_variable=data.corr()["price"]
features_selected=correalation_with_dependent_variable[abs(correalation_with_dependent_variable) > correlation_threshold]
print("Selected features are:",features_selected)
data=pd.get_dummies(data,columns=["cut","color","clarity"])
x=data.iloc[:,:9].values
y=data[['price']].values
model=Sequential()
model.add(Dense(64,activation='relu',input_dim=9))
model.add(Dense(1,activation='linear'))
model.compile(optimizer=Adam(learning_rate=0.001),loss='mean_squared_error',metrics=['mse'])
model.fit(x,y,epochs=20,batch_size=128)
model.save("C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/ML_Models/gemstone_price_predictor.pkl")
print("Model Saved")
loaded_model=load_model("C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/ML_Models/gemstone_price_predictor.pkl")
carat=float(input("Enter carat weight of the cubic zirconia:"))
cut=input("Describe the cut quality Fair,Good,Very Good,Premium,Ideal:")
color=input("Colour of the cubic zirconia.With D being the best and J the worst.")
clarity=input("Cubic zirconia Clarity refers to the absence of the Inclusions and Blemishes. (In order from Best to Worst, FL = flawless, I3= level 3 inclusions) FL, IF, VVS1, VVS2, VS1, VS2, SI1, SI2, I1, I2, I3")
depth=float(input("The Height of a cubic zirconia, measured from the Culet to the table, divided by its average Girdle Diameter."))
table=float(input("The Width of the cubic zirconia's Table expressed as a Percentage of its Average Diameter."))
X=float(input("Length of the cubic zirconia in mm."))
Y=float(input("Width of the cubic zirconia in mm."))
Z=float(input("Height of the cubic zirconia in mm."))
user_input=[[carat,cut,color,clarity,depth,table,X,Y,Z]]
user_input=pd.DataFrame(user_input)
user_input=pd.get_dummies(user_input,columns=["cut","color","clarity"])
prediction=loaded_model.predict(user_input)
print("The value of gemstone is : ",prediction[0][0])
