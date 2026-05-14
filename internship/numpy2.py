import numpy as np
import csv

# Open CSV file
a = open("dataset.csv", "r")

# Read CSV data
reader = csv.DictReader(a)

# Store age values
ages = []

# Extract Age column
for row in reader:

    age = row["Age"]

    # Handle missing values
    if age == "":
        ages.append(np.nan)

    else:
        ages.append(float(age))

# Convert list into NumPy array
age_array = np.array(ages)

# Calculate mean age ignoring NaN
mean_age = np.nanmean(age_array)

# Replace NaN values with mean age
age_array = np.where(np.isnan(age_array), mean_age, age_array)

# Create age group classification
groups = np.where(age_array < 18, "Child",
         np.where(age_array <= 60, "Adult", "Senior"))

# Count each group
child_count = np.sum(groups == "Child")
adult_count = np.sum(groups == "Adult")
senior_count = np.sum(groups == "Senior")

# Print results
print("Child Count :", child_count)
print("Adult Count :", adult_count)
print("Senior Count:", senior_count)

# Close file
a.close()