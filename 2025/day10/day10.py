import time
from collections import defaultdict
from itertools import combinations
from z3 import *


start = time.time()
input_file = "input.txt"
with open(input_file, "r") as f:
    lines = f.read().splitlines()
    

def part1():
    machines = []
    for line in lines:
        items = line.split(" ")

        # get light dec
        lights = items[0][1:-1]
        digits = len(lights)
        light_binary = ""
        for l in lights:
            light_binary += "1" if l == "#" else "0"
        light_dec = int(light_binary, 2)

        # get button dec
        button_group = []
        buttons = [tuple(map(int, button[1:-1].split(","))) for button in items[1:-1]]
        for button in buttons:
            button_binary = ["0"] * digits
            for d in button:
                button_binary[d] = "1"
            button_dec = int("".join(button_binary), 2)
            button_group.append(button_dec)

        machines.append([light_dec, button_group])

    ans = 0
    for [correct, buttons] in machines:
        curr = 0
        combo_len = 0
        found = False
        while not found:
            combo_len += 1
            for combo in combinations(buttons, combo_len):
                temp = curr
                for button in combo:
                    temp ^= button
                if temp == correct:
                    found = True
                    break
        ans += combo_len
    
    return ans


def part2():
    machines = []
    for i, line in enumerate(lines):
        items = line.split(" ")
    
        buttons = [list(map(int, button[1:-1].split(","))) for button in items[1:-1]]
        joltages = [int(j) for j in items[-1][1:-1].split(",")]
    
        machines.append([joltages, buttons])

    ans = 0
    for [joltages, buttons] in machines:
        solver = Solver()

        button_presses = [Int(f"b{i}") for i in range(len(buttons))]
        for b in button_presses:
            solver.add(b >= 0)

        for i, joltage in enumerate(joltages):
            relevant_buttons = []
            for j, button in enumerate(buttons):
                if i in button:
                    relevant_buttons.append(button_presses[j])
            solver.add(Sum(relevant_buttons) == joltage)

        while solver.check() == sat:
            model = solver.model()
            total_presses = sum([model[press_counts].as_long() for press_counts in model])
            solver.add(Sum(button_presses) < total_presses)
        ans += total_presses

    return ans


if __name__ == "__main__":
    print(f"----------------\nanswer: {part2()}")
    print(f"elapsed time: {time.time() - start}")
