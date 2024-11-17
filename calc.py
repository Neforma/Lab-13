while True:
    try:
        num1, num2 = map(int, input('Впишите 2 целых числа: ').split())
    except ValueError:
        print("Вы ввели не число. Попробуйте снова.")
    else:
        print('Выберите операцию:')
        print('', 'Сложение: +', '\n', 'Вычитание: -', '\n', 'Умножение: *', '\n', 'Деление: /')
        oper = input()

        if oper == '+':
            print(f'Сложение: {num1} + {num2} = {num1 + num2}')
        elif oper == '-':
            print(f'Вычитание: {num1} - {num2} = {num1 - num2}')
        elif oper == '*':
            print(f'Умножение: {num1} * {num2} = {num1 * num2}')
        elif oper == '/':
            if num2 != 0:
                print(f'Деление: {num1} / {num2} = {num1 / num2}')
            else:
                print('Ты че дурак что-ли?')

        else:
            print('Ты че ввёл?')
