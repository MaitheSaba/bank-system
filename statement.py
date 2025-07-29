balance = 0.0
bank_statement = ""

def setDeposit(amount):
    """
    Adds the given amount to the balance and logs the deposit

    Aumenta o saldo, depositando o valor recebido (amount), e registra o depósito
    """
    global balance, bank_statement
    balance += amount
    bank_statement += f"Depósito registrado: R${amount:.2f}\n"

def setWithdrawal(amount):
    """
    Subtracts the given amount from the balance and logs the withdrawal

    Diminui o saldo, 'sacando' o valor recebido (amount), e registra o saque
    """
    global balance, bank_statement
    balance -= amount
    bank_statement += f"Saque registrado: R${amount:.2f}\n"

def getBankStatement():
    """
    Returns the full account statement

    Retorna o extrato completo
    """
    return bank_statement

def getBalance():
    """
    Returns the current account balance

    Retorna o saldo atual
    """
    return balance

