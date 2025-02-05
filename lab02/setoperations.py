def make_set(data):
    if data is None:
        return []
    unique_elements = []
    for item in data:
        if item not in unique_elements:
            unique_elements.append(item)
    return unique_elements

def is_set(data):
    if data is None:
        return False
    return len(data) == len(make_set(data))

def union(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    return make_set(setA + setB)

def intersection(setA, setB):
    if not is_set(setA) or not is_set(setB):
        return []
    return [item for item in setA if item in setB]

set1 = [1, 2, 3, 4, 4, 5]
set2 = [3, 4, 5, 6, 7]
    
print("make_set Operation:", make_set(set1))
print("is_set Operation 1:", is_set(set1))
print("is_set Operation 2:", is_set(set2))
print("union Operation:", union(make_set(set1), make_set(set2)))
print("intersection Operation:", intersection(make_set(set1), make_set(set2)))