input_file = "input.txt"

def part1():
    with open(input_file, "r") as f:
        eqs = None
        first_pass = True
        for line in f:
            items = line.split()
            if first_pass:
                eqs = list(range(len(items)))
            for i, item in enumerate(items):
                if first_pass:
                    eqs[i] = [item]
                else:
                    eqs[i].append(item)
            first_pass = False

    ans = 0
    for eq in eqs:
        if eq[-1] == "+":
            sum = 0
            for num in eq[:-1]:
                sum += int(num)
            ans += sum
        else:
            prod = 1
            for num in eq[:-1]:
                prod *= int(num)
            ans += prod
    return ans


def part2():
    with open(input_file, "r") as f:
        input = f.read()
        lines = input.splitlines()

        num_eqs = len(lines[0].split())
        eqs = list(range(num_eqs))

        curr_eq = []
        curr_eq_idx = num_eqs - 1

        col = len(lines[0]) - 1
        end_eq = False
        while col >= 0:
            curr_num = ""

            # iterate through lines by col (right to left)
            for line in lines:
                if line[col] in ["*", "+"]:
                    # if we hit operator, add curr num then operator to curr_eq and signal eq end
                    curr_eq.append(curr_num)
                    curr_eq.append(line[col])
                    end_eq = True
                elif line[col] != " ":
                    # else if item is num, append to curr_num
                    curr_num += line[col]

            if end_eq:
                # if eq end, we already added last num and operator, so just as curr_eq
                eqs[curr_eq_idx] = curr_eq

                # update curr eq index, reset curr eq
                curr_eq_idx -= 1
                curr_eq = []

                # update curr col to skip next empty col and reset eq end flag
                col -= 2
                end_eq = False
            else:
                # if not eq end, append curr num to eq and update curr col by 1
                curr_eq.append(curr_num)
                col -= 1

    ans = 0
    for eq in eqs:
        if eq[-1] == "+":
            sum = 0
            for num in eq[:-1]:
                sum += int(num)
            ans += sum
        else:
            prod = 1
            for num in eq[:-1]:
                prod *= int(num)
            ans += prod
    return ans


if __name__ == "__main__":
    print(part2())
