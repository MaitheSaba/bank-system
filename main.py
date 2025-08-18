from checking_account import CheckingAccount as ca
from withdrawal import Withdrawal as wd
from deposit import Deposit as dp
from person import NaturalPerson as np

def menu():
    print("MENU".center(20, "="))
    option = input("""1 - Sacar\n2 - Depositar\n3 - Ver extrato\n4 - Criar cliente\n5 - Criar conta corrente\n6 - Ver clientes\n7 - Buscar contas\n0 - Sair\n=> """)
    return option

def withdraw(clients, accounts):
    cpf = int(input("Informe o CPF do titular (somente números): "))
    client = np.getUserByCpf(clients, cpf)
    if client:
        client_accounts = ca.getAccountsByUser(accounts, cpf)
        if client_accounts:
            account_choice = -1
            while account_choice <= 0 or account_choice > len(client_accounts) - 1:
                for i,account in enumerate(client_accounts):
                    print(f"{i + 1} - {account}")
                account_choice = int(input("Escolha uma conta ou '0' para sair: ")) - 1
                if account_choice == -1:
                    break
                elif(account_choice < 0 or account_choice > len(client_accounts) - 1):
                    print("Opção inválida")
                else:
                    account = client.account(account_choice)
                    print(f"Saldo disponível: R$ {account.balance():.2f}")
                    amount = float(input("Informe o valor do saque: ")) 
                    withdraw = wd(amount)
                    status, message = withdraw.register(account)
                    print(message)
                    new_balance = account.balance()
                    print(f"Saldo: R${new_balance:.2f}")                    
        else:
            print("Esse cliente não possui contas vinculadas")
    else:
        print("Cliente não encontrado")

def deposit(clients, accounts):
    cpf = int(input("Informe o CPF do titular (somente números): "))
    client = np.getUserByCpf(clients, cpf)
    if client:
        client_accounts = ca.getAccountsByUser(accounts, cpf)
        if client_accounts:
            account_choice = -1
            while account_choice <= 0 or account_choice > len(client_accounts) - 1:
                for i,account in enumerate(client_accounts):
                    print(f"{i + 1} - {account}")
                account_choice = int(input("Escolha uma conta ou '0' para sair: ")) - 1
                if account_choice == -1:
                    break
                elif(account_choice < 0 or account_choice > len(client_accounts) - 1):
                    print("Opção inválida")
                else:  
                    account = client.account(account_choice)
                    amount = float(input("Informe quanto deseja depositar: "))
                    deposit = dp(amount) 
                    status, message = deposit.register(account)
                    print(message)
                    new_balance = account.balance()
                    print(f"Saldo: R${new_balance:.2f}")
        else:
            print("Esse cliente não possui contas vinculadas")
    else:
        print("Cliente não encontrado")

def show_statement(clients, accounts):
    cpf = int(input("Informe o CPF do titular (somente números): "))
    client = np.getUserByCpf(clients, cpf)
    if client:
        client_accounts = ca.getAccountsByUser(accounts, cpf)
        if client_accounts:
            account_choice = -1
            while account_choice <= 0 or account_choice > len(client_accounts) - 1:
                for i,account in enumerate(client_accounts):
                    print(f"{i + 1} - {account}")
                account_choice = int(input("Escolha uma conta ou '0' para sair: ")) - 1
                if account_choice == -1:
                    break
                elif(account_choice < 0 or account_choice > len(client_accounts) - 1):
                    print("Opção inválida")
                else: 
                    account = client.account(account_choice)
                    bank_statement = account.statement()
                    print("EXTRATO".center(21, "="))
                    print("Não foram realizadas transações"if not bank_statement else bank_statement)
                    new_balance = account.balance()
                    print(f"Saldo disponível: R${new_balance:.2f}")
        else:
            print("Esse cliente não possui contas vinculadas")
    else:
        print("Cliente não encontrado")

def add_client(clients):
    cpf = int(input("Informe o CPF (somente números): "))
    client = np.getUserByCpf(clients, cpf)
    if client:
        print("CPF já cadastrado!")
    else:
        name = input("Nome completo: ")
        birthdate = input("Data de nascimento (dd-mm-aaaa): ")
        street = input("Rua: ")
        number = input("Número: ")
        additional = input("Complemento: ")
        district = input("Bairro: ")
        city = input("Cidade: ")
        state = input("Sigla do estado: ")
        address = f"{street}, {number} - {additional} - {district} - {city}/{state}"
        new_client = np(address=address, name=name, cpf=cpf, birthdate=birthdate)
        clients.append(new_client)
        print("Usuário cadastrado com sucesso!")

def add_account(clients, accounts):
    cpf = int(input("Informe o CPF do titular (somente números): "))
    account_holder = np.getUserByCpf(clients, cpf)
    if account_holder:
        number = len(accounts) + 1
        new_account = ca(account_holder, number)
        account_holder.add_account(new_account)
        accounts.append(new_account)
        print("Conta cadastrada com sucesso!")
    else:
        print("CPF para o titular não encontrado.")

def show_clients(clients, accounts):
    if len(clients) > 0:
        for i,client in enumerate(clients):
            print(f"{i + 1} - {client.name()}")
        details = int(input("Escolha uma opção para ver detalhes ou '0' para sair: "))
        if details != 0:
            client = np.getUserByIndex(clients, details - 1)
            if client:
                client_accounts = ca.getAccountsByUser(accounts, client.cpf())
                print("==============================")
                print(client)
                print("----- CONTAS DO USUÁRIO -----")
                if client_accounts:
                    for account in client_accounts:
                        print(account)
                else:
                    print("Esse usuário ainda não possui contas vinculadas")
            else:
                print("Usuário não encontrado")
    else:
        print("Nenhum usuário cadastrado")

def show_accounts(clients, accounts):
    cpf = int(input("Informe o CPF do titular(somente números) ou '0' para ver todos registros: "))
    if cpf != 0:
        account_holder = np.getUserByCpf(clients, cpf)    
        accounts = ca.getAccountsByUser(accounts, cpf) if account_holder else None
    if accounts:
        for account in accounts:
            print("====================")
            print(account)
    else:
        print("Nenhuma conta encontrada para esse titular.")

clients = []
accounts = []
while True:
    option = menu()

    if option == '1':
        if clients:
            withdraw(clients, accounts)
        else:
            print("Nenhum cliente cadastrado. Por favor, crie um cliente primeiro.")
    elif option == '2':
        if clients:
            deposit(clients, accounts)
        else:
            print("Nenhum cliente cadastrado. Por favor, crie um cliente primeiro.")
    elif option == '3':
        if clients:
            show_statement(clients, accounts)
        else:
            print("Nenhum cliente cadastrado. Por favor, crie um cliente primeiro.")
    elif option == '4':
        add_client(clients)
    elif option == '5':
        add_account(clients, accounts)
    elif option == '6':
        show_clients(clients, accounts)
    elif option == '7':
        if accounts:
            show_accounts(clients, accounts)
        else:
            print("Nenhuma conta cadastrada.")
    elif option == '0':
        break
    else:
        print("Opção inválida")

print("Encerrando sistema...")