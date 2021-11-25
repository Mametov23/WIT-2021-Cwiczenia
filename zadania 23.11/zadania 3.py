from random import randint
n1 = randint(1, 6)
n2 = randint(1, 6)



while n1 != n2:
    n1 = randint(1, 6)
    n2 = randint(1, 6)
    print('Rzuty kostką: ', n1, n2)

print('równe liczby: ', n1, n2)
