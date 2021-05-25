from typing import Tuple, List


def diff_count(numbers: List[int]) -> Tuple[int, int]:
    count_1, count_3 = 0, 0
    for index, value in enumerate(numbers, start=0):
        if index != 0:
            if numbers[index] - numbers[index - 1] == 1:
                count_1 += 1
            elif numbers[index] - numbers[index - 1] == 3:
                count_3 += 1
    return count_1, count_3


silly_list: List[int] = [int(line) for line in open("input/day10.txt", "r").readlines()]
silly_list = sorted(silly_list)
handled_input: List[int] = [0] + silly_list + [silly_list[-1] + 3]

# Part 1
c1, c3 = diff_count(handled_input)
print(f"Part 1: c1 = {c1}, c3 = {c3}, product = {c1 * c3}")

# Part 2
# n1, n2, n3 = sum_of_k(numbers, 2020, 3)
# print(f"Part 2: N1 = {n1}, N2 = {n2}, N3 = {n3} product = {n1 * n2 * n3}")
