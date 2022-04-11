import csv
import pandas as pd
import random

kaggleData = open('StateNames.csv')

#define list to hold names
nameList = []

#read in data from kaggle
reader = csv.DictReader(kaggleData)

#take unique names from the state of HI
for row in reader:
    if row['State'] == 'HI' and row['Name'] not in nameList:
        nameList.append(row['Name'])

kaggleData.close()

#read in data that teammates gathered
df = pd.read_excel('hawaiianGatheredNames.xlsx')

gatheredList = df.values.tolist()

#join the names together, ensuring they are unique and also clean the data
for name in gatheredList:
    if name not in nameList:
        nameList.append(name)
    elif name[0] == '[':
        name = name[1:-1]
        nameList.append(name)

#output list of names to csv
columnNames = ['Name']
rowNames = []
for name in nameList:
    rowNames.append([name])

with open('hawaiianFirstNames.csv', 'w', encoding="utf-8", newline = '') as f:
    write = csv.writer(f) 
    write.writerow(columnNames) 
    write.writerows(rowNames)

        
