import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
data=pd.read_csv("C:/Users/HP/Desktop/Iris.csv")
data=data.drop("Id",1)
cols=["SepalLengthCm","SepalWidthCm","PetalLengthCm","PetalWidthCm"]
data.rename(columns={cols[0]:0,cols[1]:1,cols[2]:2,cols[3]:3},inplace=True)
colors={"Iris-setosa":"red","Iris-virginica":"blue","Iris-versicolor":"green"}
plt.scatter(
  data[0],
  data[2],
  c=data["Species"].map(colors))
plt.xlabel(cols[0])
plt.ylabel(cols[2])
plt.title("Iris Dataset Scatterplot")
plt.show()