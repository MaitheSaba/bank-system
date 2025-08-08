accounts = []
AGENCY = "0001"

def setAccount(user):
    """
    Receives the user that will be the account holder
    Gets the account number and sets a new account with these information

    Recebe o usuário que vai ser o titular da conta
    Define o número da conta e adiciona uma nova conta com essas informações
    """
    account_number = len(accounts) + 1
    accounts.append({"agency": AGENCY, "account_number" : account_number, "account_holder":user})

def getAccounts():
    """
    Returns all accounts

    Retorna todas as contas
    """
    return accounts

def getAccountsByUser(cpf):
    """
    Receives a CPF value related to an user
    Returns all accounts from the related account holder

    Recebe um valor de CPF relacionado a um usuário
    Retorna todas as contas do titular relacionado a esse CPF
    """
    user_accounts = []
    for account in accounts:
        if(account["account_holder"]["cpf"] == cpf):
            user_accounts.append(account)
    return user_accounts