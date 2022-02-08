import sqlite3

def gg():
    print('Welcome')
    print('Wybierz funkcję poniżej')
    print('1. Dodaj wpis')
    print('2. Usuń wpis')
    print('3. Zobacz wpisy')
    print('4. Zobacz moje skargi')
    print('5. Ostrzeżenia od administratora')
    print('6. Stop')

    opi = input('Wprowadź liczbę funkcji: ')

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
        print('Wprowadzono błędną liczbę!')
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

    users_nazwa = input('wpisz nazwę imprezy: ')
    users_opis = input('opisz co tam będzie: ')
    users_tim = input('podaj czas trwania imprezy: ')
    users_jezyk = input('w jakich językach: ')
    users_age = int(input('Napisz od jakiego wieku (np. 0): '))
    users_plat = int(input('Koszt (0-to nic nie kosztuje): '))
    users_kraj = input('W jakim kraju: ')
    users_city = input('W jakim mieście: ')
    users_ul = input('Na której ulicy odbędzie się impreza: ')
    users_login = loggin

    po.execute(f"SELECT * FROM org")
    if po.fetchone(): 
        po.execute("INSERT INTO org VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (users_nazwa, users_opis, users_tim, users_jezyk, users_age, users_plat, users_kraj, users_city, users_ul, users_login))
        do.commit()
        print('Wpis dodany')
        gg()
    else: 
        print('Wpis nie został dodany / albo taki wpis już jest')
        gg()


    do.close()
def da(): 
    da = sqlite3.connect(r'programm/org.db')
    pa = da.cursor()

    us_login = loggin
    pa.execute(f"SELECT * FROM org WHERE login = '{us_login}'")
    three_results = pa.fetchall()
    print(df)
    
    input("Naciśnij Enter, aby kontynuować")
    da.close()
    gg()
def delete(): 
    dell = sqlite3.connect(r'programm/org.db')
    pop = dell.cursor()

    uz_nazwa = input('Wpisz nazwę wydarzenia: ')

    pop.execute(f"DELETE FROM org WHERE nazwa ='{uz_nazwa}'")
    dell.commit()
    print(pop.fetchall())
    input('Naciśnij Enter, aby kontynuować!')
    dell.close()
    gg()
def zob():
    di = sqlite3.connect(r'programm/zab.db')
    pi = do.cursor()

    us_login = loggin
    pa.execute(f"SELECT * FROM zab WHERE organizator = '{us_login}'")
    three_results = pa.fetchall()
    print(df)
    
    input("Naciśnij Enter, aby kontynuować")
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
    
    input("Naciśnij Enter, aby kontynuować")
    da.close()
    gg()