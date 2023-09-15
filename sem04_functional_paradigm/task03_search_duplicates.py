'''Контекст
Важнейшая задача в анализе данных - поиск дубликатов. Дубликат - это наблюдение, встречающееся в
данных больше одного раза. Такие наблюдения не просто не улучшают результат анализа или
полученных моделей, но и замедляют весь процесс в целом, поэтому аналитики и разработчики
предпочитают избавляться от них перед тем как приступить к анализу.
● Ваша задача
Реализовать с использованием функциональной парадигмы процедуру для поиска дубликатов. На вход
подается массив, где могут присутствовать дубликаты (а могут и не присутствовать). При применении к
массиву, дубликаты должны быть выведены на экран в виде списка.
● Решение.. ?
'''

def search_duplicates(arr):
    uniq_set = set()
    duplicates = list(filter(lambda x: x in uniq_set or uniq_set.add(x), arr))
    return duplicates
 

def find_duplicates(arr):
    seen = set()
    duplicates = []
    for item in arr:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates    

def find_duplicates2(arr):
    duplicates = list(filter(lambda x: arr.count(x) > 1, set(arr)))
    return duplicates    

def search_duplicates(arr):
    uniq_set = set()
    return list(set(filter(lambda x: x in uniq_set or uniq_set.add(x), arr)))

arr = [2, 3, 4, 2, 1, 5, 6, 4, 7, 8, 3, 1]

duplicates = search_duplicates(arr)
print(duplicates)  

duplicates2 = find_duplicates(arr)
print(duplicates2)  

duplicates3 = find_duplicates2(arr)
print(duplicates3)  

'''
его вариант
def search_duplicates(arr):
    count_items = {}
    for item in arr:
        count_items.setdefault(item, 0)
        count_items[item] += 1
    return list(set(filter(lambda x: count_items[x] > 1, arr)))

arr = [8, 4, 7, 0, 4, 0, 10, 4, 7, 4]

duplicates = search_duplicates(arr)
print(duplicates)

***********************
def search_duplicates(arr):
    count_items = {}
    for item in arr:
        count_items.setdefault(item, 0)
        count_items[item] += 1
    return list(filter(lambda x: count_items[x] > 1, count_items))


arr = [8, 4, 7, 0, 4, 0, 10, 4, 7, 4]

duplicates = search_duplicates(arr)
print(duplicates)
'''