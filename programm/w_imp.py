import sqlite3

def glawna(): 
    print('Welcome')
    print('Wybierz funkcję')
    print('1. Działania filtracyjne')
    print('2. Wszystkie imprezy w moim mieście')
    print('3. Wszystkie wydarzenia na świecie')
    print('4. Skarga na organizatora imprez')
    print('5. Stop')

    p = input('Napisz cyfrę funkcji: ')
    if p == '1': 
        imp()
    elif p == '4':
        cit()
    elif p == '3': 
        glo()
    elif p == '4': 
        zab()
    elif p == '5':
        ggg()
    else: 
        print('Wprowadzono błędną liczbę!')
        glawna()
    
def imp():
    ll = sqlite3.connect(r'programm/org.db')
    li = ll.cursor()

    i_kraj = input('kraj: ')
    i_miasto = input('miasto: ')
    i_cena = int(input('Cena (napisz 0 - za zajęcia bezpłatne): '))
    i_age = int(input('Napisz swój wiek: '))

    if  not (i_kraj and i_miasto and i_cena and i_age) is None : 
        li.execute(f"SELECT * FROM org WHERE kraj LIKE '{i_kraj}' AND city LIKE '{i_miasto}' AND plat <= '{i_cena}' and age <= '{i_age}'")
        ll.commit()

        three_results = li.fetchall()
        print(three_results)
    
        input("Naciśnij Enter, aby kontynuować")
        ll.close()
        glawna()
    else: 
        print('Coś wpisane nie jest poprawne')
        glawna()
def glo(): 
    ll = sqlite3.connect(r'programm/org.db')
    li = ll.cursor()

    li.execute("SELECT * FROM org")
    ll.commit() 
    
    three_results = li.fetchall()
    print(three_results)
    input("Naciśnij Enter, aby kontynuować")
    ll.close()
    glawna()
def zab(): 
    do = sqlite3.connect(r'programm/zab.db')
    po = do.cursor()

    po.execute("""CREATE TABLE IF NOT EXISTS zab (
        nazwa TEXT,
        opisa TEXT,
        organizator TEXT
    )""")

    do.commit()

    users_nazwa = input('Wpisz nazwę imprezy: ')
    users_opisa = input('Powiedz nam o przyczynie skargi: ')
    users_login = input('Login organizatora imprezy: ')


    po.execute(f"SELECT * FROM zab")
    if po.fetchone(): 
        po.execute("INSERT INTO zab VALUES (?, ?, ?)", (users_nazwa, users_opis, users_login))
        do.commit()
        print('Wpis dodany')
        glawna()
    else: 
        print('Taka skarga już istnieje')
        glawna()


    do.close()
def ggg():

    raise SystemExit(1)
def cit():
    ll = sqlite3.connect(r'programm/org.db')
    li = ll.cursor()

    i_kraj = input('kraj: ')
    i_miasto = input('miasto: ')

    if  not (i_kraj and i_miasto) is None : 
        li.execute(f"SELECT * FROM org WHERE kraj LIKE '{i_kraj}' AND city LIKE '{i_miasto}'")
        ll.commit()

        three_results = li.fetchall()
        print(three_results)
    
        input("Naciśnij Enter, aby kontynuować")
        ll.close()
        glawna()
    else: 
        print('Coś wpisane nie jest poprawne')
        glawna()