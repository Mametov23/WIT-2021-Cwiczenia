import wybieranie_użytkownika
import organizator_materiałów
import auth1


uzytkownic = {"Admin": "eldart987654"}
user_is_authenticated = False

while True:
    print('1. Zarejestruj się')
    print('2. Zaloguj się')
    print('3. Powrót do wyboru użytkownika')
    option = input('Wybierz opcję: ')
    if option == '1':
        login, haslo = auth1.register()
        uzytkownic[login] = haslo
    elif option == '2':
        user_is_authenticated = auth1.login(uzytkownic)
        if user_is_authenticated:
            print('Zalogowano pomyślnie')
        else:
            print('Niepoprawne dane logowania')
    elif option == '3':
        wybieranie_użytkownika