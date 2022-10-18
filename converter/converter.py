import prompt

CM_IN_M = 100
MM_IN_CM = 10


def convert():
    data = [
        {
            'key': 1,
            'from_type': 'CM',
            'to_type': 'M',
            'handler': lambda number: number / CM_IN_M,
        },
        {
            'key': 2,
            'from_type': 'M',
            'to_type': 'CM',
            'handler': lambda number: number * CM_IN_M,
        },
        {
            'key': 3,
            'from_type': 'CM',
            'to_type': 'MM',
            'handler': lambda number: number * MM_IN_CM,
        },
        {
            'key': 4,
            'from_type': 'ММ',
            'to_type': 'СМ',
            'handler': lambda number: number / MM_IN_CM,
        },
    ]

    print('Типы конвертации:')
    for item in data:
        key = item.get('key')
        from_type = item.get('from_type')
        to_type = item.get('to_type')
        print(f'{key}. {from_type} -> {to_type}')

    convert_type = prompt.integer('Выберите тип конвертации:')

    number = prompt.real('Введите значение для перевода: ')

    for item in data:
        if convert_type == item.get('key'):
            converted_number = item.get('handler')(number)
            from_type = item.get('from_type')
            to_type = item.get('to_type')
            print(f'{number} {from_type} = {converted_number} {to_type}')
            return

    raise 'Неизвестный тип конвертации'
