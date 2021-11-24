def register(): 
    login = input('podaj login: ')
    haslo = input('podaj hasło: ')
    powtorz_haslo = input('powtorz proszę hasło: ')

    try:
         if not haslo == powtorz_haslo:
            print('oba hasła musi byc ze sobą zgodne')
         if not len(haslo) >= 6:
             print('hasło musi być większe niż 6 znaków')

         return login, haslo
    except AssertionError:
        print('Login nie pasuje do Regulaminu')
    except ValueError:
        print('hasło nie pasuje do Regulaminu')


def login(ussers):
    login = input('Podaj login: ')
    haslo = input('Podaj haslo: ')

    if ussers.get(login):
        return ussers.get(login) == haslo
    else:
        return False

