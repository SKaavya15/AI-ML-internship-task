import csv
a=open("dataset.csv","rt")
reader=csv.DictReader(a)
file=open("survivors.csv","w")
fieldnames=reader.fieldnames
write=csv.DictWriter(file,fieldnames=fieldnames)
write.writeheader()
for row in reader:
    if row["Survived"]=="1":
        write.writerow(row)
print("created successfully")