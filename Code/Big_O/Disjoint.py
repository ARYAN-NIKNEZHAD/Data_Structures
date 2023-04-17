

def disjoint(arr, arr2, arr3):
    for i in arr:
        for j in arr2:
            for k in arr3:
                if i == j == k:
                    return False
    return True










def disjoint2(arr, arr2, arr3):
    for i in arr:
        for j in arr2:
            if i == j:
                for k in arr3:
                    if i == k:
                        return False
    return True



print(disjoint2([1, 2], [1, 5], [2, 8]))
