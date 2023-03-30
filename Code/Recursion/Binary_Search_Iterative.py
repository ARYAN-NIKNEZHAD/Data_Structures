def binary_search_iterative(x, target):
    low = 0
    high = len(x) - 1
    while low <= high:
        mid = (low + high) // 2
        if target == x[mid]:
            return True
        elif target < x[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

lst = [i for i in range(100)]
print(binary_search_iterative(lst, 90))
