import sqlite3
import requests
from pprint import pprint
# 1). Create a database model
conn = sqlite3.connect('swapi.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS users (username, password)')
cursor.execute('CREATE TABLE IF NOT EXISTS logs (action, date)')
conn.commit()
conn.close()
# 2). Create Python models
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def greeting(self):
        print(f'Hello, I am {self.username}')

class Log:
    def __init__(self, action, date):
        self.action = action
        self.date = date
# 3). Create the application's logic
def register():
    username = input('Input username: ')
    password = input('Input password: ')
    conn = sqlite3.connect('swapi.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users VALUES (?, ?)', (username, password))
    conn.commit()
    conn.close()

def login():
    username = input('Input username: ')
    password = input('Input password: ')
    conn = sqlite3.connect('swapi.db')
    cursor = conn.cursor()
    queryset = cursor.execute('SELECT * from users')
    users = queryset.fetchall()
    conn.close()
    # Converting primitive data structures to composite data types
    user_objects = []
    for user in users:
        user_objects.append(User(user[0], user[1]))

    # Verifying user's credentials
    for user in user_objects:
        if user.username == username and user.password == password:
            return user
    return False

global user
user = False
while True:
    if user:
        print('1. Log-out')
        print('2. Show all people from Star Wars')
        print('0. Exit')
        option = input ('Choose an option: ')
        if option == '1':
            user = False
        elif option == '2':
            response = requests.get('https://swapi.dev/api/people/')
            data = response.json()
            pprint(data)
        elif option == '0':
            break
    else:
        print('1. Register')
        print('2. Log-in')
        print('0. Exit')
        option = input('Choose an option: ')
        if option == '1':
            register()
        elif option == '2':
            user = login()
        elif option == '0':
            break