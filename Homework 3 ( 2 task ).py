#list1 = [12, 3, 4, 10]
#list2 = [1]
#list3 = []
#list4 = [12, 3, 4, 10, 8]

def last_to_first(lst):
    if len(lst) > 1:
        lst = [lst[-1]] + lst[:-1]
    return lst

list1 = [55, 1, 18, 2]
print(last_to_first(list1))

list2 = [5]
print(last_to_first(list2))

list3 = []
print(last_to_first(list3))

list4 = [55, 1, 18, 2, 9]
print(last_to_first(list4))