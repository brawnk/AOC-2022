def shape_score(shape):
    points = {"X": 1, "Y": 2, "Z": 3}
    return points[shape]


def game_score(row):
    point_map = {"A X": 3, "A Y": 6, "A Z": 0, "B X": 0, "B Y": 3, "B Z": 6, "C X": 6, "C Y": 0, "C Z": 3}
    return point_map[row]


def score(row):
    return game_score(row) + shape_score(row[2])


if __name__ == "__main__":
    total_score = 0
    with open('input.txt', 'r') as f:
        for line in f:
            game = line.strip()
            total_score += score(game)

    print(total_score)
