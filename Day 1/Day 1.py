import ast


def process_input(raw_input):
    elf_list = []
    elf_split = raw_input.split("\n\n")
    for elf in elf_split:
        row = []
        food = elf.split()
        for i in food:
            item_calories = ast.literal_eval(i)
            row.append(item_calories)
        elf_list.append(row)
    return elf_list


def part_one(elf_list):
    max_calories = 0
    for elf in elf_list:
        calories = sum(elf)
        max_calories = max(max_calories, calories)
    return max_calories


def part_two(elf_list):
    calories_list = []
    for elf in elf_list:
        calories_list.append(sum(elf))

    calories_list.sort(reverse=True)
    top_three = calories_list[0] + calories_list[1] + calories_list[2]

    return top_three


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        file = f.read()

    elves = process_input(file)

    print(part_one(elves))

    print(part_two(elves))
