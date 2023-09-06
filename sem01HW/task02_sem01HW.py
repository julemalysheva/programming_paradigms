# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

def sort_numbers(numbers):
    return sorted(numbers, reverse=True)

# Пример использования:
numbers = [5, 2, 8, 3, 1, 7]
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)  # Вывод: [8, 7, 5, 3, 2, 1]