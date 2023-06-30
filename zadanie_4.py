import json

class User:
    def __init__(self, name, id, levelAccess) -> None:
        self.name = name
        self.id = id
        self.levelAccess = levelAccess
    
    def __str__(self) -> str:
        return f'Имя:{self.name}, ID:{self.id}, уровень доступа:{self.levelAccess}'
    
    def __repr__(self) -> str:
        return f'User("{self.name}","{self.id}",{self.levelAccess})'
    

def loadUsers(fileName):
    data = []
    res = []
    with open(fileName, "r") as f:
        data = json.load(f)
    for i in data:
        res.append(User(i["name"], i["id"], i["levelAccess"]))
    return res

if __name__=="__main__":
    users = loadUsers("TesT_13/users.json")
    print(users)

