import pandas as pd


data = pd.read_csv("dataset.csv")
filtered_data = data[
    
    (data["Sex"] == "female") &
    (data["Age"] >= 18) &
    (data["Age"] <= 35) &
    (data["Pclass"] == 1)

]
filtered_data.to_csv("first_class_women.csv", index=False)

print("Filtered data exported successfully")