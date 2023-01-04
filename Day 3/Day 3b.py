def priority(item):
    if item == item.lower():
        return ord(item) - 96
    else:
        return ord(item) - 38  # - 64 + 26


if __name__ == "__main__":
    total = 0
    prev_row = []
    i = 0
    with open('input.txt', 'r') as f:
        for line in f:
            if i == 0:  # first of three
                prev_row = line

            common = [item for item in line if item in prev_row]
            prev_row = common

            if i == 2:  # last of three
                i = 0
                total += priority(common[0])
                continue

            i += 1

    print(total)
