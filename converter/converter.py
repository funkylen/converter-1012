CM_IN_M = 100

def convert():
    print("Типы конвертации: \n 1. Сантиметры в метры\n 2. Метры в сантиметры")
    
    convert_type = int(input('Выберите тип конвертации:'))

    number = int(input('Введите значение для перевода: '))

    if convert_type == 1:
        converted_number = number / CM_IN_M
        from_type = 'CM'
        to_type = 'M'
    elif convert_type == 2:
        converted_number = number * CM_IN_M
        from_type = 'M'
        to_type = 'CM'
    else:
        raise 'Неизвестный тип конвертации'

    print(f'{number} {from_type} = {converted_number} {to_type}')