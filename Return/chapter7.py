#Reading files 


sentence = 'Hello\nWorld!'
print(sentence)



fhand = open('text.txt')


#Count lines in file
count = 0
for line in fhand :
    count = count + 1
print('Line Count:', count)

print(fhand.read())

stuff = list()
stuff.append('Book')
stuff.append(99)
print(stuff)



#average sum(nums)/len(nums)

abc = 'With three words'
stuff = abc.split()
#look for blanks and preak it into pieces

print(stuff)


freinds = ['Joseph','Glenn', 'Sally']
freinds.sort()
print(freinds)