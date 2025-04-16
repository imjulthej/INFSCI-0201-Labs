def zipmap(key_list, value_list, override=False):
    max_len = max(len(key_list), len(value_list))
    padded_values = value_list[:len(key_list)] + [None] * (len(key_list) - len(value_list))
    zipped = list(map(lambda kv: (kv[0], kv[1]), zip(key_list, padded_values)))

    keys = [k for k, _ in zipped]
    if not override and len(set(keys)) != len(keys):
        return {}

    result = {}
    for k, v in zipped:
        if not override and k in result:
            continue
        result[k] = v
    return result

# Example
if __name__ == "__main__":
    print(zipmap(['a', 'b', 'c', 'd'], [1, 2, 3, 4]))
    print(zipmap([1, 2, 3, 2], [4, 5, 6, 7], True))
    print(zipmap([1, 2, 3], [4, 5, 6, 7, 8]))
    print(zipmap([1, 3, 5, 7], [2, 4, 6]))