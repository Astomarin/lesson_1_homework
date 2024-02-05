#[0, 1, 0, 12, 3]
#[0]
#[1, 0, 13, 0, 0, 0, 5]
#[9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]


def zero_to_end(lst):
    non_zero = [num for num in lst if num != 0]
    zero = [0] * (len(lst) - len(non_zero))
    result = non_zero + zero
    return result

arr1 = [1, 5, 0, 0, 53]
result1 = zero_to_end(arr1)
print(result1)
arr2 = [0]
result2 = zero_to_end(arr2)
print(result2)
arr3 = [10, 1, 0, 0, 0, 0, 55]
result3 = zero_to_end(arr3)
print(result3)
arr4 = [11, 0, 12, 13, 0, 55, 0, 35, 0, 95, 0, 0, 96, 0]
result4 = zero_to_end(arr4)
print(result4)
