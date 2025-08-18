class Client:
    def __init__(self, address):
        self._address = address
        self._accounts = []

    def add_account(self, account):
        """
        Adds a new account to the client's list of accounts

        Adiciona uma nova conta à lista de contas do cliente
        """
        self._accounts.append(account)
    
    def account(self, position):
        """
        Returns the account at the specified position in the client's accounts list

        Retorna a conta na posição especificada da lista de contas do cliente
        """
        return self._accounts[position]
    
