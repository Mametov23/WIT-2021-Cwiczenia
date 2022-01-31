import sqlite3
 
dbb = sqlite3.connect(r'moja_aplikacja/organizator.db')
sq = dbb.cursor()

sq.execute("""CREATE TABLE IF NOT EXISTS organizator (
    login TEXT, 
    password TEXT
)""")

dbb.commit()

users_login = input('Wpisz swoje imię: ')
users_password = input('Wpisz hasło: ')

sq.execute(f"SELECT login FROM organizator WHERE login = '{users_login}'")
if sq.fetchone() is None: 
    sq.execute(f"INSERT INTO organizator VALUES (?, ?)", (users_login, users_password))
    dbb.commit()
    print('użytkownik dodany do bazy ')
else: 
    print('Taki użytkownik już istnieje')


dbb.close()