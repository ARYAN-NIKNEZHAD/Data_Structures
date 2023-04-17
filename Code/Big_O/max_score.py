
def max_score(lst):
    x = lst[0]
    for i in range(len(lst)):
        if lst[i] > x:
            x = lst[i]
    return x


lst = [1, 3, 5, 9]
print(max_score(lst))
