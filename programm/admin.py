import sqlite3

def logo(): 
    print("Авторизация")
    global log
    log = input('Введи логин: ')
    pas = input('Введи пароль: ')

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
    print('Админ панель')
    print('1. Посмотреть жалобы от пользователей')
    print('2. Отправить предупреждение организатору')
    print('3. Удалить организатора')
    print('4. Посмотреть все мероприятия')
    print('4. Стоп')
    
    e = input('Введите номер функции: ')

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
    input("Нажмите Enter, что бы продолжить")
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

    nazwaor = input('Логин организатора на которого поступает предупреждение: ')
    dlaczegoo = input('Введите коротко причину предупреждения: ')
    opisanie = input("Опишите причину подробнее: ")

    po.execute(f"SELECT * FROM pred")
    if po.fetchone(): 
        po.execute("INSERT INTO pred VALUES (?, ?, ?)", (nazwaor, dlaczegoo, opisanie))
        do.commit()
        print('Запись добавлена')
        h()
    else: 
        print('Запись не добалена/либо же такая запись уже есть')
        h()


    do.close()
def deleteor(): 
    dell = sqlite3.connect(r'programm/organizator.db')
    pop = dell.cursor()

    uz_nazwa = input('Введите имя организатора: ')

    pop.execute(f"DELETE FROM organizator WHERE login ='{uz_nazwa}'")
    dell.commit()
    print(pop.fetchall())
    input('Нажмите Enter, что бы продолжить!')
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
    input("Нажмите Enter, что бы продолжить")
    ll.close()
    glawna()