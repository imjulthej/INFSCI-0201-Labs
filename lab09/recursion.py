def product_of_digits(x):
    x = abs(x)
    if x < 10:
        return x
    return (x % 10) * product_of_digits(x // 10)

def array_to_string(a, index=0):
    if index == len(a) - 1:
        return str(a[index])
    return str(a[index]) + "," + array_to_string(a, index + 1)

def log(base, value):
    if value < 1 or base <= 1:
        raise ValueError("Base must be greater than 1 and value must be greater than 0")
    if value < base:
        return 0
    return 1 + log(base, value // base)


# Example
print(product_of_digits(234))
print(array_to_string([1, 2, 3, 4]))
print(log(10, 123456))