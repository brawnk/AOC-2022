import re
from time import perf_counter


class Sensor:
    def __init__(self, sensor, beacon):
        self.sensor = sensor
        self.beacon = beacon
        self.range = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])

    def row(self, row):
        empty = None
        distance = abs(row - self.sensor[1])
        if distance <= self.range:
            left = self.sensor[0] - abs(distance-self.range)
            right = self.sensor[0] + abs(distance-self.range)
            empty = [left, right + 1]
        return empty


def process_input(raw_input):
    raw_input = raw_input.split("\n")

    sensor_list = []
    for r in raw_input:
        temp = re.findall(r'-?\d+', r)
        res = list(map(int, temp))
        sensor = Sensor((res[0], res[1]), (res[2], res[3]))
        sensor_list.append(sensor)
    return sensor_list


def overlap(x, y):
    if min(x[1], y[1]) - max(x[0], y[0]) >= 0:
        return min(x[0], y[0]), max(x[1], y[1])


def merge(lst):
    new_list = lst.copy()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            combined = overlap(lst[i], lst[j])
            if combined is not None:
                new_list[i] = combined
                new_list.pop(j)
                break
        else:
            continue
        break

    if lst != new_list:
        new_list = merge(new_list)
    return new_list


def searched_columns(sensor_list, row):
    empty = []
    for s in sensor_list:
        positions = s.row(row)
        if positions is None:
            continue
        empty.append(positions)

    return merge(empty)


def part_one(sensor_list, row):
    empty = searched_columns(sensor_list, row)

    total = 0
    for positions in empty:
        num = positions[1] - positions[0]
        total += num

    beacons = []
    for s in sensor_list:
        if s.beacon[1] == row:
            beacons.append(s.beacon)
    total -= len(set(beacons))

    return total


def part_two(sensor_list, max_val):
    for i in range(max_val):
        empty = searched_columns(sensor_list, i)
        if empty[0][0] < 1 and empty[0][1] > max_val:
            continue
        return min(empty[0][1], empty[1][1]) * max_val + i


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        file = f.read()

    sensors = process_input(file)

    t1 = perf_counter()
    print(part_one(sensors, int(2E6)))
    print(part_two(sensors, int(4E6)))  # room for optimisation, completes in 100 seconds on my PC
    print(perf_counter() - t1)
