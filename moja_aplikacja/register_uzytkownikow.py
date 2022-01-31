import sqlite3
import auth_uzytkownika
import sqlite3
 

db = sqlite3.connect(r'moja_aplikacja/users.db')
sql = db.cursor()

sql.execute("""CREATE TABLE IF NOT EXISTS users (
    login TEXT, 
    password TEXT
)""")

db.commit()

users_login = input('Wpisz swoje imię: ')
users_password = input('Wpisz hasło: ')

sql.execute(f"SELECT login FROM users WHERE login = '{users_login}'")
    
if sql.fetchone() is None: 
    sql.execute(f"INSERT INTO users VALUES (?, ?)", (users_login, users_password))
    db.commit()
    print('użytkownik dodany do bazy ')
    auth_uzytkownika
else: 
    print('Taki użytkownik już istnieje')

db.close()