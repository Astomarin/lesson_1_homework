while True:
    num1 = float(input("Введіть перше число: "))
    operation = input("Введіть операцію (+, -, *, /): ")
    num2 = float(input("Введіть друге число: "))

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
        break