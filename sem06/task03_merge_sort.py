def merge_sorting(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sorting(lst[:mid])
    right = merge_sorting(lst[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    return result + left[i:] + right[j:]


lst = [2, 8, 9, 7, 45, 7, 0, 14]        
print(merge_sorting(lst))