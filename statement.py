class Balance:
    def __init__(self):
        self._balance = 0.0
        self._statement = ""

    def getBalance(self):
        """
        Returns the current account balance

        Retorna o saldo atual
        """
        return self._balance

    def setDeposit(self, amount):
        """
        Adds the given amount to the balance and logs the deposit

        Aumenta o saldo, depositando o valor recebido (amount), e registra o depósito
        """
        self._balance += amount
        self._statement += f"Depósito registrado: R${amount:.2f}\n"
        return self._balance

    def setWithdrawal(self, amount):
        """
        Subtracts the given amount from the balance and logs the withdrawal

        Diminui o saldo, 'sacando' o valor recebido (amount), e registra o saque
        """
        self._balance -= amount
        self._statement += f"Saque registrado: R${amount:.2f}\n"
        return self._balance

    def getBankStatement(self):
        """
        Returns the full account statement

        Retorna o extrato completo
        """
        return self._statement

