Summ_1 = [0, 4, 8, 3, 5, 9]
Summ_2 = [2, 6, 9]
Summ_3 = [2]
Zero = []


def multiply_summ(arr):
    return sum(arr[0::2]) * arr[-1] if arr else 0

result1 = multiply_summ(Summ_1)
result2 = multiply_summ(Summ_2)
result3 = multiply_summ(Summ_3)
result4 = multiply_summ(Zero)
print(result1)
print(result2)
print(result3)
print(result4)
