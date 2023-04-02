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
    

    

