from transaction import Transaction
from checking_account import CheckingAccount

class Deposit(Transaction):
    def __init__(self, amount = 0):
        self._amount = amount

    @property
    def amount(self):
        return self._amount
    
    def register(self, client_account: CheckingAccount):
        """
        Attempts to deposit the specified amount into the client's account, checking the criteria

        Tenta depositar o valor especificado na conta do cliente, verificando os critérios
        """
        if self._amount <= 0:
            return False, "Depósito cancelado. Somente valores maiores que R$0.00"
        else:
            return client_account.deposit(self._amount)
