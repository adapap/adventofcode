def seven(m):
    n = str(m)
    if len(n) <= 2:
        return (m, 0)
    res = seven(int(n[:-1]) - 2 * int(n[-1]))
    return (res[0], res[1] + 1)


seven(1603)
seven(371)
seven(483)