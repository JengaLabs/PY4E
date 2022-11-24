

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75

print(purse)

print(purse['candy'])

#Can modifie a value
purse['candy'] = purse['candy'] + 2
print(purse['candy'])
#can set an indexes value
purse['candy'] = 10
print(purse['candy'])

#in a list the keys are the index position, while a dicts keys can be any data types literals

counts = dict()

names = ['bruv', 'jake', 'daniel', 'jake', 'zqian', 'bruv']
#*
#for name in names :
 #   if name not in counts:
 #       counts[name] = 1
 #   else :
#        counts[name] = counts[name] + 1 
#print(counts)

#this method of checking to see if a key is already in a dict exist

for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

#Histogram of words in a file

#handle opening file
fhand = open('text.txt')
#Get string of the file
fileContent = fhand.read()
#word count dictionary
wordCountDict = dict()

for word in fileContent.split():
    wordCountDict[word] = wordCountDict.get(word, 0) + 1



value = any


largest = -1
for k,v in wordCountDict.items() :
    if v > largest :
        largest = v 
        value = k
    
        

print(value, largest)


#Convert dict to list and print 
#wordCountList = wordCountDict.items()
#for aaa,bbb in wordCountDict.items() :
 #   print(aaa,bbb)


#for key in wordCountDict:
#    print(key, wordCountDict[key])


