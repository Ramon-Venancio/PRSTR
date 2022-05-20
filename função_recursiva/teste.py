def test(n):
    if n == 1:
        return n
    print(n)
    return test(n -1)

test(5)