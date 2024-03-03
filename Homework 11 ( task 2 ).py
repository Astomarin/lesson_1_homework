def is_even(number):
    return not number & 1

## def is_even(number):
##    return bin(number)[-1] == '0'
## Це другий сбосіб як це вирішити, як для мене перший більш простий

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')
