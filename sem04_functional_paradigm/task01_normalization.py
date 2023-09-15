'''Нормализация данных
Ваша задача
Реализовать с использованием функциональной парадигмы процедуру normalization, которая выполняет
нормализацию полученного массива по приведенной формуле нормализованного значения элемента, где
○ x_norm - нормализованное значение элемента
○ x - исходное значение элемента
○ x_max, x_min - максимальное и минимальное значение в массиве
Формула: x_norm = (x - x_min) / (x_max - x_min)
'''
def normalization(arr):
    x_min = min(arr)
    x_max = max(arr)

    return list(map(lambda x: (x - x_min) / (x_max - x_min), arr))


def normalization3(arr):
    x_min = min(arr)
    x_max = max(arr)
    return [(x - x_min) / (x_max - x_min) for x in arr]


def normalization2(arr):
    x_min = min(arr)
    x_max = max(arr)

    def normalize(x):
        return (x - x_min) / (x_max - x_min)

    return list(map(normalize, arr))    

def normalization(arr):
    x_min = min(arr)
    x_max = max(arr)

    return list(map(lambda x: (x - x_min) / (x_max - x_min), arr))


arr = [5, 10, 15, 20]

normalized_arr = normalization(arr)
print(normalized_arr)    

normalized_arr2 = normalization2(arr)
print(normalized_arr2)    

# проверяющие утилиты mypy, flake8, bandit

