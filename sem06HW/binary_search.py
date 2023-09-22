import random;

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    found = False
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            found = True
            break
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    if found:
        return mid
    else:
        return None


def create_random_sort_list(length, min_value, max_value):
    random_list = []
    for _ in range(length):
        random_list.append(random.randint(min_value, max_value))
    random_list.sort()    
    return random_list


random_list = create_random_sort_list(10, 10, 20)
print(f'Список {random_list}')   
print(f'Индекс элемента 15 в списке: {binary_search(random_list, 15)}') 


