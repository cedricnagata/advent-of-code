import math

input_file = "input.txt"

def euclidean_dist(p: str, q: str) -> float:
    p = [int(coord) for coord in p.split(",")]
    q = [int(coord) for coord in q.split(",")]
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)

with open(input_file, "r") as f:
    input = f.read()
    boxes = input.splitlines()

    edges = []
    nodes = {}
    for i, source in enumerate(boxes):
        nodes[i] = [int(coord) for coord in source.split(",")]
        for j, dest in enumerate(boxes[i + 1 :], (i + 1)):
            dist = euclidean_dist(source, dest)
            edges.append((i, j, dist))
    edges.sort(key=lambda x: x[2])


def part1():
    circuits = []
    seen = set()
    for edge in edges[:1000]:
        (source, dest, _) = edge
        if source in seen and dest in seen:
            i = 0
            source_circuit = dest_circuit = -1
            while source_circuit == -1 or dest_circuit == -1:
                if source in circuits[i]:
                    source_circuit = i
                if dest in circuits[i]:
                    dest_circuit = i
                i += 1
            if source_circuit != dest_circuit:
                set_to_merge = circuits[dest_circuit]
                circuits[source_circuit].update(set_to_merge)
                circuits.pop(dest_circuit)
        elif source in seen:
            i = 0
            while source not in circuits[i]:
                i += 1
            circuits[i].add(dest)
            seen.add(dest)
        elif dest in seen:
            i = 0
            while dest not in circuits[i]:
                i += 1
            circuits[i].add(source)
            seen.add(source)
        else:
            circuits.append(set([source, dest]))
            seen.add(source)
            seen.add(dest)

    for i in range(len(nodes)):
        if i not in seen:
            circuits.append(set([i]))

    circuits.sort(key=lambda x: -len(x))
    ans = 1
    for i in range(3):
        ans *= len(circuits[i])

    return ans


def part2():
    circuits = []
    seen = set()
    final_edge = None

    for edge in edges:
        (source, dest, _) = edge
        if source in seen and dest in seen:
            i = 0
            source_circuit = dest_circuit = -1
            while source_circuit == -1 or dest_circuit == -1:
                if source in circuits[i]:
                    source_circuit = i
                if dest in circuits[i]:
                    dest_circuit = i
                i += 1
            if source_circuit != dest_circuit:
                set_to_merge = circuits[dest_circuit]
                circuits[source_circuit].update(set_to_merge)
                circuits.pop(dest_circuit)
        elif source in seen:
            i = 0
            while source not in circuits[i]:
                i += 1
            circuits[i].add(dest)
            seen.add(dest)
        elif dest in seen:
            i = 0
            while dest not in circuits[i]:
                i += 1
            circuits[i].add(source)
            seen.add(source)
        else:
            circuits.append(set([source, dest]))
            seen.add(source)
            seen.add(dest)

        if len(circuits) == 1 and len(seen) == len(nodes):
            final_edge = edge
            break

    final_node_1, final_node_2 = nodes[final_edge[0]], nodes[final_edge[1]]
    ans = final_node_1[0] * final_node_2[0]

    return ans


if __name__ == "__main__":
    print(part2())
