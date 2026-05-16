# Titanic Dataset Analysis using Python

## Overview

This project performs data analysis on the Titanic dataset using Python libraries such as:

* `csv`
* `json`
* `NumPy`
* `Pandas`

The program demonstrates:

* CSV file handling
* Data filtering
* CSV to JSON conversion
* Statistical analysis using NumPy
* Data grouping and filtering using Pandas

---

## Features

### 1. Read CSV File

* Reads the Titanic dataset (`dataset.csv`)
* Prints the first 5 rows of the dataset

### 2. Filter Survived Passengers

* Extracts passengers who survived
* Saves them into a new file:

  * `survivors.csv`

### 3. Convert CSV to JSON

* Converts the CSV dataset into JSON format
* Creates:

  * `dataset.json`

### 4. NumPy Age Analysis

Performs statistical analysis on the `Age` column:

* Mean
* Median
* Standard Deviation

Missing age values are replaced with the mean age.

### 5. Age Group Classification

Classifies passengers into:

* Child (<18)
* Adult (18–60)
* Senior (>60)

Displays count of each group.

### 6. Fare Normalization

Normalizes the `Fare` column using Min-Max Normalization formula:

x_{norm} = \frac{x - x_{min}}{x_{max} - x_{min}}

Prints the first 10 normalized fare values.

### 7. Pandas Dataset Analysis

Displays:

* Dataset shape
* Column names
* Data types
* Missing values count

### 8. Group By Passenger Class

Groups data by passenger class (`Pclass`) and calculates:

* Average survival rate
* Mean age
* Mean fare

### 9. Survival Rate by Family Size

Creates a new column:

* `FamilySize = SibSp + Parch`

Calculates survival rate based on family size.

### 10. Filter First Class Women

Filters:

* Female passengers
* Age between 18 and 35
* First class passengers

Exports result to:

* `first_class_women.csv`

---

## Technologies Used

* Python
* NumPy
* Pandas
* CSV Module
* JSON Module

---

## Files Generated

| File Name               | Description                            |
| ----------------------- | -------------------------------------- |
| `survivors.csv`         | Contains survived passengers           |
| `dataset.json`          | JSON version of dataset                |
| `first_class_women.csv` | Filtered first-class female passengers |

---

## Requirements

Install required libraries before running:

```bash
pip install numpy pandas
```

---

## How to Run

1. Place `dataset.csv` in the project folder.
2. Run the Python file:

```bash
python filename.py
```

---

## Learning Outcomes

This project helps understand:

* File handling in Python
* CSV and JSON processing
* NumPy statistical operations
* Handling missing values
* Data normalization
* Data analysis using Pandas
* Grouping and filtering datasets

---

## Sample Dataset

This project uses the famous Titanic dataset containing passenger details such as:

* Age
* Gender
* Passenger class
* Fare
* Survival status

---

## Conclusion

This project is a beginner-friendly data analysis project that combines Python fundamentals with practical data science concepts using NumPy and Pandas.
