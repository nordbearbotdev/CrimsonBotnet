import os

class AccountsRead:
    def __init__(self):
        self.accounts = []
        for account in os.listdir('accounts'):
            if account[-7:] == 'account':
                account = open(f'accounts/{account}', 'r')
                self.accounts.append(account.read())
