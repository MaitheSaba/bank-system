from client import Client

class NaturalPerson(Client):
    def __init__(self, address, name, cpf, birthdate):
        super().__init__(address)
        self._name = name
        self._cpf = cpf
        self._birthdate = birthdate
    
    def name(self):
        return self._name
    
    def cpf(self):
        return self._cpf
    
    @classmethod
    def getUserByCpf(cls, clients, cpf):
        """
        Searches for a user by "cpf" (unique).
        Returns the user found or None

        Busca o usuário pelo CPF.
        Retorna o usuário ou "None"
        """
        return next((user for user in clients if user.cpf() == cpf), None)

    @classmethod
    def getUserByIndex(self, clients, position):
        """
        Searches for a user by index

        Busca usuário por index (posição)
        """
        for i, user in enumerate(clients):
            if(i == position):
                return user
            
    def __str__(self):
        return f"Nome: {self._name}, CPF: {self._cpf}, Data de Nascimento: {self._birthdate}, Endereço: {self._address}"