from collections import defaultdict

def group_by(f, target_list):
    grouped = defaultdict(list)
    for item in target_list:
        key = f(item) - 1
        grouped[key].append(item)
    return dict(grouped)

# Example
if __name__ == "__main__":
    print(group_by(len, ["hi", "dog", "me", "bad", "good"]))