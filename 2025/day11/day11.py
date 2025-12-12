import time
from collections import defaultdict

start = time.time()
input_file = "input.txt"
with open(input_file, "r") as f:
    lines = f.read().splitlines()

graph = defaultdict(list)
for line in lines:
    [node, neighbors] = line.split(": ")
    graph[node] = neighbors.split(" ")

def dfs(curr, end, reqs, visited, mem):
    completed_reqs = [r for r in reqs if r in visited]
    memo_key = (curr, tuple(sorted(completed_reqs)))

    if memo_key in mem:
        return mem[memo_key]
    if curr == end:
        return 1 if len(completed_reqs) == len(reqs) else 0
    
    visited.add(curr)
    num_paths = sum([dfs(neighbor, end, reqs, visited, mem) for neighbor in graph[curr] if neighbor not in visited])
    visited.remove(curr)
    
    mem[memo_key] = num_paths
    return num_paths

    
def part1():
    return dfs("you", "out", [], set(), {})


def part2():
    return dfs("svr", "out", ["fft", "dac"], set(), {})


if __name__ == "__main__":
    print(f"----------------\nanswer: {part2()}")
    print(f"elapsed time: {time.time() - start}")
