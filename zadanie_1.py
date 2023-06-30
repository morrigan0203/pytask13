

def getNum() -> int:
    num = None
    while True:
        try:
            num = float(input("Введите число : "))
            break
        except ValueError as e:
            print(f'Ваш ввод привёл к ошибке ValueError: {e}')
    return num

if __name__=="__main__":
    print(getNum())

