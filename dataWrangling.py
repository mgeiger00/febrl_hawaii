import csv
import pandas as pd
import random

kaggleData = open('StateNames.csv')

#define list to hold names
nameList = []

reader = csv.DictReader(kaggleData)

for row in reader:
    if row['State'] == 'HI' and row['Name'] not in nameList:
        nameList.append(row['Name'])

kaggleData.close()

df = pd.read_excel('hawaiianGatheredNames.xlsx')

gatheredList = df.values.tolist()

for name in gatheredList:
    if name not in nameList:
        nameList.append(name)
columnNames = ['Name', 'freq']
rowNames = []
for name in nameList:
    rowNames.append([name, random.randint(1,48)])

with open('hawaiianFirstNames.csv', 'w', encoding="utf-8", newline = '') as f:
    write = csv.writer(f) 
    write.writerow(columnNames) 
    write.writerows(rowNames)

        
