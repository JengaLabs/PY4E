#Strings are just a collection of chars

s = 'Monty Python'

print(s[0])

#for letter in s :
    #print(letter)

#print up to but not including
#omit to do the begining or ending 
print(s[0:])

#Check if letter is in string
if 'n' in s :
    print('N is in fruit')

print('Done')

#Find the school
data = 'From stephen.marquard@ct.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

#find space after @ 
sspos = data.find(' ',atpos)
print(sspos)

host = data[atpos+1 : sspos]
print(host)

print(len('banana')*7)


data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
pos = data.find('.')
print(data[pos:pos+3])