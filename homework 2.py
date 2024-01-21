number = int(input("Введіть 4-значне число: "))

print(number // 1000)
print((number % 1000) // 100)
print((number % 100) // 10)
print(number % 10)