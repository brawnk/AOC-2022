import re
from collections import deque
from copy import deepcopy


class Monkey:
    def __init__(self, info, divisors_list):
        numbers = []
        for i in info:
            temp = re.findall(r'\d+', i)
            numbers += list(map(int, temp))

        # check if operation number is old
        old_count = len(re.findall(r'old', info[2]))
        self.items = deque(numbers[1: -5 + old_count])
        self.operator = re.findall(r'[+*]', info[2])[0]
        self.number = 'old' if old_count == 2 else numbers[-4]
        self.divisor = numbers[-3]
        self.true_monkey = numbers[-2]
        self.false_monkey = numbers[-1]

        # part two self.remainders replaces self.items
        self.remainders = deque()
        for item in self.items:
            remainders = {}
            for divisor in divisors_list:
                remainders[divisor] = item % divisor
            self.remainders.append(remainders)

        self.inspections = 0

    def inspect(self):
        number = self.number
        if self.number == 'old':
            number = self.items[0]

        if self.operator == '*':
            self.items[0] *= number
        else:
            self.items[0] += number

        self.items[0] = int(self.items[0] / 3.0)
        self.inspections += 1

    def test(self):
        if self.items[0] % self.divisor == 0:
            return True
        return False

    def throw(self):
        item = self.items[0]
        self.items.popleft()
        return item

    def catch(self, item):
        self.items.append(item)

    def part_two_inspect(self):
        number = self.number
        if self.operator == '*':
            for divisor, remainder in self.remainders[0].items():
                self.remainders[0][divisor] *= number if number != 'old' else self.remainders[0][divisor]
        else:
            for divisor, remainder in self.remainders[0].items():
                self.remainders[0][divisor] += number if number != 'old' else self.remainders[0][divisor]

        for i, remainder in self.remainders[0].items():
            self.remainders[0][i] = remainder % i

        self.inspections += 1

    def part_two_test(self):
        if self.remainders[0][self.divisor] == 0:
            return True
        return False

    def part_two_throw(self):
        item = self.items[0]
        self.items.popleft()
        remainder = self.remainders[0]
        self.remainders.popleft()
        return item, remainder

    def part_two_catch(self, item, remainder):
        self.items.append(item)
        self.remainders.append(remainder)


def process_input(raw_input):
    raw_input = raw_input.split("\n\n")

    divisors_list = []
    processed_input = []
    for line in raw_input:
        line = line.split("\n")
        divisors_list.append(int(re.findall(r'\d+', line[-3])[0]))
        processed_input.append(line)

    return processed_input, divisors_list


def initialise_monkeys(processed_input, divisors_list):
    monkey_list = []
    for line in processed_input:
        monkey_list.append(Monkey(line, divisors_list))

    return monkey_list


def turn(monkey_list, i):
    monkey = monkey_list[i]

    for _ in range(len(monkey.items)):
        monkey.inspect()

        if monkey.test() is True:
            new_monkey = monkey_list[monkey.true_monkey]
        else:
            new_monkey = monkey_list[monkey.false_monkey]
        item = monkey.throw()
        new_monkey.catch(item)

    return monkey_list


def part_two_turn(monkey_list, i):
    monkey = monkey_list[i]

    for _ in range(len(monkey.items)):
        monkey.part_two_inspect()

        if monkey.part_two_test() is True:
            new_monkey = monkey_list[monkey.true_monkey]
        else:
            new_monkey = monkey_list[monkey.false_monkey]
        item, remainder = monkey.part_two_throw()
        new_monkey.part_two_catch(item, remainder)

    return monkey_list


def monkey_round(monkey_list):
    for i in range(len(monkey_list)):
        monkey_list = turn(monkey_list, i)
    return monkey_list


def part_two_monkey_round(monkey_list):
    for i in range(len(monkey_list)):
        monkey_list = part_two_turn(monkey_list, i)
    return monkey_list


def part_one(input_list, rounds):
    monkey_list = deepcopy(input_list)

    for _ in range(rounds):
        monkey_list = monkey_round(monkey_list)

    inspections = []
    for monkey in monkey_list:
        inspections.append(monkey.inspections)

    inspections.sort(reverse=True)
    monkey_business = inspections[0] * inspections[1]

    return monkey_business


def part_two(input_list, rounds):
    monkey_list = deepcopy(input_list)

    for _ in range(rounds):
        monkey_list = part_two_monkey_round(monkey_list)

    inspections = []
    for monkey in monkey_list:
        inspections.append(monkey.inspections)

    inspections.sort(reverse=True)
    monkey_business = inspections[0] * inspections[1]

    return monkey_business


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        file = f.read()

    data, divisors = process_input(file)

    monkeys = initialise_monkeys(data, divisors)
    print(part_one(monkeys, 20))

    print(part_two(monkeys, 10_000))
