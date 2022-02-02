import sqlite3

def gg():
    print('Welcome')
    print('Wybierz funkcję poniżej')
    print('1. Добавить запись')
    print('2. Удалить запись')
    print('3. Просмотр записей')
    print('4. Посмотреть мои жалобы')
    print('5. Прежупреждения от администратора')
    print('6. Стоп')

    opi = input('Введи число функции: ')

    if opi == '1': 
        dod()
    elif opi == '2': 
        delete()
    elif opi == '3': 
        da()
    elif opi == '4': 
        da()
    elif opi == '5': 
        pred()
    elif opi == '6 ':
        stop()
    else: 
        print('Введено не верное число!')
        gg()
def authh():

    print('Logowanie')
    global loggin
    loggin = input('Wpisz swój login: ')
    passsword = input('Wpisz swój hasło: ')
    con = sqlite3.connect(r'programm/organizator.db')
    curs = con.cursor()
    curs.execute(f"SELECT * FROM organizator WHERE login = '{loggin}' AND password = '{passsword}'")
    con.commit()

    if curs.fetchone() is None:
        print('Wprowadzone dane są nieprawidłowe')
        authh()
        
    else: 
        print("Wszystkie dane są poprawne")
        gg()

    con.close()
def dod(): 
    do = sqlite3.connect(r'programm/org.db')
    po = do.cursor()

    po.execute("""CREATE TABLE IF NOT EXISTS org (
        nazwa TEXT,
        opis TEXT, 
        tim TEXT,
        jezyk TEXT,
        age INTEGER NOT NULL, 
        plat INTEGER NOT NULL,
        kraj TEXT,
        city TEXT,
        ul TEXT,
        login TEXT
    )""")

    do.commit()

    users_nazwa = input('Напиши название мероприятия: ')
    users_opis = input('Опиши, что там будет: ')
    users_tim = input('Введите время проведения мероприятия: ')
    users_jezyk = input('На каких языках: ')
    users_age = int(input('Напиши от какого возраста(например 0): '))
    users_plat = int(input('Стоимость (0 - это бесплатно): '))
    users_kraj = input('В какой стране: ')
    users_city = input('В каком городе: ')
    users_ul = input('На какой улице будет проходить мероприятие: ')
    users_login = loggin

    po.execute(f"SELECT * FROM org")
    if po.fetchone(): 
        po.execute("INSERT INTO org VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (users_nazwa, users_opis, users_tim, users_jezyk, users_age, users_plat, users_kraj, users_city, users_ul, users_login))
        do.commit()
        print('Запись добавлена')
        gg()
    else: 
        print('Запись не добалена/либо же такая запись уже есть')
        gg()


    do.close()
def da(): 
    da = sqlite3.connect(r'programm/org.db')
    pa = da.cursor()

    us_login = loggin
    pa.execute(f"SELECT * FROM org WHERE login = '{us_login}'")
    three_results = pa.fetchall()
    print(df)
    
    input("Нажмите Enter, что бы продолжить")
    da.close()
    gg()
def delete(): 
    dell = sqlite3.connect(r'programm/org.db')
    pop = dell.cursor()

    uz_nazwa = input('Введите название мероприятия: ')

    pop.execute(f"DELETE FROM org WHERE nazwa ='{uz_nazwa}'")
    dell.commit()
    print(pop.fetchall())
    input('Нажмите Enter, что бы продолжить!')
    dell.close()
    gg()
def zob():
    di = sqlite3.connect(r'programm/zab.db')
    pi = do.cursor()

    us_login = loggin
    pa.execute(f"SELECT * FROM zab WHERE organizator = '{us_login}'")
    three_results = pa.fetchall()
    print(df)
    
    input("Нажмите Enter, что бы продолжить")
    da.close()
    gg()
def stop(): 

    raise SystemExit(1)
def pred(): 
    da = sqlite3.connect(r'programm/pred.db')
    pa = da.cursor()

    us_login = loggin
    pa.execute(f"SELECT * FROM pred WHERE login = '{us_login}'")
    three_results = pa.fetchall()
    print(df)
    
    input("Нажмите Enter, что бы продолжить")
    da.close()
    gg()