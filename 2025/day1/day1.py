import time

with open("input.txt", "r") as f:
    input = f.read()

rotations = input.split("\n")

def part_1(rotations: list[str]) -> int:
    curr = 50
    ans = 0

    for r in rotations:
        dir, num = r[0], int(r[1:]) % 100
        if curr == 0:
            ans += 1
        if dir == "L":
            curr = ((curr - num) + 100) % 100
        if dir == "R":
            curr = (curr + num) % 100

    return ans

def part_2(rotations: list[str]) -> int:
    curr = 50
    ans = 0

    for r in rotations:
        prev_curr = curr
        dir, diff = r[0], int(r[1:])
        ans += diff // 100
        
        if dir == "L":
            curr -= (diff % 100)
            if curr == 0 and diff > 0:
                ans += 1
            elif curr < 0:
                if prev_curr != 0:
                    ans += 1
                curr = (curr + 100) % 100
        if dir == "R":
            curr += (diff % 100)
            if curr == 0 and diff > 0:
                ans += 1
            elif curr > 99:
                if prev_curr != 0:
                    ans += 1
                curr = curr % 100

    return ans

if __name__ == "__main__":
    print(part_2(rotations))