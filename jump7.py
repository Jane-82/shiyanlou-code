for x in range(1,101):
    a = x % 10
    b = x // 10
    if x % 7 != 0 and a != 7 and b != 7:
        print(x)
