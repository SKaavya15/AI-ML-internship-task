
import csv
import json
import numpy as np
import pandas as pd


# 1. READ CSV FILE AND PRINT FIRST 5 ROWS
# -------------------------------------------------

print("FIRST 5 ROWS OF DATASET\n")

a = open("dataset.csv", "r")

lines = a.readlines()

for i in range(6):
    print(lines[i])

a.close()



# 2. FILTER SURVIVED PASSENGERS
# -------------------------------------------------

a = open("dataset.csv", "r")

reader = csv.DictReader(a)

file = open("survivors.csv", "w", newline="")

fieldnames = reader.fieldnames

write = csv.DictWriter(file, fieldnames=fieldnames)

write.writeheader()

for row in reader:

    if row["Survived"] == "1":
        write.writerow(row)

print("\nSurvivors file created successfully")

a.close()
file.close()


# 3. CSV TO JSON
# -------------------------------------------------

f = open("dataset.csv", "r")

reader = csv.DictReader(f)

data = []

for r in reader:
    data.append(r)

json_file = open("dataset.json", "w")

json.dump(data, json_file, indent=4)

print("\nCSV converted to JSON successfully")

f.close()
json_file.close()

#NUMPY

# 4. NUMPY AGE ANALYSIS
# -------------------------------------------------

a = open("dataset.csv", "r")

reader = csv.DictReader(a)

ages = []

for row in reader:

    age = row["Age"]

    if age == "":
        ages.append(np.nan)

    else:
        ages.append(float(age))


age_col = np.array(ages)


mean_age = np.nanmean(age_col)


age_col = np.where(np.isnan(age_col), mean_age, age_col)


mean = np.mean(age_col)
median = np.median(age_col)
std = np.std(age_col)

print("\nAGE STATISTICS")
print("Mean :", mean)
print("Median :", median)
print("Standard Deviation :", std)

a.close()



# 5. AGE GROUP CLASSIFICATION
# -------------------------------------------------

groups = np.where(age_col < 18, "Child",
         np.where(age_col <= 60, "Adult", "Senior"))

child_count = np.sum(groups == "Child")
adult_count = np.sum(groups == "Adult")
senior_count = np.sum(groups == "Senior")

print("\nAGE GROUP COUNTS")
print("Child Count :", child_count)
print("Adult Count :", adult_count)
print("Senior Count :", senior_count)


# 6. NORMALISATION
# -------------------------------------------------

a = open("dataset.csv", "r")

reader = csv.DictReader(a)

fares = []

for row in reader:

    fare = row["Fare"]

    if fare == "":
        fares.append(np.nan)

    else:
        fares.append(float(fare))

fare_array = np.array(fares)

mean_fare = np.nanmean(fare_array)

fare_array = np.where(np.isnan(fare_array), mean_fare, fare_array)

min_value = np.min(fare_array)
max_value = np.max(fare_array)

normalized_fare = (fare_array - min_value) / (max_value - min_value)

print("\nFIRST 10 NORMALIZED FARE VALUES")
print(normalized_fare[:10])

a.close()

#PANDAS

# 7. LOAD DATASET USING PANDAS
# -------------------------------------------------

data = pd.read_csv("dataset.csv")

print("\nSHAPE OF DATASET")
print(data.shape)

print("\nCOLUMN NAMES")
print(data.columns)

print("\nDATA TYPES")
print(data.dtypes)

print("\nMISSING VALUES COUNT")
print(data.isnull().sum())



# 8. GROUP BY PASSENGER CLASS
# -------------------------------------------------

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

print("\nGROUPED DATA BY PCLASS")
print(result)



# -------------------------------------------------

data["FamilySize"] = data["SibSp"] + data["Parch"]

family_result = data.groupby("FamilySize")["Survived"].mean()

family_result = family_result.sort_values(ascending=False)

print("\nSURVIVAL RATE BY FAMILY SIZE")
print(family_result)



# 10. FILTER FIRST CLASS WOMEN
# -------------------------------------------------

filtered_data = data[

    (data["Sex"] == "female") &
    (data["Age"] >= 18) &
    (data["Age"] <= 35) &
    (data["Pclass"] == 1)

]

filtered_data.to_csv("first_class_women.csv", index=False)

print("\nFiltered first class women data exported successfully")
