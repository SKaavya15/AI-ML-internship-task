import pandas as pd
data = pd.read_csv("dataset.csv")
data["FamilySize"] = data["SibSp"] + data["Parch"]
result = data.groupby("FamilySize")["Survived"].mean()
result = result.sort_values(ascending=False)
print(result)