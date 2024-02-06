import string
import keyword

print(keyword.kwlist) #це сугубо для мене


user_input = input("Потрібно ввести ім'я змінної: ")

if user_input.isdigit() or user_input[0].isdigit():
    print(False)
else:
    allowed_characters = string.ascii_letters + string.digits + "_"
    if any(char not in allowed_characters for char in user_input):
        print(False)
    elif user_input in keyword.kwlist:
        print(False)
    else:
        print(True)
