import csv
import json
f=open("dataset.csv","r")
reader=csv.DictReader(f)
data=[]
for r in reader:
    data.append(r)
a=open("dataset.json","w")
json.dump(data,a,indent=4)
print("converted")