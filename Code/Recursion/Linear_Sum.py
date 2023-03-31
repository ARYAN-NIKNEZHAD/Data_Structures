def linear_sum(sequence, n):
    if n == 0:
        return 0
    else:
        return linear_sum(sequence, n-1) + sequence[n-1]
    
lst = [i for i in range(1, 11)]
print(linear_sum(lst, len(lst)))