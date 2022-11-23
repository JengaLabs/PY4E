#Functions


def greet(lang) :
    if lang == 'es':
        return 'Hola' 
    elif lang =='fr':
        return 'Bonjour'
    else: 
        return 'Hello'

print(greet('es'))


def thing() :
    print('hello')
    print('nerd')

def writeName(name) :
    print('Hello ' + name)


writeName('pig')

big = max('Hello World')
tiny = min('Hello World')
print(big)
print(tiny)


