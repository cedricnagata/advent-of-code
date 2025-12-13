import time

start = time.time()
input_file = "input.txt"
with open(input_file, "r") as f:
    lines = f.read().splitlines()


def part1():
    ans = 0

    for line in lines:
        if "x" in line:
            dims, counts_str = line.split(": ")
            w, h = map(int, dims.split("x"))
            counts = map(int, counts_str.split())

            area = w * h
            total_count = sum(counts) * 9

            if total_count <= area:
                ans += 1
    return ans


def part2():
    pass


if __name__ == "__main__":
    print(f"----------------\nanswer: {part1()}")
    print(f"elapsed time: {time.time() - start}")
