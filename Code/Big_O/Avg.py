

def avg(string):
    length = len(string)
    arr = [0] * length
    for i in range(length):
        total = 0
        for j in range(i + 1):
            total += string[j]
        arr[i] = total / (i + 1)

    return arr


arr = [17, 18, 10]

print(avg(arr))




def avg2(array):
    length = len(array)
    arr = [0] * length
    total = 0

    for i in range(length):
        total += array[i]
        arr[i] = total / (i + 1)

    return arr




arr = [17, 18, 10]

print(avg2(arr))