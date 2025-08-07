accounts = []
AGENCY = "0001"

def setAccount(user):
    account_number = len(accounts) + 1
    accounts.append({"agency": AGENCY, "account_number" : account_number, "account_holder":user})

def getAccounts():
    return accounts

def getAccountsByUser(cpf):
    user_accounts = []
    for account in accounts:
        if(account["account_holder"]["cpf"] == cpf):
            user_accounts.append(account)
    return user_accounts