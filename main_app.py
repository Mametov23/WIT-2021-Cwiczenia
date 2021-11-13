import auth

uzytkownicy = {'Admin': '1234'}
user_is_authenticated = False

while True:
    print('1. Zarejestruj się')
    print('2. Wyświetl uzytkowników')
    print('3. Zaloguj się')
    print('4. Zmień hasło użytkownika')
    print('5. Usuń użytkownika')
    print('0. Wyjdź z programu')
    option = input('Wybierz opcję: ')
    if option == '1':
        login, haslo = auth.register()
        uzytkownicy[login] = haslo
    elif option == '2':
        print(uzytkownicy)
    elif option == '3':
        user_is_authenticated = auth.login(uzytkownicy)
        if user_is_authenticated:
            print('Zalogowano pomyślnie')
        else:
            print('Niepoprawne dane logowania')
    elif option == '4': 
       uz = input('Nazwa użytkownika: ')
       if uz == login: 
            n1 = input('Wpisz nowe hasło: ')
            if len(n1) >= 6: 
                haslo = n1
                uzytkownicy[login] = haslo
                print("hasło dodane")
            else: 
                print('Hasło musi mieć mniej niż 6 znaków')
       else: 
            print('Taki użytkownik nie istnieje')
    elif option == '5': 
        uz = input('Nazwa użytkownika: ')
        if uz == uzytkownicy[uz]: 
            del uzytkownicy[uz]
            print('Użytkownik', uz,'usunięty')
        else:
            print('Taki użytkownik nie istnieje')
    elif option == '0':
        break