import sqlite3

def glawna(): 
    print('Добро пожаловать')
    print('Выберите функцию')
    print('1. Мероприятия по фильтру')
    print('2. Все мероприятия в моем городе')
    print('3. Все мероприятия по Миру')
    print('4. Жалоба на организатора мероприятий')
    print('5. Стоп')

    p = input('Напиши цифру Функции: ')
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
        print('Введено не верное число!')
        glawna()
    
def imp():
    ll = sqlite3.connect(r'programm/org.db')
    li = ll.cursor()

    i_kraj = input('Страна: ')
    i_miasto = input('Город: ')
    i_cena = int(input('Цена(напишите 0 - для бесплатных мероприятий): '))
    i_age = int(input('Наишите свой возраст:'))

    if  not (i_kraj and i_miasto and i_cena and i_age) is None : 
        li.execute(f"SELECT * FROM org WHERE kraj LIKE '{i_kraj}' AND city LIKE '{i_miasto}' AND plat <= '{i_cena}' and age <= '{i_age}'")
        ll.commit()

        three_results = li.fetchall()
        print(three_results)
    
        input("Нажмите Enter, что бы продолжить")
        ll.close()
        glawna()
    else: 
        print('Что-то введено не правильно')
        glawna()
def glo(): 
    ll = sqlite3.connect(r'programm/org.db')
    li = ll.cursor()

    li.execute("SELECT * FROM org")
    ll.commit() 
    
    three_results = li.fetchall()
    print(three_results)
    input("Нажмите Enter, что бы продолжить")
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

    users_nazwa = input('Напиши название мероприятия: ')
    users_opisa = input('Расскажите о причине жалобы: ')
    users_login = input('Логин организатора мероприятия: ')


    po.execute(f"SELECT * FROM zab")
    if po.fetchone(): 
        po.execute("INSERT INTO zab VALUES (?, ?, ?)", (users_nazwa, users_opis, users_login))
        do.commit()
        print('Запись добавлена')
        glawna()
    else: 
        print('Такая жалоба уже существует')
        glawna()


    do.close()
def ggg():

    raise SystemExit(1)
def cit():
    ll = sqlite3.connect(r'programm/org.db')
    li = ll.cursor()

    i_kraj = input('Страна: ')
    i_miasto = input('Город: ')

    if  not (i_kraj and i_miasto) is None : 
        li.execute(f"SELECT * FROM org WHERE kraj LIKE '{i_kraj}' AND city LIKE '{i_miasto}'")
        ll.commit()

        three_results = li.fetchall()
        print(three_results)
    
        input("Нажмите Enter, что бы продолжить")
        ll.close()
        glawna()
    else: 
        print('Что-то введено не правильно')
        glawna()