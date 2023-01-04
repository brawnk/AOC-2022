def make_map(raw_input):
    raw_input = raw_input.split()
    array = []

    for i in range(len(raw_input)):
        row = [j for j in raw_input[i]]
        array.append(row)

    return array


def numerate(h_map):
    rows = len(h_map)
    cols = len(h_map[0])
    o_x = None
    o_y = None

    num_map = [[0] * cols for _ in range(rows)]
    for i in range(len(h_map)):
        for j in range(len(h_map[i])):
            letter = h_map[i][j]

            if letter == "S":
                num_map[i][j] = 1
                o_x = j
                o_y = i

            elif letter == "E":
                num_map[i][j] = 26

            else:
                num_map[i][j] = ord(letter) - 96
    return num_map, o_x, o_y


def distance(h_map):
    rows = len(h_map)
    cols = len(h_map[0])

    dist_map = [[float('inf')] * cols for _ in range(rows)]
    for i in range(len(h_map)):
        for j in range(len(h_map[i])):
            if h_map[i][j] == "E":
                dist_map[i][j] = 0

    return dist_map


def neighbours(d_map, i, j, n_map):
    rows = len(d_map)
    cols = len(d_map[0])

    if i > 0 and (n_map[j][i - 1] - n_map[j][i]) < 2:
        left = d_map[j][i - 1]
    else:
        left = float('inf')

    if i + 1 < cols and (n_map[j][i + 1] - n_map[j][i]) < 2:
        right = d_map[j][i + 1]
    else:
        right = float('inf')

    if j > 0 and (n_map[j - 1][i] - n_map[j][i]) < 2:
        up = d_map[j - 1][i]
    else:
        up = float('inf')

    if j + 1 < rows and (n_map[j + 1][i] - n_map[j][i]) < 2:
        down = d_map[j + 1][i]
    else:
        down = float('inf')

    return left, right, up, down


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        file = f.read()

    height_map = make_map(file)

    number_map, origin_x, origin_y = numerate(height_map)

    distance_map = distance(height_map)

    changes = True
    while changes:
        changes = False
        for y in range(len(height_map)):
            for x in range(len(height_map[y])):
                path = min(neighbours(distance_map, x, y, number_map)) + 1
                if path < distance_map[y][x]:
                    changes = True
                    distance_map[y][x] = path

    # part 1
    print(distance_map[origin_y][origin_x])

    # part 2
    start_points = []
    for y in range(len(height_map)):
        for x in range(len(height_map[y])):
            if number_map[y][x] == 1:
                start_points.append(distance_map[y][x])
    print(min(start_points))
