import time
from heapq import *
import itertools

start = time.time()
input_file = "input.txt"
with open(input_file, "r") as f:
    lines = f.read().splitlines()


class Rect:
    def __init__(self, x1, y1, x2, y2):
        self.p1 = (x1, y1)
        self.p2 = (x2, y2)
        self.area = self.get_area(x1, y1, x2, y2)

    def __lt__(self, other):
        return self.area > other.area

    @staticmethod
    def get_area(x1: int, y1: int, x2: int, y2: int) -> int:
        return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

    def __str__(self):
        return f"p1: {self.p1}, p2: {self.p2}, area: {self.area}"


def part1():
    rects = []
    heapify(rects)
    for i, line1 in enumerate(lines):
        [x1, y1] = [int(c) for c in line1.split(",")]
        for line2 in lines[i + 1 :]:
            [x2, y2] = [int(c) for c in line2.split(",")]
            heappush(rects, Rect(x1, y1, x2, y2))
    return heappop(rects).area


def part2():
    points = [tuple(map(int, l.split(","))) for l in lines]
    edges = [edge for edge in itertools.pairwise(points + [points[0]])]

    rects = []
    heapify(rects)
    for i, (x1, y1) in enumerate(points):
        for x2, y2 in points[i + 1 :]:
            heappush(rects, Rect(x1, y1, x2, y2))

    while rects:
        rect = heappop(rects)
        (x1, y1), (x2, y2), area = rect.p1, rect.p2, rect.area

        x_low, x_high = min(x1, x2), max(x1, x2)
        y_low, y_high = min(y1, y2), max(y1, y2)

        def valid(x_low, x_high, y_low, y_high):
            for (edge_x1, edge_y1), (edge_x2, edge_y2) in edges:
                if edge_x1 == edge_x2:
                    if (
                        x_low < edge_x1 < x_high
                        and min(edge_y1, edge_y2) <= y_high
                        and max(edge_y1, edge_y2) >= y_low
                    ):
                        return False
                if edge_y1 == edge_y2:
                    if (
                        y_low < edge_y1 < y_high
                        and min(edge_x1, edge_x2) <= x_high
                        and max(edge_x1, edge_x2) >= x_low
                    ):
                        return False
            return True

        if valid(x_low, x_high, y_low, y_high):
            return area


if __name__ == "__main__":
    print(f"----------------\nanswer: {part2()}")
    print(f"elapsed time: {time.time() - start}")
