

from pandas import notnull


x = 7
if x < 10:
    print('x is less than 10')
if x < 5:
    print('x is less than 5')
else :
    print('x between 5 and 10')


astr = 'hello'

try :
    istr = int(astr)
except :
    istr = -1

print('First', istr)

astr = '123'
try: 
    istr = int(astr)
except :
    istr = -1

print('second', istr)


rawstr = input('Enter a num:')

try: 
    ival = int(rawstr)
except :
    ival = -1

if(ival > 0) :
    print('NICE WORK')
else:
    print('not an number')