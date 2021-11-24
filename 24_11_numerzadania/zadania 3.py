element = input('Podaj liczby: ')
numer= input('Jaką liczbę należy znaleźć? ')
index = element.find(numer)
if index == -1:
    print('False')
else:
    print("True")