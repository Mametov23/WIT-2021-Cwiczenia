import sqlite3 
import prosty_uzytkownik

print('Logowanie')
loggin = input('Wpisz swój login: ')
passsword = input('Wpisz swój hasło: ')
con = sqlite3.connect(r'moja_aplikacja/users.db')
curs = con.cursor()
curs.execute(f"SELECT * FROM users WHERE login = '{loggin}' AND password = '{passsword}'")
con.commit()

if curs.fetchone() is None:
    print("Wszystkie dane są poprawne")
else: 
    print('Wprowadzone dane są nieprawidłowe')
    prosty_uzytkownik

con.close()