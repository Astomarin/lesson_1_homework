def print_digits(number):
    if not (isinstance(number, int) and 1000 <= number <= 9999):
        print("Треба ввести 4-ох значне число")
        return

    print(number // 1000)
    print((number % 1000) // 100)
    print((number % 100) // 10)
    print(number % 10)

try:
    user_input = int(input("Введіть 4-ох значне число: "))
    print_digits(user_input)
except ValueError:
    print("Помилка, це не 4-ох значне число")