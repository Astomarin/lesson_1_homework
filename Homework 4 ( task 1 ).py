#[0, 1, 0, 12, 3]
#[0]
#[1, 0, 13, 0, 0, 0, 5]
#[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]

list_zero_end = [11, 0, 12, 13, 0, 55, 0, 35, 0, 95, 0, 0, 96, 0]
def zero_to_end(lst):
    non_zero = [num for num in lst if num != 0]
    zero = [0] * (len(lst) - len(non_zero))
    result = non_zero + zero
    return result


result4 = zero_to_end(list_zero_end)
print(result4)
