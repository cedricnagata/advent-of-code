with open("input.txt", "r") as f:
    input = f.read()

ranges = input.split(",")

def part1(ranges: list[str]) -> int:
    newRanges = []
    for range in ranges:
        split = range.split("-")
        start, end = split[0], split[1]
        startLen, endLen = len(start), len(end)

        if startLen == endLen:
            if startLen % 2 == 0:
                newRanges.append((start, end))
        else:
            while startLen <= endLen:
                if startLen % 2 == 0:
                    if startLen == endLen:
                        newRanges.append((start, end))
                    else:
                        newRanges.append((start, "9" * startLen))
                start = "1" + ("0" * startLen)
                startLen += 1

    ans = 0
    def isInvalid(num: int, l: int) -> bool:
        numStr = str(num)
        return numStr[:l//2] == numStr[l//2:]
    
    for start, end in newRanges:
        l = len(start)
        startNum, endNum = int(start), int(end)
        while startNum <= endNum:
            if isInvalid(startNum, l):
                ans += startNum
            startNum += 1
    return ans


def part2(ranges: list[str]) -> int:
    def isInvalid(num: int) -> bool:
        numStr = str(num)
        l = len(numStr)
        for i in range(1, l+1 // 2):
            if l % i == 0:
                chunk = numStr[:i]
                if chunk * (l // i) == numStr:
                    return True
        return False
    
    ans = 0
    for r in ranges:
        [start, end] = r.split("-")
        startNum, endNum = int(start), int(end)
        while startNum <= endNum:
            if isInvalid(startNum):
                ans += startNum
            startNum += 1
    return ans

if __name__ == "__main__":
    print(part2(ranges))
