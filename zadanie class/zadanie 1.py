class BanKard: 
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

class BankAccount: 
    def _init_(self, owner, balance, bank): 
        self.owner = owner
        self.balance = balance
        self.bank = bank

    def get_owner(self):
        print('owner...')

    def get_balance(self):
        print('balance...')

    def get_bank(self):
        print('bank...')

    def set_balance(self):
        print('self_balance...')

class Bank:
    def __init__(self, name, bank_accounts, bank_cards):
        self.name = name
        self.bank_accounts = bank_accounts
        self.bank_cards = bank_cards

    def get_bank_accounts(self):
        print('get_bank_accounts...')

    def get_bank_cards(self):
        print('get_bank_cards...')

class CrediCard(BankCard):
    def __init__(self, balance, payments_history):
        super()._init_(owner,number,provider)
        self.payments_history = payments_history
        self.balance = balance

    def get_balance(self):
        print('get_balance....')

    def set_balance(self):
        print('set_balance...')

    def get_payments_history(self):
        print('get_payments_history...')


class PremiumBankAccount(BankAccount):
    def _init_(self,financial_manager):
        super()._init_(owner, balance, bank)
        self.financial_manager = financial_manager

    def get_financial_manager(self):
        print('get_financial_manager...')

    def set_financial_manager(self):
        print('set_financial_manager...')

class StudentBankAccount(BankAccount):
    def _init_(self, overdraft_balance, overdraft_limit):
        super()._init_(owner, balance, bank)
        self.overdraft_balance = overdraft_balance
        self.overdraft_limit = overdraft_limit

    def get_overdraft_balance(self):
        print('get_overdraft_balance...')

    def set_overdraft_balance(self):
        print('set_overdraft_balance...')

    def get_overdraft_limit(self):
        print('get_overdraft_limit...')

    def set_overdraft_limit(self):
        print('set_overdraft_limit...')
