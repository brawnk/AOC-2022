def overlap(row):
    if row[1] < row[2] or row[3] < row[0]:
        return False
    return True


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
        print(numbers, overlap(numbers))
        if overlap(numbers):
            count += 1
print(count)
