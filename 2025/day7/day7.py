from collections import defaultdict
input_file = "input.txt"

def part1():
    with open(input_file, "r") as f:
        input = f.read()

    lines = input.splitlines()
    beams = set()
    ans = 0

    for line in lines:
        for index, char in enumerate(line):
            if char == "S":
                beams.add(index)
                continue
            elif char == "^":
                if index in beams:
                    beams.remove(index)
                    beams.add(index - 1)
                    beams.add(index + 1)
                    ans += 1
    return ans


def part2():
    with open(input_file, "r") as f:
        input = f.read()

    lines = input.splitlines()
    beams = defaultdict(int)

    for line in lines:
        for index, char in enumerate(line):
            if char == "S":
                beams[index] += 1
                continue
            elif char == "^":
                if index in beams.keys():
                    num_paths = beams.pop(index)
                    beams[index - 1] += num_paths
                    beams[index + 1] += num_paths

    ans = 0
    for num_paths in beams.values():
        ans += num_paths
    return ans


if __name__ == "__main__":
    print(part2())
