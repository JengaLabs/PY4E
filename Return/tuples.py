
#Tuples are like list, they contain elements that are stored in a index
#The difference is tuples are immutable


#LIst
l = [9, 8, 7]
l[2] = 6
print(l)


#string can't have an element changed either
#y = 'ABC'
#y[2] = 'D'

#tupple, can't have elements changed either
#t = (1, 9, 2)
#print(t[2])
#this is for effiency in the background
#thus a list can't be sorted, appeneded or revereed
#print(type(t))
#The reason to use them is just for efficenty 
#they can salso be put on the left hand side of assignment
#(a, b) = (4, 'Fred')
#print(b)
#
#d = dict()
#d['csev'] = 2
##d['cwen'] = 4
#for (k, v) in d.items() :
 #   print(k, v)

#tups = d.items()
#print(tups)

#Tuples are comparable
#Checks items in order if they are equal, goes to the next index

#(0, 1, 200) < (0, 3 ,2)
#True

#Sorting a lists of tuples

#dictionary
d = {'a': 10, 'b':1, 'c':22 }

#print(d.items())
#returns a tuple sorted by key
#print(sorted(d.items()))

#Sort items by key 
t = sorted(d.items())
for k,v in sorted(d.items()) :
    print(k,v)

#Sort by values 
c = {'a':10, 'b':1, 'c':22}
tmp = list()

for k,v in c.items() :
    #add to temp list a tupple added in value key order
    tmp.append(( v, k))
print(tmp)
#get a tuple sorted in reverse 
tmp = sorted(tmp, reverse=True)
print(tmp)

fhand = open('text.txt')
counts = dict()
for line in fhand :
    words = line.split()
    for word in words :
        counts[word] = counts.get(word,0)  + 1

lst = list()
for key, val in counts.items() :
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

#go through the top ten in list, 
for val, key in lst[:10] :
    print (key, val)


#Does the same as above code 
c = {'a':10, 'b':1, 'c':22}
print(sorted([ (v,k) for k,v in c.items() ], reverse=True ) )

print(dir(tuple))