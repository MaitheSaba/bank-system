import transactions

menu = """
Escolha uma opção:
    1 - Sacar
    2 - Depositar
    3 - Ver extrato
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
    elif option == '0':
        break
    else:
        print("Opção inválida")

print("Encerrando sistema...")