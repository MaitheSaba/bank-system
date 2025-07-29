import statement

MAX_DAILY_WITHDRAWAL = 3
limit = 500
withdrawal_count = 0

def withdrawal(amount):
    """
    Validates the requested withdrawal amount

    Valida o pedido de saque recebido (amount)
    """
    global withdrawal_count
    balance = statement.getBalance()
    if(balance < amount):
        return "Saldo insuficiente. Saque não efetuado."
    elif(amount > limit):
        return "Limite insuficiente. Saque não efetuado."
    elif(withdrawal_count == MAX_DAILY_WITHDRAWAL):
        return "Máximo de saques diários atingido. Saque não efetuado."
    elif(amount <= 0):
        return "Saque deve ser maior que R$0.00. Saque não efetuado."
    else:
        withdrawal_count += 1
        statement.setWithdrawal(amount)
        return f"Sacando R${amount:.2f}"

def deposit(amount):
    """
    Validates the requested deposit amount

    Valida o pedido de depósito recebido(amount)
    """
    if(amount <= 0):
        return "Depósito cancelado. Somente valores maiores que 0"
    else:
        statement.setDeposit(amount)
        return f"Depositando R${amount:.2f}"

def getBalance():
    """
    Returns the current account balance

    Retorna o saldo atual
    """
    return statement.getBalance()

def getTransactions():
    """
    Returns the full account statement

    Retorna o extrato completo
    """
    bank_statement = statement.getBankStatement()
    return f"{bank_statement}"