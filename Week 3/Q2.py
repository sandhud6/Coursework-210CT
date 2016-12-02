def primeNumber(n, val = None):
    if val is None:
        val = n-1
    while val >=2:
        if n % val == 0:
            print("Not a prime number")
            return False
        else:
            return primeNumber(n, val-1)

    else:

        print("This is a prime number")
        return True
