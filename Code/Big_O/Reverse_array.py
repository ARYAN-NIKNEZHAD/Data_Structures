import time

def reverse_array(array):
    length = len(array)
    new_array = [None] * length
    for i in range(length):
        new_array[length - 1 - i] = array[i]
    return new_array



def reverse_array_2(array):
    return array[::-1]


arr = [i for i in range(1000000)]

# start = time.process_time()
# print(reverse_array(arr))
# end = time.process_time()

# actual_time = end - start
# print(actual_time)



start = time.process_time()
print(reverse_array_2(arr))
end = time.process_time()

actual_time = end - start
print(actual_time)
