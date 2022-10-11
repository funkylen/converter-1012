CM_IN_M = 100

def convert():
    # Сантиметры в метры
    number_input = int(input('Введите значение для перевода: '))

    # Формула? 
    number_input = number_input / CM_IN_M
    
    print(number_input)