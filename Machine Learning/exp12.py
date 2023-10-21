import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew,kurtosis
data=pd.read_excel("C:/Users/Devashish Uniyal/OneDrive/Desktop/HousingData.xlsx")
print("Summary: ")
print(data.describe())
print("--"*75)
print("Skewness: ",skew(data,axis=0,bias=True))
print("Kurtosis: ",kurtosis(data,axis=0,bias=True))
print("--"*75)
print("Maximum Value: ",data.max(axis='columns'))
print("Minimum Value: ",data.min(axis='columns'))
print("--"*75)
correlation_matrix=data.corr()
sns.heatmap(correlation_matrix,annot=True)
plt.show()
print("Correlation: ")