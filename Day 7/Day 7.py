class Directory:
    def __init__(self):
        self.ls = {}

    def get_size(self):
        size = 0
        for i in self.ls.values():
            if str(i).isnumeric():
                size += int(i)
            else:
                size += i.get_size()
        return size


def process_input(raw_input):
    terminal_list = raw_input.strip().split('\n')

    pwd = []
    base = Directory()

    for line in terminal_list:
        arg = line.split()
        if arg[1] == 'cd':
            if arg[2] == '..':
                pwd.pop()
            else:
                pwd.append(arg[2])

        elif arg[1] == 'ls':
            continue
        else:
            location = arg[1]
            directory = base
            for i in range(1, len(pwd)):
                directory = directory.ls[pwd[i]]

            if arg[0] == 'dir':
                directory.ls[location] = Directory()
            else:
                directory.ls[arg[1]] = arg[0]

    return base


def part_one(base, threshold):
    total_size = 0
    size = base.get_size()
    if size < threshold + 1:
        total_size += size

    for d in base.ls.values():
        if isinstance(d, Directory):
            total_size += part_one(d, threshold)
    return total_size


def min_size(base, threshold):
    smallest_size = float('inf')
    size = base.get_size()
    if size >= threshold:
        smallest_size = size

    for d in base.ls.values():
        if isinstance(d, Directory):
            smallest_size = min(smallest_size, min_size(d, threshold))
    return smallest_size


def part_two(base, total_disk_space, needed_space):
    used_space = base.get_size()
    unused_space = total_disk_space - used_space

    size_to_delete = needed_space - unused_space

    return min_size(base, size_to_delete)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        file = f.read()

    root = process_input(file)

    print(part_one(root, 100000))

    print(part_two(root, 70_000_000, 30_000_000))
