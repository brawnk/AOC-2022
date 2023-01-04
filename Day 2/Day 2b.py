def shape_score(row):
    point_map = {"A X": 3, "A Y": 1, "A Z": 2, "B X": 1, "B Y": 2, "B Z": 3, "C X": 2, "C Y": 3, "C Z": 1}
    return point_map[row]


def game_score(row):
    points = {"X": 0, "Y": 3, "Z": 6}
    return points[row[2]]


def score(row):
    return game_score(row) + shape_score(row)


if __name__ == "__main__":
    total_score = 0
    with open('input.txt', 'r') as f:
        for line in f:
            game = line.strip()
            total_score += score(game)

    print(total_score)
