import csv
a=open("dataset.csv","rt")
lines=a.readlines()
for i in range(6):
    print(lines[i])

