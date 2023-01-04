def fully_contained(row):
    """fully contained if one row is strictly larger or smaller than the other"""
    if row[0] <= row[2] and row[1] >= row[3]:
        return True
    if row[0] >= row[2] and row[1] <= row[3]:
        return True
    return False


if __name__ == "__main__":
    count = 0
    with open('input.txt', 'r') as f:
        for line in f:
            gaps = []
            for char, i in zip(line, range(0, len(line))):
                if char == "-" or char == ",":
                    gaps.append(i)

            numbers = [int(line[:gaps[0]]),
                       int(line[gaps[0] + 1:gaps[1]]),
                       int(line[gaps[1] + 1:gaps[2]]),
                       int(line[gaps[2] + 1:-1])]

            if fully_contained(numbers):
                count += 1
    print(count)
