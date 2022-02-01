import sqlite3

def maiin():
    print('Выбери нужную тебе функцию')
    print('1. Ищю мероприятие')
    print('2. Я организатор мероприятий')

    n = int(input('какая функция тебе нужна: '))

    if n == 1: 
        nana()
    elif n == 2:
        man()



def registery():
    db = sqlite3.connect(r'programm/users.db')
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
        nana()
    else: 
        print('Taki użytkownik już istnieje')
        nana()


    db.close()

def authy():
    print('Logowanie')
    loggin = input('Wpisz swój login: ')
    passsword = input('Wpisz swój hasło: ')
    conm = sqlite3.connect(r'programm/users.db')
    cursm = conm.cursor()
    cursm.execute(f"SELECT * FROM users WHERE login = '{loggin}' AND password = '{passsword}'")
    conm.commit()

    if cursm.fetchone() is None:
        print('Wprowadzone dane są nieprawidłowe')
        nana()
    else: 
        print("Wszystkie dane są poprawne")
        nana()

    conm.close()

def nana():
    print('Добро пожаловать в табло поисковиков')
    print("Выбери функцию, которая тебе нужна")
    print('1. зарегестрироваться')
    print('2. авторизоваться')
    print('3. к выбору')

    x = int(input('Напиши цифру твоего выбора: '))

    if x == 1: 
        registery()
    elif x == 2: 
        authy()
    else: 
        maiin()


def registerr():
    dbb = sqlite3.connect(r'programm/organizator.db')
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
        man()
    else: 
        print('Taki użytkownik już istnieje')
        man()


    dbb.close()

def authh():
    print('Logowanie')
    loggin = input('Wpisz swój login: ')
    passsword = input('Wpisz swój hasło: ')
    con = sqlite3.connect(r'programm/organizator.db')
    curs = con.cursor()
    curs.execute(f"SELECT * FROM organizator WHERE login = '{loggin}' AND password = '{passsword}'")
    con.commit()

    if curs.fetchone() is None:
        print('Wprowadzone dane są nieprawidłowe')
        man()
    else: 
        print("Wszystkie dane są poprawne")
        man()

    con.close()

def man():

    print('Добро пожаловать в табло организаторов')
    print("Выбери функцию, которая тебе нужна")
    print('1. зарегестрироваться')
    print('2. авторизоваться')
    print('3. к выбору')

    n = int(input('Напиши цифру твоего выбора: '))

    if n == 1: 
        registerr()
    elif n == 2: 
        authh()
    else: 
        maiin()



maiin()