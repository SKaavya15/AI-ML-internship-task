import pandas as pd


data = pd.read_csv("dataset.csv")


print("Shape of Dataset:")
print(data.shape)


print("\nColumn Names:")
print(data.columns)


print("\nData Types:")
print(data.dtypes)


print("\nMissing Values Count:")
print(data.isnull().sum())