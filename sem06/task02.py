'''Контекст
Предположим, у нас есть модель, которая предсказывает прогноз продаж, и теперь мы хотим оценить
насколько модель точно это делает. Для получения оценки “точности” модели можно использовать
много разных метрик. Одна из популярных метрик - это “среднеквадратичная ошибка” (mean squared
error или MSE).
● Пусть у нас есть два массива длины n: один с предсказаниями нашей модели - Ŷ, а другой с истиной
(правильными ответами) - Y. Тогда можно вычислить MSE по простой формуле.
● Ваша задача
Реализовать процедуру для вычисления MSE на любом языке в любой парадигме. Программа получает
на вход два вектора и возвращает число - оценку MSE для этих векторов.

'''

import random


def mse(arr1, arr2):
    assert len(arr1) == len(arr2), "Длина массивов должна совпадать"
    sum_diff_x_y = sum(map(lambda x, y: (x-y)**2, arr1, arr2))

    return round(sum_diff_x_y/len(arr1),2)


def main():
    array_x, array_y = [], []
    for i in range(7):
        array_x.append(random.randint(0, 10))
        # array_y.append(random.randint(0, 10))
    for i in range(7):
        # array_x.append(random.randint(0, 10))
        array_y.append(random.randint(0, 10))
    
    print(f'Array of X: {array_x} \nArray of Y: {array_y}')
    print(f'\nMSE = {mse(array_x, array_y)}')


if __name__ == "__main__":
    main()