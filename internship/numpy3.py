import numpy as np
import csv
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
print("First 10 Normalized Fare Values:\n")
print(normalized_fare[:10])
a.close()