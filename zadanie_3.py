

class MyBaseException(Exception):
    pass

class LevelException(MyBaseException):
    def __init__(self, value):
        self.value = value
    def __str__(self) -> str:
        return f'Неправильный уровень {self.value}'

class AccessException(MyBaseException):
    def __init__(self, value):
        self.value = value
    def __str__(self) -> str:
        return f'Ошибка доступа {self.value}'


