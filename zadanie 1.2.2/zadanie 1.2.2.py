try: 
    nwe = []
    n1 = int(input('Ile liczb chcesz napisać? '))
    for i in range(n1):
        nwe.append(float(input()))
    nwe.sort()
    if nwe == []: 
        raise AssertionError('Lista jest pusta')
    max = nwe[-1]
    min = nwe[0]
    summ = sum(nwe)
    print('summ =', summ,'max =', max,'min =', min)
except ValueError: 
    print('Wprowadzono Nie liczbę, ale literę')
except AssertionError as e:
    print(e)