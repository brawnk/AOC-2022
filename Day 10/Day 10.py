def part_one(raw_input):
    cycle = 1
    register = 1
    cycle_check = 20
    total = 0
    for instruction in raw_input:
        old_register = register
        if instruction[:4] == "noop":
            cycle += 1

        else:  # addx
            cycle += 2
            register += int(instruction[5:])

        if cycle > cycle_check:
            total += cycle_check * old_register

        elif cycle == cycle_check:
            total += cycle_check * register
        else:
            continue

        if cycle_check == 220:
            break
        cycle_check += 40
    return total


def get_register(c, cycles, registers):
    if c == 0:
        return registers[0]

    for i, cycle in enumerate(cycles):
        if cycle > c:
            return registers[i - 1]


def part_two(raw_input):
    cycles = [0]
    registers = [1]
    for instruction in raw_input:
        if instruction[:4] == "noop":
            cycles.append(cycles[-1] + 1)
            registers.append(registers[-1])

        else:  # addx
            cycles.append(cycles[-1] + 2)
            registers.append(registers[-1] + int(instruction[5:]))

    screen = []
    row = ""
    for cycle in range(240):
        distance = abs(get_register(cycle, cycles, registers) - (cycle % 40))

        row += "#" if distance <= 1 else "."

        if (cycle + 1) % 40 == 0:
            screen.append(row)
            row = ""

    for i in screen:
        print(i)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        instructions = f.readlines()

    print(part_one(instructions))

    part_two(instructions)
