import ast


def process_input(raw_input):
    packets = raw_input.split()

    for i in range(len(packets)):
        packets[i] = ast.literal_eval(packets[i])

    return packets


def check_elements(left, right):
    for i, j in zip(left, right):
        # print(i, j)
        if isinstance(i, int) is True and isinstance(j, int) is True:
            if i < j:
                # print("lhs smaller")
                return True
            elif i > j:
                # print("rhs smaller")
                return False
            elif i == j:
                continue
        elif isinstance(i, list) is True and isinstance(j, list) is True:
            ans = check_elements(i, j)
            if ans is True:
                return True
            elif ans is False:
                return False
        else:
            new_i = [i] if isinstance(i, int) else i
            new_j = [j] if isinstance(j, int) else j
            ans = check_elements(new_i, new_j)
            if ans is True:
                return True
            elif ans is False:
                return False

    if len(left) < len(right):
        # print("lhs ran out of items")
        return True
    if len(left) > len(right):
        # print("rhs ran out of items")
        return False


def part_one(packets):
    pairs = []

    for i in range(0, len(packets), 2):
        left = packets[i]
        right = packets[i + 1]
        pair = [left, right]
        pairs.append(pair)

    total = 0
    for i, pair in enumerate(pairs):
        left = pair[0]
        right = pair[1]
        if check_elements(left, right) is True:
            total += i + 1
    return total


def bubble_sort(array):
    for i in range(len(array) - 1):
        left = array[i]
        right = array[i + 1]
        if check_elements(left, right) is False:
            array[i] = right
            array[i + 1] = left

    return array


def part_two(packets):
    packets.append([[2]])
    packets.append([[6]])

    last_pass = packets.copy()

    while True:
        packets = bubble_sort(packets)
        if packets == last_pass:
            break
        last_pass = packets.copy()

    decoder_key = (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)

    return decoder_key


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        file = f.read()

    processed_input = process_input(file)

    print(part_one(processed_input))

    print(part_two(processed_input))
