users = []

def setUser(**kwargs):
    """
    Sets a new user

    Adiciona um novo usuário
    """
    users.append(kwargs)

def getUserByCpf(cpf):
    """
    Searches for a user by "cpf" (unique).
    Returns the user found or None

    Busca o usuário pelo CPF.
    Retorna o usuário ou "None"
    """
    return next((user for user in users if user["cpf"] == cpf), None)

def getUserByIndex(position):
    """
    Searches for a user by index

    Busca usuário por index (posição)
    """
    for i, user in enumerate(users):
        if(i == position):
            return user
        
def getUsers():
    """
    Returns all users

    Retorna todos usuários
    """
    return users