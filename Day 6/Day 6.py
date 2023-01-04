def marker_search(stream, length):
    for i in range(len(datastream) - length + 1):
        marker = stream[i : i + length]
        if len(set(marker)) == length:
            return(i + length)


def part_one(stream):
    return marker_search(stream, 4)


def part_two(stream):
    return marker_search(stream, 14)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        datastream = f.read()

    print(part_one(datastream))

    print(part_two(datastream))
