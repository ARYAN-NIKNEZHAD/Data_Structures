

def unique_name(string):
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j]:
                return False
    return True

print(unique_name("aryan"))
print(unique_name("sara"))
