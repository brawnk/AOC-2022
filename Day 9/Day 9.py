class Knot:
    def __init__(self, length):
        self.positions = [[0, 0] for _ in range(length)]
        self.tail_positions = {(0, 0)}

    def head_move(self, direction):
        self.positions[0][0] -= 1 if direction == "L" else 0
        self.positions[0][0] += 1 if direction == "R" else 0
        self.positions[0][1] += 1 if direction == "U" else 0
        self.positions[0][1] -= 1 if direction == "D" else 0

    def distance(self, prev, knot):
        x = self.positions[prev][0] - self.positions[knot][0]
        y = self.positions[prev][1] - self.positions[knot][1]
        return x, y

    def update(self):
        knots = len(self.positions)
        for knot in range(1, knots):
            x, y = self.distance(knot - 1, knot)

            if abs(x) <= 1 and abs(y) <= 1:  # touching
                pass

            else:
                if x != 0:
                    self.positions[knot][0] += int(x / abs(x))

                if y != 0:
                    self.positions[knot][1] += int(y / abs(y))

            if knot == knots - 1:
                self.tail_positions.add((self.positions[knot][0], self.positions[knot][1]))


def simulate_rope(moves_list, knots):
    rope = Knot(knots)

    for line in moves_list:
        move = line[0]
        number = int(line[2:])

        for _ in range(number):
            rope.head_move(move)
            rope.update()

    return len(set(rope.tail_positions))


def part_one(moves_list):
    return simulate_rope(moves_list, 2)


def part_two(moves_list):
    return simulate_rope(moves_list, 10)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        moves = f.readlines()

    print(part_one(moves))

    print(part_two(moves))

