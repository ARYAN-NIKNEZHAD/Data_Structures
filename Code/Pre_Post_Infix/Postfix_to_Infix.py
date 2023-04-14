from pythonds.basic import Stack

def postfix_to_infix(exp):
    s = Stack()
    for k in exp:
        if k.isalpha():
            s.push(k)
        elif k in ["+", "-", "*", "/"]:
            b = s.pop()
            a = s.pop()
            s.push("(" + a + k + b + ")")
    return s.pop()


print(postfix_to_infix('ABC+*'))
