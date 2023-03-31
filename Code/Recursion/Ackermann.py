def ackermann(a, b, s="%s"):
    print(s %("A(%d, %d)" %(a, b)))
    if a == 0:
        return b+1
    elif b == 0:
        return ackermann(a-1, 1, s)
    else:
        return ackermann(a-1, ackermann(a, b-1, s % ("A(%d, %%s)" % (a-1))), s)


print(ackermann(1, 1))

