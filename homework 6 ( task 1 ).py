people = [
    {"name": "Yakiv", "age": 24},
    {"name": "Emiliya", "age": 40},
    {"name": "Mykhailo", "age": 33},
    {"name": "Sofiya", "age": 19},
    {"name": "Yevheniya", "age": 31},
    {"name": "Nicholas", "age": 24},
    {"name": "Olha", "age": 33}
]
min_age = min(person["age"] for person in people)
most_min_age = [person["name"] for person in people if person["age"] == min_age]

max_name_len = max(len(person["name"]) for person in people)
most_long_name = [person["name"] for person in people if len(person["name"]) == max_name_len]

summ_age = sum(person["age"] for person in people) / len(people)

print("Task1) Наймолодша людина: ", most_min_age)
print("Task2) Найдовше ім'я: ", most_long_name)
print("Task3) Середній рік: ", summ_age)
