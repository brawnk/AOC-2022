def make_grid(raw_input):
    raw_input = raw_input.split()
    tree_map = []

    for i in range(len(raw_input)):
        row = [j for j in raw_input[i]]
        tree_map.append(row)

    return tree_map


def paths(tree_map, x, y):
    left = tree_map[y][:x][::-1]
    right = tree_map[y][x + 1:]
    top = [tree_map[i][x] for i in range(y)][::-1]
    bottom = [tree_map[i][x] for i in range(y + 1, len(tree_map))]

    return left, right, top, bottom


def check_visible(height, path):
    for direction in path:
        if height > max(direction):
            return True


def part_one(tree_map):
    count = 2 * len(tree_map) + 2 * (len(tree_map[0]) - 2)

    for x in range(1, len(tree_map[0]) - 1):
        for y in range(1, len(tree_map) - 1):
            lines = paths(tree_map, x, y)
            tree = tree_map[y][x]
            if check_visible(tree, lines):
                count += 1

    return count


def tree_score(height, path):
    product = 1
    for direction in path:
        if len(direction) == 0:
            product *= 0
            continue

        total = 0
        for i in direction:
            total += 1
            if i >= height:
                break
        product *= total

    return product


def part_two(tree_map):
    scenic_score = 0
    for x in range(len(tree_map[0])):
        for y in range(len(tree_map)):
            lines = paths(tree_map, x, y)
            tree = tree_map[y][x]
            score = tree_score(tree, lines)
            scenic_score = max(scenic_score, score)

    return scenic_score


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        trees = f.read()

    grid = make_grid(trees)

    print(part_one(grid))

    print(part_two(grid))
