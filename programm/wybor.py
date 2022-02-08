import sqlite3
import os
import dodawanie_wpisow
import w_imp
import admin


def maiin():
    print('Wybierz żądaną funkcję')
    print('1. Szukam imprezy')
    print('2. Jestem organizatorem imprez')
    print('3. Administrator')

    n = input('jakiej funkcji potrzebujesz: ')

    if n == '1': 
        nana()
    elif n == '2':
        man()
    elif n == '3':
        admin()
    else: 
        print('Wprowadzono niepoprawną wartość')
        maiin()


""" Osoby szukające imprezy """

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
        w_imp.glawna()

    conm.close()

def nana():
    print('Witamy w wyszukiwarkach wyników')
    print("Wybierz funkcję, której potrzebujesz")
    print('1. Zarejestruj się')
    print('2. autoryzować')
    print('3. do wyboru')

    x = input('Napisz cyfrę swojego wyboru: ')

    if x == '1': 
        registery()
    elif x == '2': 
        authy()
    else: 
        maiin()

""" Poniżej organizatorzy imprez """

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

def man():

    print('Witamy na tablicy organizatorów')
    print("Wybierz funkcję, której potrzebujesz")
    print('1. Zarejestruj się')
    print('2. autoryzować')
    print('3. do wyboru')

    n = input('Napisz cyfrę swojego wyboru: ')

    if n == '1': 
        registerr()
    elif n == '2': 
        dodawanie_wpisow.authh()
    elif n == '3':
        maiin()
    else:  
        print('Wprowadzono niepoprawną wartość!')
        maiin()

""" Poniżej funkcje administratora """
def mana(): 
    admin.logo()


maiin()