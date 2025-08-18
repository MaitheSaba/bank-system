from transaction import Transaction
from checking_account import CheckingAccount

class Withdrawal(Transaction):
    def __init__(self, amount = 0):
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        self._amount = value

    def register(self, client_account: CheckingAccount):
        """
        Attempts to withdraw the specified amount from the client's account, checking the criteria

        Tenta sacar o valor especificado da conta do cliente, verificando os critérios
        """
        current_balance = client_account.balance() 
        if current_balance < self._amount:
            return False, "Saldo insuficiente. Saque não efetuado."
        elif self._amount > client_account.limit():
            return False, "Limite insuficiente. Saque não efetuado."
        elif client_account.withdrawal_count() == client_account.max_daily_withdrawals(): 
            return False, "Máximo de saques diários atingido. Saque não efetuado."
        elif self._amount <= 0:
            return False, "Saque deve ser maior que R$0.00. Saque não efetuado."
        else:
            client_account.add_withdrawal_count()
            return client_account.withdraw(self._amount)