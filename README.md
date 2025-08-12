# 🪙 Bank System 
## Version 1 (commited July 29, 2025)
Basic banking system with functions for withdrawals, deposits and viewing account statement.
### Rules
#### Initial limit (per withdrawal) = R$ 500.00
#### Maximum of 3 daily withdrawals
### 💸 Withdrawal
  - Only positive amounts allowed
  - Withdrawal amount must not exceed the current balance
  - Withdrawal amount must not exceed the limit
  - Must not exceed daily withdrawals
### 💵 Deposits
  - Only positive amounts allowed

## Version 2 (commited from August 7 to August 12, 2025)
Function definitions with parameters and beginning of object-oriented programming.
Added features to create and view users, and to create and view accounts (related to those users). The connection between Version 1 and Version 2 functionalities hasn't been implemented yet.
### 👥 Users
  - Stored in a list
  - Name, birthdate, CPF (brazilian SSN; only digits stored) and address
  - Must have an unique CPF
  - Functions: create, get by CPF, get by index and get all
### 🔒 Accounts
  - Stored in a list
  - Must be related to one user exclusively (by CPF)
  - Multiple accounts per user allowed
  - Agency number (0001), sequential account number and account holder (user)
  - Functions: create, get all and get by user (through CPF)

#
# 🪙 Sistema bancário
## Primeira versão (commit em 29 de julho de 2025)
Sistema bancário básico com operações de saque, depósito e ver extrato.
### Regras
#### Limite inicial (por saque) = R$ 500.00
#### Máximo de 3 saques diários
### 💸 Saque
  - Somente valores positivos permitidos
  - Saque não pode ser maior que o saldo atual
  - Saque não pode ser maior que o limite
  - Não exceder a quantidade de saques diários
### 💵 Depósito
  - Somente valores positivos permitidos

## Segunda versão (commits de 7 de agosto a 12 de agosto de 2025)
Definição de funções com parâmetros e início do uso de orientação a objeto. 
Adição das funcionalidades de criar e ver usuários, criar e ver contas (associadas a esses usuários). Ainda não foi feita relação entre as funcionalidades da versão 1 e da versão 2.
### 👥 Usuários
  - Armazenados em lista
  - Nome, data de nascimento, CPF (somente números) e endereço
  - CPF único
  - Funções: criar, pesquisar por CPF, pesquisar por index e ver todos
### 🔒 Contas
  - Armazenadas em lista
  - Devem ser associadas a somente um usuário (atribuição pelo CPF)
  - Mesmo usuário pode ter várias contas
  - Agência fixa (0001), número da conta sequencial e usuário titular
  - Funções: criar, ver todas e pesquisar por CPF do usuário titular
