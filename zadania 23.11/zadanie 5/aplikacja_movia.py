import auth1

movies = []
ussers = {'admin': '1212'}
user_is_authenticated = False

while True:
    print('1. twórz użytkownika: ')
    print('2. Dodaj film: ')
    print('3. Zmodyfikuj ilość dostępnego filmu: ')
    print('4. Zobacz całą ofertę: ') 
    print('5. Sprawdź dostępność filmu')
    print('6. Wypożycz film: ')
    print('7. Zaloguj się:')
    print('0. Wyjdź z programu')
    option = input('Wybierz opcję: ') 
    if option == '1':
        login, haslo = auth1.register()    #тут я регестрирую пользователя 
        ussers[login] = haslo
    elif option == '7':
        user_is_authenticated = auth1.login(ussers)   #тут вход в свой профиль 
        if user_is_authenticated:
            user_is_authenticated = True
            print('zalogowano pomyślnie')
        else:
            print('Niepoprawne dane logowania')
    elif option == "2":
        if user_is_authenticated == True:
            nazwa = input('Jak nazywa film?  ')
            movies.append(nazwa)
        else:
            print('Nie ma takiego uzytkownika')
    elif option == '4':
        print(movies)
    elif option == '3':
        uz = input('Tytuł filmu, który chcesz usunąć: ')
        if uz in movies:
            movies.remove(uz)
            print('Film', uz,'usunięty')
        else:
            print('Takiego filmu nie ma na liście')
    elif option == '5':
        name = input('Tytuł filmu: ')
        if name in movies:
            print('Taki film jest')
        else:
            print('Nie ma takiego filmu')
    elif option == '6':
        n2 = input('Wyślij literę Y, jeśli chcesz wypożyczyć film: ')
        if n2 == "Y":
            n3 = input('Jak nazywa się film?  ')
            if n3 in movies:
                n4 = int(input('Na ile dni chcesz wypożyczyć film? '))
                print('Masz film', n3, 'na', n4, 'dni')
            else:
                print('Nie ma takiego filma')
        else:
           print("Now it's really ded inside")
    elif option == '0':
        break



