def get_integer_input(prompt):
    while True:
        user_input = input('Введите число по горизонтали:')
        user_input = input('Введите число по вертикали:')
        try:
            return int(user_input)
        except ValueError:
            print("Ошибка: введите целое число!")

X_REPEAT = get_integer_input("Введите число ячеек по горизонтали: ")
Y_REPEAT = get_integer_input("Введите число ячеек по вертикали: ")

for i in range(Y_REPEAT):
    print(r'_ \ \ \_/ __' * X_REPEAT)
    print(r' \ \ \___/ _' * X_REPEAT)
    print(r'\ \ \_____/ ' * X_REPEAT)
    print(r'/ / / ___ \_' * X_REPEAT)
    print(r'_/ / / _ \__' * X_REPEAT)
    print(r'__/ / / \___' * X_REPEAT)