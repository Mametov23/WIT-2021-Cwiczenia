import sqlite3

def logo(): 
    print("Logowanie")
    global log
    log = input('Wpisz login: ')
    pas = input('Wpisz hasło: ')

    con = sqlite3.connect(r'programm/admin.db')
    curs = con.cursor()
    curs.execute(f"SELECT * FROM organizator WHERE login = '{loggin}' AND password = '{passsword}'")
    con.commit()

    if curs.fetchone() is None:
        print('Wprowadzone dane są nieprawidłowe')
        logo()
        
    else: 
        print("Wszystkie dane są poprawne")
        h()

    con.close()


def h(): 
    print('Admin panel')
    print('1. Zobacz skargi od użytkowników')
    print('2. Wyślij Ostrzeżenie do organizatora')
    print('3. Usuń organizatora')
    print('4. Zobacz wszystkie wydarzenia')
    print('4. Stop')
    
    e = input('Wprowadź numer funkcji: ')

    if e == '1': 
        zaloby()
    elif e == '2':
        predy()
    elif e == '3':
        deleteor()
    elif e == '4':
        stoped()

def zaloby(): 
    ll = sqlite3.connect(r'programm/zab.db')
    li = ll.cursor()

    li.execute("SELECT * FROM zab")
    ll.commit() 
    
    three_results = li.fetchall()
    print(three_results)
    input("Naciśnij Enter, aby kontynuować")
    ll.close()
    h()
def predy(): 
    do = sqlite3.connect(r'programm/pred.db')
    po = do.cursor()

    po.execute("""CREATE TABLE IF NOT EXISTS pred (
        nazwaor TEXT,
        dlaczego TEXT, 
        opisanie TEXT
    )""")

    do.commit()

    nazwaor = input('Login Organizatora na który napływa Ostrzeżenie: ')
    dlaczegoo = input('Wpisz krótko powód Ostrzeżenia: ')
    opisanie = input("opisz bardziej szczegółowo przyczynę skargi na użytkownika: ")

    po.execute(f"SELECT * FROM pred")
    if po.fetchone(): 
        po.execute("INSERT INTO pred VALUES (?, ?, ?)", (nazwaor, dlaczegoo, opisanie))
        do.commit()
        print('Wpis dodany')
        h()
    else: 
        print('Wpis nie został dodany / albo taki wpis już jest')
        h()


    do.close()
def deleteor(): 
    dell = sqlite3.connect(r'programm/organizator.db')
    pop = dell.cursor()

    uz_nazwa = input('Wpisz nazwę organizatora: ')

    pop.execute(f"DELETE FROM organizator WHERE login ='{uz_nazwa}'")
    dell.commit()
    print(pop.fetchall())
    input('Naciśnij Enter, aby kontynuować!')
    dell.close()
    gg()
def stoped():
        raise SystemExit(1)
def wsi(): 
    ll = sqlite3.connect(r'programm/org.db')
    li = ll.cursor()

    li.execute("SELECT * FROM org")
    ll.commit() 
    
    three_results = li.fetchall()
    print(three_results)
    input("Naciśnij Enter, aby kontynuować")
    ll.close()
    glawna()