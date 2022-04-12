import csv
import pandas as pd
import numpy as np

namesFile = open('zipcodes.csv', 'r', encoding='utf-8')
reader = csv.DictReader(namesFile)
print(reader.fieldnames)
nameList = []
for row in reader:
    nameList.append(row['\ufeffZip Code'])

a = 2.0
#using userLength as the number of names, casting as int to run function
# np.random.zipf is the function that generates the numbers
zNum = np.random.zipf(a, len(nameList))


i = 0
columnNames = ['Name', 'freq']
rowNames = []
for name in nameList:
    rowNames.append([name, zNum[i]])
    i = i + 1

with open("zipcodes-freq.csv", 'w', encoding="utf-8", newline = '') as subFile:  #Max's Code
    write = csv.writer(subFile)
    write.writerow(columnNames)
    write.writerows(rowNames)

#Close subFile
subFile.close()
