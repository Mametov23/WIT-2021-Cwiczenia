class BankKard: 
    def __init__(self, owner, number, provider): 
        self.owner = owner
        self.number = number 
        self.provider = provider

    def get_number(self): 
        print('number...')

    def get_owner(self): 
        print('owner...')
    
    def get_provider(self): 
        print('provider...')

bank1 = BankKard('1233', '0554440', 'play')
bank1.get_number()