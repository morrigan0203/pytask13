

def getValue(dict, key, defaultValue):
    try:
        return dict[key]
    except KeyError as e:
        print(f'Такого ключа {key} нет в этом словаре,возвращаем значение по умолчанию {defaultValue}')
        return defaultValue


if __name__=="__main__":

    d = {1:"1", 2:"2", 3:"3", 4:"4"}
    print(getValue(d, 2, "2__"))
    print(getValue(d, 6, "6__"))
