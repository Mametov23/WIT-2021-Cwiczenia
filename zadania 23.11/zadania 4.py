from random import randint

i = int(input('Ile razy chcesz rzucić kostką do gry?'))
o = 0
g = 0
while o < i:
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    if n1 == n2:
        print('liczby równe: ', n1, n2)
        g = g + 1

    else:
        print('nierówne liczby: ', n1, n2)
    o = o+1
    
print('równych liczb wypadło: ', g)