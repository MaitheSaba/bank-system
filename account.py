class Account:
    _agency = "0001"
    def __init__(self, client, number, statement = "", balance=0.0):
        self._client = client
        self._number = number
        self._statement = statement
        self._balance = balance

    def balance(self):
        return self._balance
            
    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account and logs the withdrawal into the statement

        Saca o valor informado da conta e registra o saque no extrato
        """
        old_balance = self._balance
        self._balance -= amount
        self._statement += f"Saque registrado: R${amount:.2f}\n"
        if(old_balance > self._balance):
            return True, f"Sacando R${amount:.2f}"
        else:
            return False, "Algo deu errado, tente novamente"

    def deposit(self, amount):
        """
        Deposits the specified amount into the account and logs the deposit into the statement
          
        Deposita o valor informado na conta e registra o depósito no extrato
        """
        old_balance = self._balance
        self._balance += amount
        self._statement += f"Depósito registrado: R${amount:.2f}\n"
        if(old_balance < self._balance):
            return True, f"Depositando R${amount:.2f}"
        else:
            return False, "Algo deu errado, tente novamente"
        
    def statement(self):
        """
        Returns the full account statement

        Retorna o extrato completo
        """
        return self._statement
    
    @classmethod
    def getAccountsByUser(self, accounts, cpf):
        """
        Receives a CPF value related to an user and all accounts registered
        Returns all accounts from the related account holder

        Recebe um valor de CPF relacionado a um usuário e todas as contas registradas
        Retorna todas as contas do titular relacionado a esse CPF
        """
        user_accounts = []
        for account in accounts:
            if(account._client.cpf() == cpf):
                user_accounts.append(account)
        return user_accounts
    
    def __str__(self):
        return f"Agência: {self._agency}, C/C: {self._number}, Titular: {self._client.name()}, Saldo: R${self._balance:.2f}"