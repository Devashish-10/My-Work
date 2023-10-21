import pandas as pd
import numpy as np
import tensorflow as tf
from keras.models import Sequential
from keras.models import load_model 
from keras.layers import Dense
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/emails.csv")
data=data.dropna(axis=0,how="any",inplace=False)
x=data.iloc[:,1:3002].values
y=data[['Prediction']].values
model=Sequential()
model.add(Dense(128,activation='relu',input_dim=3001))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x,y,epochs=10,batch_size=128)
model.save("C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/PYTHON PROJECT/email_scam.pkl")
