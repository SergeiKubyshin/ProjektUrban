def test(n, a='text', b=1):
    print(n, a, b)

    def fac(n):
        if n == 1:
            return 1
        return fac(n - 1) * n

    print(fac(n))

test(3)