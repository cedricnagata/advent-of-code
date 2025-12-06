from heapq import *

input_file = "input.txt"

def part1():
    freshRanges = []
    ids = []    

    with open(input_file, "r") as f:
        for line in f:
            split = line.split("-")
            l = len(split)
            if l == 2:
                freshRanges.append((int(split[0]), int(split[1])))
            else:
                if line != "\n":
                    ids.append(int(line))

    def isValidId(id):
        for start, end in freshRanges:
            if id >= start and id <= end:
                return True
        return False
    
    ans = 0
    for id in ids:
        if isValidId(id):
            ans += 1
    return ans


def part2():
    fresh_ranges = []
    with open(input_file, "r") as f:
        for line in f:
            split = line.split("-")
            l = len(split)
            if l == 2:
                fresh_ranges.append((int(split[0]), int(split[1])))
            else:
                break

    sorted_ranges = sorted(fresh_ranges)

    ans = largest = 0
    for (start, end) in sorted_ranges:
        if start > largest:
            ans += end - start + 1
        else:
            if end > largest:
                ans += end - largest
        largest = max(largest, end)
    return ans


if __name__ == "__main__":
    print(part2())
