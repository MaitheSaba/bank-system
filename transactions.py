from statement import Balance

MAX_DAILY_WITHDRAWAL = 3
limit = 500
balance = Balance()

def withdrawal(*, amount, withdrawal_count):
    """
    Validates the requested withdrawal amount

    Valida o pedido de saque recebido (amount)
    """
    current_balance = balance.getBalance()
    if current_balance < amount:
        return "Saldo insuficiente. Saque não efetuado.", current_balance, withdrawal_count
    elif amount > limit:
        return "Limite insuficiente. Saque não efetuado.", current_balance, withdrawal_count
    elif withdrawal_count == MAX_DAILY_WITHDRAWAL:
        return "Máximo de saques diários atingido. Saque não efetuado.", current_balance, withdrawal_count
    elif amount <= 0:
        return "Saque deve ser maior que R$0.00. Saque não efetuado.", current_balance, withdrawal_count
    else:
        withdrawal_count += 1
        new_balance = balance.setWithdrawal(amount)
        return f"Sacando R${amount:.2f}", new_balance, withdrawal_count

def deposit(amount, /):
    """
    Validates the requested deposit amount

    Valida o pedido de depósito recebido(amount)
    """
    if amount <= 0:
        return "Depósito cancelado. Somente valores maiores que 0", balance.getBalance()
    else:
        new_balance = balance.setDeposit(amount)
        return f"Depositando R${amount:.2f}", new_balance

def getBalance():
    """
    Returns the current account balance

    Retorna o saldo atual
    """
    return balance.getBalance()

def getTransactions(current_balance, /, *, bank_statement):
    """
    Returns the full account statement

    Retorna o extrato completo
    """
    current_balance = balance.getBalance()
    bank_statement = balance.getBankStatement()
    return f"{bank_statement}", current_balance
