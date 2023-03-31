def hanoi(n, s, a, t):
    if n == 1:
        print(f"move disk 1 from {s} to {t}")
        return 
    hanoi(n-1, s, t, a)
    print(f"move disk {n} from {s} to {t}")
    hanoi(n-1, a, s, t)


hanoi(3, "A", "B", "C")
