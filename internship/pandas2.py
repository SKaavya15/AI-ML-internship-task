import pandas as pd


data = pd.read_csv("dataset.csv")


result = data.groupby("Pclass").agg({

    "Survived": "mean",
    "Age": "mean",
    "Fare": "mean"

})

result.columns = [

    "Average Survival Rate",
    "Mean Age",
    "Mean Fare"

]

# Display result
print(result)