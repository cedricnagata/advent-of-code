with open("input.txt", "r") as f:
    input = f.read()

banks = input.split("\n")

def part1(banks: list[str]) -> int:
    ans = 0

    for bank in banks:
        largest = 0
        idx = -1
        for i in range(len(bank)-1):
            if int(bank[i]) > largest:
                largest, idx = int(bank[i]), i
        nextLargest = 0
        for b in range(idx + 1, len(bank)):
            nextLargest = max(nextLargest, int(bank[b]))

        ans += (largest * 10 + nextLargest)

    return ans


def part2(banks: list[str]) -> int:
    ans = 0

    for bank in banks:
        numStr = ""
        currIdx = -1
        remDigits = 12

        while remDigits > 0:
            largest = 0
            for i in range(currIdx + 1, len(bank) + 1 - remDigits):
                if int(bank[i]) > largest:
                    largest, currIdx = int(bank[i]), i
            numStr += str(largest)
            remDigits -= 1
        ans += int(numStr)
    return ans

if __name__ == "__main__":
    print(part2(banks))
