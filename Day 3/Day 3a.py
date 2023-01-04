def priority(item):
    if item == item.lower():
        return ord(item) - 96
    else:
        return ord(item) - 38  # - 64 + 26


if __name__ == "__main__":
    total = 0
    with open('input.txt', 'r') as f:
        for line in f:
            mid = len(line) // 2
            left_compartment = line[:mid]
            right_compartment = line[mid:]
            common = [item for item in left_compartment if item in right_compartment]
            total += priority(common[0])

    print(total)