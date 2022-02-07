import sqlite3
import datetime

class User:
    '''
    username: nazwa użytkownika,
    password: hasło użytkownika,
    requests_count: ilość requestów wykonanych przez użytkownika
    '''
    def __init__(self, username, password, requests_count):
        self.username = username
        self.password = password
        self.requests_count = requests_count
    
    def us(self):
        print('Username: ', self.username)
        print('Password:', self.password)
        print('Requests_count: ', self.requests_count)
    


class Log:
    '''
    username: nazwa użytkownika k†óry wykonał zapytanie,
    date: data kiedy zapytanie zostało wykonane
    type_param: co użytkownik wybrał jako `type`,
    number_param: co użytkownik wybrał jako `number` 
    '''
    def __init__(self, username, data, type_param, number_param):
        self.username = username 
        self.data = data
        self.type_param = type_param
        self.number_param = number_param

    def logo(self):
        print('username:', self.username)
        print('date: ', self.data)
        print('type: ', self.type_param)
        print('number: ', self.number_param)

    



def register():
    
    username = input('Input username: ')
    password = input('Input password: ')
    requests_count = 0
    conn = sqlite3.connect(r'requests/numbeapp.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?, ?)', (username, password, requests_count))
    conn.commit()
    conn.close()

def login():
    global username
    username = input('Input username: ')
    password = input('Input password: ')
    conn = sqlite3.connect(r'requests/numbeapp.db')
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * FROM users')
    users = queryset.fetchall()
    # Converting primitive data structures to composite data types
    user_objects = []
    for user in users:
        user_objects.append(User(user[0], user[1], user[2]))

    # Verifying user's credentials
    for user in user_objects:
        if user.username == username and user.password == password:
            return user
    return False



def get_number():
    import datetime
    try:
        type = input("Napisz Typ(prykład: `trivia`, `math`, `date`, lub `year`): ")
        if type == 'trivia' or type == 'math' or type == 'date' or type == 'year':
            print('type jest zapisano')
        elif not (type == 'trivia' or type == 'math' or type == 'date'):
            type = 'trivia'
            print('the default type is trivia')
        number = input("Możesz napisać słowo 'random' lub liczbę całkowitą, a jeśli wybrałeś' type ' date, to w formie month / day: ")
        
        b = datetime.datetime.now()
        conn = sqlite3.connect(r'requests/numbeapp.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO logs VALUES (?, ?, ?, ?)', (username, b, type, number))
        conn.commit()
        cursor.execute(f'UPDATE users set requests_count = requests_count + 1 WHERE username = "{username}" ')
        conn.commit()
        print('Wpis został pomyślnie zaktualizowany')
        cursor.close()

    except sqlite3.Error as error:
        print("Błąd podczas pracy z SQLite", error)
    finally:
        if conn:
            conn.close()
            print("Połączenie z SQLite zamknięte")

def get_logs():
    conn = sqlite3.connect(r'requests/numbeapp.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM logs WHERE username = '{username}'")
    a = cursor.fetchone()
    usernam = a[0]
    date = a[1]
    typ = a[2]
    num = a[3]
    ex = Log(usernam, date, typ, num)
    ex.logo()
    print(ex)
    conn.close()

def get_users():
    conn = sqlite3.connect(r'requests/numbeapp.db')
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    a = cursor.fetchone()
    usernam = a[0]
    date = a[1]
    req = a[2]
    ex = User(usernam, date, req)
    ex.us()
    print(ex)
    conn.close()


user = False
while True:
    if not user:
        print('1. Zarejestruj się')
        print('2. Zaloguj się')
        print('0. Wyjdź z programu')
        option = input('Podaj opcję: ')
        if option == '1':
            register()
        elif option == '2':
            user = login()
        elif option == '0':
            break
    else:
        print('1. Wykonaj zapytanie')
        print('2. Zobacz logi')
        print('3. Zobacz uzytkowników')
        print('0. Wyjdź z programu')
        option = input('Podaj opcję: ')
        if option == '1':
            get_number()
        elif option == '2':
            get_logs()
        elif option == '3':
            get_users()
        elif option == '0':
            break;