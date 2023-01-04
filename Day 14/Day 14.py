import ast
import copy
from time import perf_counter

def process_input(raw_input):
    rock_occupied = {}
    rows = raw_input.split("\n")
    for row in rows:
        temp = []
        positions = row.split(" -> ")
        for data in positions:
            coordinate = ast.literal_eval(data)
            x = coordinate[0]
            y = coordinate[1]
            position = x + y * 1j
            temp.append(position)

        # fill paths
        x, y = temp[0].real, temp[0].imag
        if x not in rock_occupied.keys():
            rock_occupied[x] = {y}
        else:
            rock_occupied[x].add(y)

        for i in range(1, len(temp)):
            start = temp[i - 1]
            finish = temp[i]

            x_diff = finish.real - start.real
            y_diff = finish.imag - start.imag

            steps = int(max(abs(x_diff), abs(y_diff)))
            step = (x_diff // steps) + (y_diff // steps) * 1j

            last = start
            for j in range(steps):
                last = last + step
                x, y = last.real, last.imag

                if x not in rock_occupied.keys():
                    rock_occupied[x] = {y}
                    continue
                rock_occupied[x].add(y)

    return rock_occupied


def move_down(sand_position, rock_occupied, floor):
    x = sand_position.real
    y = sand_position.imag
    y_coords = [floor]

    if x in rock_occupied.keys():
        y_coords += list(rock_occupied[x])
    elif floor < 0:  # part one
        return True

    y_coords.sort()
    if floor < 0 and y_coords[-1] <= y:  # part one
        return True

    for i in y_coords:
        if i > y:
            return x + (i - 1) * 1j


def move_sand(sand_position, rock_occupied, floor):
    new_position = move_down(sand_position, rock_occupied, floor)

    if new_position is True:
        return True

    # check left
    temp = move_down(new_position - 1, rock_occupied, floor)
    if temp is True:
        return True

    if temp.imag > new_position.imag:
        new_position = move_sand(temp, rock_occupied, floor)

    # check right
    else:
        temp = move_down(new_position + 1, rock_occupied, floor)
        if temp is True:
            return True

        if temp.imag > new_position.imag:
            new_position = move_sand(temp, rock_occupied, floor)

    return new_position


def part_one(rocks):
    occupied_spots = copy.deepcopy(rocks)

    i = 0
    while True:
        # move floor out of range for part one
        new = move_sand(500 + 0j, occupied_spots, floor=-1)

        if new is True:
            return i

        x, y = new.real, new.imag
        if x not in occupied_spots.keys():
            occupied_spots[x] = {y}
        else:
            occupied_spots[x].add(y)

        i += 1


def part_two(rocks):
    occupied_spots = copy.deepcopy(rocks)
    floor = 0
    for y in occupied_spots.values():
        floor = max(max(y), floor)
    floor += 2

    i = 0
    while True:
        new = move_sand(500, occupied_spots, floor=floor)

        if new == 500:
            return i + 1

        x, y = new.real, new.imag
        if x not in occupied_spots.keys():
            occupied_spots[x] = {y}
        else:
            occupied_spots[x].add(y)

        i += 1


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        file = f.read()

    occupied = process_input(file)

    print(part_one(occupied))

    t1 = perf_counter()
    print(part_two(occupied))  # probably room for some optimisation here, complete in about 20 seconds on my pc
    print(perf_counter() - t1)
