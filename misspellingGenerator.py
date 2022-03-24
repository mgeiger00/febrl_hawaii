import string
import random
import csv

#create function to misspell words based on letters nearby chosen letter on keyboard
def createMisspelling(word):
    letterDict = {'a':['s','q','z','w'], 'b':['v','n','g','h'], 'c':['x','v','d','f'], 'd':['s','f','e','r','c'], 'e':['w','d','r'],
                  'f':['d','g','r','v','c'], 'g':['f','h','t','b','v'],'h':['g','j','y','b','n'],'i':['u','o','k'], 'j':['h','k','u','m','n'],
                  'k':['j','l','i','m'], 'l':['k','o','p'], 'm':['n','j','k'], 'n':['b','m','h','j'], 'o':['i','p','l'], 'p':['o','l'],
                  'q':['w','a'],'r':['e','t','f'], 's':['a','d','w','x','z'], 't':['r','y','g','f'], 'u':['y','i','j'], 'v':['c','b','f','q'],
                  'w':['q','e','s'], 'x':['z','c','s','d'], 'y':['t','u','h'], 'z':['x','a','s'], 'A':['S','Q','Z','W'], 'B':['V','N','G','H'], 'C':['X','V','D','F'], 'D':['S','F','E','R','C'], 'E':['W','D','R'],
                  'F':['D','G','R','V','C'], 'G':['F','H','T','B','V'],'H':['G','J','Y','B','N'],'I':['U','O','K'], 'J':['H','K','U','M','N'],
                  'K':['J','L','I','M'], 'L':['K','O','P'], 'M':['N','J','K'], 'N':['B','M','H','J'], 'O':['I','P','L'], 'P':['O','L'],
                  'Q':['W','A'],'R':['E','T','F'], 'S':['A','D','W','X','Z'], 'T':['R','Y','G','F'], 'U':['Y','I','J'], 'V':['C','B','F','Q'],
                  'W':['Q','E','S'], 'X':['Z','C','S','D'], 'Y':['T','U','H'], 'Z':['X','A','S'], '1':['2'], '2':['1','3'], '3':['2','4'],
                  '4':['3','5'], '5':['4','6'], '6':['5','7'], '7':['6','8'], '8':['7','9'], '9':['8','0'], '0':['9']}
    chosenLetter = random.choice(range(len(word)))
    #weird case caused by okina
    if ((word[chosenLetter] != '[') and (word[chosenLetter] != ']') and(word[chosenLetter] != ' ')):
        misspelledWord = word[:chosenLetter] + random.choice(letterDict[word[chosenLetter]]) + word[chosenLetter + 1:]
    return misspelledWord                                          
    
                        

namesFile = open('hawaiianFirstNames.csv', 'r', encoding='utf-8')

reader = csv.DictReader(namesFile)

#list of names
nameList = []

for row in reader:
    #weird case caused by okina
    if row['Name'][0] != '[' and row['Name'] not in nameList:
        nameList.append(row['Name'])

namesFile.close()

misspellingsDict = {}
#nameList = ['Max', 'Mia', 'Pona', 'Kana', 'Gerald', 'Hansel', 'Gretel']

#make random number of misspellings (1-3) for each name
for name in nameList:
    numOfMisspellings = random.randrange(1,3)
    for i in range(numOfMisspellings):
        if name not in misspellingsDict:
            misspellingsDict[name] = []
            misspellingsDict[name].append(createMisspelling(name))
        else:
            misspellingsDict[name].append(createMisspelling(name))

with open('firstname-misspell.csv', 'w') as csvfile:   
    writer = csv.writer(csvfile)
    key_list = list(misspellingsDict.keys())
    limit = len(key_list)
    writer.writerow(misspellingsDict.keys())
    writer.writerows(zip(*misspellingsDict.values()))







