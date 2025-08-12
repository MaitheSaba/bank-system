import transactions
import users
import accounts as acc

def menu():
    print("MENU".center(20, "="))
    option = input("""1 - Sacar\n2 - Depositar\n3 - Ver extrato\n4 - Criar usuário\n5 - Criar conta corrente\n6 - Ver usuários\n7 - Buscar contas\n0 - Sair\n=> """)
    return option

withdrawal_count = 0

while True:
    balance = transactions.getBalance()
    option = menu()

    if option == '1':
        print(f"Saldo disponível: R$ {balance:.2f}")
        amount = float(input("Informe o valor do saque: ")) 
        message, new_balance, withdrawal_count = transactions.withdrawal(amount=amount, withdrawal_count=withdrawal_count)
        print(message, f"| Saldo: R${new_balance:.2f}")

    elif option == '2':
        amount = float(input("Informe quanto deseja depositar: "))
        message, new_balance = transactions.deposit(amount)
        print(message, f"| Saldo: R${new_balance:.2f}")

    elif option == '3':
        bank_statement = ""
        bank_statement, new_balance = transactions.getTransactions(balance, bank_statement=bank_statement)
        print("EXTRATO".center(21, "="))
        print("Não foram realizadas transações"if not bank_statement else bank_statement)
        print(f"Saldo disponível: R${new_balance:.2f}")

    elif option == '4':
        cpf = int(input("Informe o CPF (somente números): "))
        if users.getUserByCpf(cpf):
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
            users.setUser(name=name, birthdate=birthdate, cpf=cpf, address=address)
            print("Usuário cadastrado com sucesso!")

    elif option == '5':
        cpf = int(input("Informe o CPF do titular (somente números): "))
        account_holder = users.getUserByCpf(cpf)
        if account_holder:
            acc.setAccount(account_holder)
            print("Conta cadastrada com sucesso!")
        else:
            print("CPF para o titular não encontrado.")

    elif option == '6':
        all_users = users.getUsers()
        if all_users:
            for i,user in enumerate(all_users):
                print(f"{i + 1} - {user["name"]}")
            details = int(input("Escolha uma opção para ver detalhes ou '0' para sair: "))
            if details != 0:
                user = users.getUserByIndex(details - 1)
                if user:
                    user_accounts = acc.getAccountsByUser(user["cpf"])
                    print("==============================")
                    print(f"""Nome: {user["name"]}\nData de nascimento: {user["birthdate"]}\nCPF: {user["cpf"]}\nEndereço: {user["address"]}""")
                    print("----- CONTAS DO USUÁRIO -----")
                    if user_accounts:
                        for account in user_accounts:
                            print(f"Agência: {account["agency"]} - C/C: {account["account_number"]} - Titular: {account["account_holder"]["name"]}")
                    else:
                        print("Esse usuário ainda não possui contas vinculadas")
                else:
                    print("Usuário não encontrado")
        else:
            print("Nenhum usuário cadastrado")

    elif option == '7':
        cpf = int(input("Informe o CPF do titular(somente números) ou '0' para ver todos registros: "))
        if cpf == 0:
            accounts = acc.getAccounts()
        else:
            account_holder = users.getUserByCpf(cpf)    
            accounts = acc.getAccountsByUser(cpf) if account_holder else None
        if accounts:
            for account in accounts:
                print("====================")
                print(f"Agência: {account["agency"]} - C/C: {account["account_number"]} - Titular: {account["account_holder"]["name"]}")
        else:
            print("Nenhuma conta encontrada.")

    elif option == '0':
        break
    else:
        print("Opção inválida")

print("Encerrando sistema...")