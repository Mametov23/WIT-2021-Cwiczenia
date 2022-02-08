class User: 
    def __init__(self, username, password, is_admin = False):
        self.username = username 
        self.password = password
        self.is_admin = is_admin
    
    def get_username(self):
        print(username)

    def set_password(self):
        pas = input('Напиши новый пароль: ')
        if len(pas) < 6:
            print('Bląd')
        elif len(pas) >= 6: 
            self.password = pas

class Admin(User):
    def __init__ (self):
        pass

    def get_users(self):
        print('getting users...')


c = Admin()
c.get_users()