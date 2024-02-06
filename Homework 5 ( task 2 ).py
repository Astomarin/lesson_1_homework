while True:
    try:
        num1 = float(input("Введіть перше число: "))
        operation = input("Введіть операцію (+, -, *, /): ")

        while True:
            try:
                num2 = float(input("Введіть друге число: "))
                break  #додав для перевірки коректності числа, щоб не збивалося на перше число
            except ValueError:
                print("Помилка: Будь ласка, введіть коректне число.")

    except ValueError:
        print("Помилка: Будь ласка, введіть коректне число.")
        continue

    if operation == '+':
        result = num1 + num2
        print("Результат: ", result)
    elif operation == '-':
        result = num1 - num2
        print("Результат: ", result)
    elif operation == '*':
        result = num1 * num2
        print("Результат: ", result)
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print("Результат: ", result)
        else:
            print("Помилка: Неможливо ділити на 0.")
    else:
        print("Помилка: Невірна операція.")

    choice = input("Бажаєте продовжити (y/n)? ").lower()
    if choice != 'y':
        break
