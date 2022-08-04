import csv

fileContents = open('hawaiianstreetnames.csv', encoding="utf-8")

#define list to hold names
nameList = []

#read in data from csv
reader = csv.DictReader(fileContents)

print(reader.fieldnames)

#take unique values (just in case of duplicates)
for row in reader:
    if row['\ufeffName'] not in nameList:
        nameList.append(row['\ufeffName'])

fileContents.close()

cleanedList = []

for name in nameList:
    if name.isalpha():
        cleanedList.append(name)

#output list of names to csv
columnNames = ['Name']
rowNames = []
for name in cleanedList:
    rowNames.append([name])

with open('hawaiianstreetnames2.csv', 'w', encoding="utf-8", newline = '') as f:
    write = csv.writer(f) 
    write.writerow(columnNames) 
    write.writerows(rowNames)
