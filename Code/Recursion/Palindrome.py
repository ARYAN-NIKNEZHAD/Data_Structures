def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

print(is_palindrome("radar"))


def is_palindrome2(s):
    for i in range(len(s) // 2):
        if s[i] != s[-i-1]:
            return False
    return True

print(is_palindrome2("radar"))