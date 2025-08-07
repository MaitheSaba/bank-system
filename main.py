import transactions
import users

menu = """
Escolha uma opção:
    1 - Sacar
    2 - Depositar
    3 - Ver extrato
    4 - Criar usuário
    5 - Criar conta corrente
    6 - Ver usuários
    0 - Sair
=>"""

while True:
    balance = transactions.getBalance()
    option = input(menu)
    if option == '1':
        print(f"Saldo disponível: R$ {balance:.2f}")
        amount = float(input("Informe o valor do saque: ")) 
        print(transactions.withdrawal(amount))
    elif option == '2':
        amount = float(input("Informe quanto deseja depositar: "))
        print(transactions.deposit(amount))
    elif option == '3':
        bank_statement = transactions.getTransactions()
        print("EXTRATO".center(21, "="))
        print("Não foram realizadas transações"if not bank_statement else bank_statement)
        print(f"Saldo disponível: R${balance:.2f}")
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
        break
    elif option == '6':
        all_users = users.getUsers()
        for i,user in enumerate(all_users):
            print(f"{i + 1} - {user["name"]}")
        details = int(input("Escolha uma opção para ver detalhes ou '0' para sair: "))
        if details != 0:
            user = users.getUserByIndex(details - 1)
            if user:
                print("==============================")
                print(f"""Nome: {user["name"]}\nData de nascimento: {user["birthdate"]}\nCPF: {user["cpf"]}\nEndereço: {user["address"]}""")
            else:
                print("Usuário não encontrado")
    elif option == '0':
        break
    else:
        print("Opção inválida")

print("Encerrando sistema...")