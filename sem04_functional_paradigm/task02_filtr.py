'''Фильтрация данных/
Контекст
Предположим, что есть какой-то массив содержащий данные о разных людях и их возрасте и вас
попросили ответить на следующий вопрос: “сколько в массиве людей возраста > 30?”. Для этого, 
вы хотите написать программу для фильтрации наблюдений по возрастному признаку.
● Ваша задача
Написать скрипт принимающий на вход массив с данными о людях и число - возраст, 
а возвращающий число - количество людей старше указанного возраста.
● Решение.. ?
'''

def filter_by_age(people, age):
    filtered_people = filter(lambda x: x['age'] > age, people)
    return len(list(filtered_people))

people = [
    {'name': 'Alla', 'age': 25},
    {'name': 'Ivan', 'age': 40},
    {'name': 'Vika', 'age': 35},
    {'name': 'Julia', 'age': 30}
]

count = filter_by_age(people, 30)
print(count)  

'''
def filter_by_age_1(people, age):
    return sum(map(lambda x: x.get("age", -1) > age, people))
'''

'''
def filter_persons(persons: list[str], border_age: int) -> list[str]:
    return list(filter(lambda person: int(person.split(";")[1].strip()) > border_age, persons))


persons_lst = ["Иванов И.И.; 20", "Петров П.П.; 35", "Мухаммедова Э.З.; 45"]

print(persons_lst)
print(filter_persons(persons_lst, 30))

a = "  \n\t  123   \t\n\n\t"

print([a])
print([a.strip()])
print([a.lstrip()])
print([a.rstrip()])
'''