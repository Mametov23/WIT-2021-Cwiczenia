import register_uzytkownikow
import auth_uzytkownika
import wybieranie_użytkownika




print('1. Zarejestruj się')
print('2. Zaloguj się')
print('3. Powrót do wyboru użytkownika')
option = int(input('Wybierz opcję: '))
if option == 1:
    register_uzytkownikow
elif option == 2:
    auth_uzytkownika
else:
    wybieranie_użytkownika