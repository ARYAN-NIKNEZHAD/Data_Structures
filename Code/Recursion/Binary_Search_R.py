def binary_search_R(x, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == x[mid]:
            return True
        elif target < x[mid]:
            return binary_search_R(x, target, low, mid-1)
        else:
            return binary_search_R(x, target, mid+1, high)


lst = [i for i in range(1, 101)]
print(binary_search_R(lst, 90, 1, 100))