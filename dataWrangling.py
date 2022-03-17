import csv
import pandas as pd
import random

kaggleData = open('StateNames.csv')

#define list to hold names
nameList = []

reader = csv.DictReader(kaggleData)

for row in reader:
    if row['State'] == 'HI':
        nameList.append(row['Name'])

kaggleData.close()

df = pd.read_excel('hawaiianGivenname.xlsx')

gatheredList = df.values.tolist()

nameList += gatheredList
columnNames = ['Name', 'freq']
rowNames = []
for name in nameList:
    rowNames.append([name, random.randint(1,48)])

with open('hawaiianFirstNames.csv', 'w', encoding="utf-8") as f:
    write = csv.writer(f) 
    write.writerow(columnNames) 
    write.writerows(rowNames)

        
