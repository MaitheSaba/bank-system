users = []

def setUser(**kwargs):
    users.append(kwargs)

def getUserByCpf(cpf):
    return next((user for user in users if user["cpf"] == cpf), None)

def getUserByIndex(position):
    for i, user in enumerate(users):
        if(i == position):
            return user
        
def getUsers():
    return users