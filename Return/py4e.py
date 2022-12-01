name = input('Who are you? ')
askString = 'What floor would you like to go to ' +  name + '?'
floor = input(askString)
UsFloor = int(floor) + 1 #convert to us number
print('US floor landing on' , UsFloor)

x = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
y = x.items()


print(y)