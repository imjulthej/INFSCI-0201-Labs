from functools import reduce

def my_filter(predicate, seq):
    return reduce(lambda acc, x: acc + [x] if predicate(x) else acc, seq, [])

# Example
if __name__ == "__main__":
    print(my_filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5, 6]))
    print(my_filter(lambda x: x > 3, [1, 2, 3, 4, 5]))