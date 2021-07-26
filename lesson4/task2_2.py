#100000 loops, best of 5: 42.8 usec per loop - 55
#100000 loops, best of 5: 1.62 msec per loop - 550

def eratosphenes(n):
    def is_prime(n):
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i += 1
        return True

    for p in range(2, n + 1):
        if is_prime(p):
            print(f"{', ' if p > 2 else ''}{p}", end="")
