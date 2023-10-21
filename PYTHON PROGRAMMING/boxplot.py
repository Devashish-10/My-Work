import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data=pd.read_csv("C:/Users/HP/Desktop/Iris.csv")
data=data.drop("Id",1)
cols=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
data.rename(columns={cols[0]:0,cols[1]:1,cols[2]:2,cols[3]:3},inplace=True)
plt.boxplot([data[0],data[1],data[2],data[3]])
plt.show()
plt.boxplot(columns=[0],by=["Species"])
plt.show() 
