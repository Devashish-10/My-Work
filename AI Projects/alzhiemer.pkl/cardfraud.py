import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.models import load_model
from keras.layers import Dense 
data=pd.read_csv("C:/Users/Devashish Uniyal/OneDrive/Desktop/Datasets/card_transdata.csv")
x=data.iloc[:,:7]
y=data[["fraud"]]
model=Sequential()
model.add(Dense(64,activation='relu',input_dim=7))
model.add(Dense(1,activation='sigmoid'))
model.compile(optimizer='rmsprop',loss='binary_crossentropy',metrics=['accuracy'])
model.fit(x,y,epochs=10,batch_size=128)
model.save('C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/ML_Models/cardfraud.pkl')
print("Model Saved")
loaded_model=load_model('C:/Users/Devashish Uniyal/OneDrive/Desktop/coding/ML_Models/cardfraud.pkl')
print("Model Loaded")
dist_card_used=float(input("Enter the distance at which the card is used:\n"))
dist_last_transaction=float(input("Enter the distance from last transaction the card was used:\n"))
median_purchase=float(input("Enter the median amount you spent while shopping:\n"))
amt=float(input("Enter the amount the card user spent:\n"))
ratio_to_median_purchase=float(amt)/float(median_purchase)
repeat_retailer=float(input("Does the transcation has a repeated retailer if yes enter 1 and if no enter 0:\n"))
chip=float(input("Was the chip used while transaction if yes enter 1 and if no enter 0: :\n"))
paym=float(input("Did the pin was enterd to make the transaction if yes enter 1 and if no enter 0::\n"))
order_type=float(input("Was an online order places using the card if yes enter 1 and if no enter 0::\n"))
user_input=[[dist_card_used,dist_last_transaction,ratio_to_median_purchase,repeat_retailer,chip,paym,order_type]]
prediction=loaded_model.predict(user_input)
if prediction==1:
               print("Transaction at risk")
else :
                print("No risk in transaction")


