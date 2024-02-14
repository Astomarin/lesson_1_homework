my_dict_1 = {1: 1, 2: 2, 3: 3}
my_dict_2 = {11: 11, 2: 22, 3: 33}


common_keys = list(set(my_dict_1.keys()) & set(my_dict_2.keys()))
first_dict_keys = list(set(my_dict_1.keys()) - set(my_dict_2.keys()))
new_dict = {key: my_dict_1[key] for key in first_dict_keys if key not in my_dict_2}
merged_dict = {}

for key in my_dict_1.keys():
    if key in my_dict_2:
        merged_dict[key] = [my_dict_1[key], my_dict_2[key]]
    else:
        merged_dict[key] = my_dict_1[key]

for key in my_dict_2.keys():
    if key not in my_dict_1:
        merged_dict[key] = my_dict_2[key]


print("а) Список з ключами, які є в обох діктах:", common_keys)
print("б) Список ключей, які є в першому але немає в другому", first_dict_keys)
print("в) Новий словник з ключами, які є в першому, але немає в другому словнику:", new_dict)
print("г) Об'єднані словники:", merged_dict)

