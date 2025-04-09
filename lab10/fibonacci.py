import time

def memoize(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n-1) + recur_fibo(n-2)

@memoize
def fast_fibo(n):
    if n <= 1:
        return n
    return fast_fibo(n-1) + fast_fibo(n-2)

def main():
    n = 35

    start = time.time()
    print(f"Normal Fibonacci({n}): {recur_fibo(n)}")
    print("Time:", time.time() - start)

    start = time.time()
    print(f"Memoized Fibonacci({n}): {fast_fibo(n)}")
    print("Time:", time.time() - start)

if __name__ == "__main__":
    main()