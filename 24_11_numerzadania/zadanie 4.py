def cotocoto():
    string = input("Podaj string: ")

    if not len(string) == 8:
        raise ValueError('Powinno być 8 znaków')
    else:
        print('Ok')

cotocoto()
