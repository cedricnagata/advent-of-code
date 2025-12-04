with open("input.txt", "r") as f:
    input = f.read()

grid: list[list[str]] = []
rows = input.split("\n")
for row in rows:
    grid.append(list(row))


def part1(grid: list[list[str]]) -> int:
    dirs = [(0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    rows, cols = len(grid), len(grid[0])

    def numValidNeighborRolls(curr_row: int, curr_col: int) -> bool:
        numRolls = 0
        for dir in dirs:
            new_row, new_col = curr_row + dir[0], curr_col + dir[1]
            if (
                new_row >= 0
                and new_row < rows
                and new_col >= 0
                and new_col < cols
                and grid[new_row][new_col] == "@"
            ):
                numRolls += 1
        return numRolls

    ans = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "@" and numValidNeighborRolls(row, col) < 4:
                ans += 1

    return ans


def part2(grid: list[list[str]]) -> int:
    dirs = [(0, 1), (1, 1), (1, 0), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]
    rows, cols = len(grid), len(grid[0])

    def numValidNeighborRolls(curr_row: int, curr_col: int) -> bool:
        numRolls = 0
        for dir in dirs:
            new_row, new_col = curr_row + dir[0], curr_col + dir[1]
            if (
                new_row >= 0
                and new_row < rows
                and new_col >= 0
                and new_col < cols
                and grid[new_row][new_col] == "@"
            ):
                numRolls += 1
        return numRolls
    
    def removeRolls() -> int:
        num_removed = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "@" and numValidNeighborRolls(row, col) < 4:
                    grid[row][col] = "."
                    num_removed += 1
        return num_removed

    ans = 0
    while True:
        num_removed = removeRolls()
        if num_removed == 0:
            break
        else:
            ans += num_removed
    
    return ans


if __name__ == "__main__":
    print(part2(grid))
