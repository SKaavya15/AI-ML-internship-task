import numpy as np
import csv
a=open("dataset.csv","r")
r=csv.DictReader(a)
ages=[]
for i in r:
    age=i["Age"]
    if age =="":
        ages.append(np.nan)
    else:
        ages.append(float(age))
age_col=np.array(ages)
mean_age=np.nanmean(age_col)
age_col=np.where(np.isnan(age_col),mean_age,age_col)
mean = np.mean(age_col)
median = np.median(age_col)
std = np.std(age_col)
print("Mean :", mean)
print("Median :", median)
print("Standard Deviation :", std)