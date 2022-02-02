import sqlite3
import os
import dodawanie_wpisow
import w_imp
import admin


def maiin():
    print('Выбери нужную тебе функцию')
    print('1. Ищю мероприятие')
    print('2. Я организатор мероприятий')
    print('3. Администратор')

    n = input('какая функция тебе нужна: ')

    if n == '1': 
        nana()
    elif n == '2':
        man()
    elif n == '3':
        admin()
    else: 
        print('Введено не верное значение')
        maiin()


""" Те, кто ищут мероприятие """

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
    print('Добро пожаловать в табло поисковиков')
    print("Выбери функцию, которая тебе нужна")
    print('1. зарегестрироваться')
    print('2. авторизоваться')
    print('3. к выбору')

    x = input('Напиши цифру твоего выбора: ')

    if x == '1': 
        registery()
    elif x == '2': 
        authy()
    else: 
        maiin()

""" Ниже организаторы мероприятий """

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

    print('Добро пожаловать в табло организаторов')
    print("Выбери функцию, которая тебе нужна")
    print('1. зарегестрироваться')
    print('2. авторизоваться')
    print('3. к выбору')

    n = input('Напиши цифру твоего выбора: ')

    if n == '1': 
        registerr()
    elif n == '2': 
        dodawanie_wpisow.authh()
    elif n == '3':
        maiin()
    else:  
        print('Введено не верное значение!')
        maiin()

""" Ниже функции администратора """
def mana(): 
    admin.logo()


maiin()