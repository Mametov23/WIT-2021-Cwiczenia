def register(): 
    login = input('podaj login: ')
    haslo = input('podaj hasło: ')
    powtorz_haslo = input('powtorz proszę hasło: ')

    try:
         assert len(login) >= 5, 'musi byc wielu znakow'

         if not haslo == powtorz_haslo:
            raise ValueError('oba hasła musi byc ze sobą zgodne')
         if not len(haslo) >= 6:
             raise ValueError('hasło musi być większe niż 6 znaków')

         return login, haslo
    except AssertionError:
        print('Login nie pasuje do Regulaminu')
    except ValueError:
        print('hasło nie pasuje do Regulaminu')


def login(uzytkownicy):
    login = input('Podaj login: ')
    haslo = input('Podaj hasło: ')

    if uzytkownicy.get(login): 
        return uzytkownicy.get(login) == haslo
    else: 
        return False
