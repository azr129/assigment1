from abc import ABC, abstractmethod


class transaction(ABC):
    def __init__(self,customerId, tellerId):
        self._customerId = customerId
        self._tellerId = tellerId

    def get_customer_id(self):
        return self._customerId
    
    def get_teller_id(self):
        return self._tellerId

    def get_transaction_description(self):
        pass


class Deposit(transaction):                           #deposit
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self._amount = amount

    def get_transaction_description(self):
        return U'Teller {self.get_teller_id()} deposited {self._amount} to account {self.get_customer_id()}' 


class Withdrawal(transaction):
    def __init__(self, customerId, tellerId, amount):
        super().__init__(customerId, tellerId)
        self._amount = amount

    
    def get_transaction_description(self):
        return U'Teller {self.get_teller_id()} withdrew {self._amount} from account {self.get_customer_id()}' 
    

class OpenAccount(transaction):
    def __init__(self, customerId, tellerId):
        super().__init__(customerId, tellerId)

    def get_transaction_description(self):
        return U'Teller {self.get_teller_id()} opened account {self.get_customer_id()}'
    
class BankAccount:
    def __init__(self, customerId, name, balance):
        self._customerId = customerId
        self._name = name
        self._balance = balance
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount


class bankaccounts:
    def __init__(self):
        pass

    def get_savings_account(self, amount):
        self._balance += amount

    def get_checquing_account(self, amount):
        self._balance = amount 


class ShowAccountMenu:
    def __init__(self, balance, deposit, withdraw, exit_account):
        self._balance = balance
        self._deposit = deposit 
        self._withdraw = withdraw
        self._exit_account = exit_account


    def get_balance(self):
        return self._balance
    
    def get_deposit(self):
        return self._deposit
    
    def get_withdraw(self):
        return self._withdraw
    
    def get_exit_account(self):
        return self._exit_account