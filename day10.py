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


# method cannot finished in time
def arrange_count(lst: List[int], min_bound: int, max_bound: int) -> int:
    if len(lst) == 1:
        if (lst[0] - min_bound <= 3) and (max_bound - lst[0] <= 3):
            return 1
        else:
            return 0
    else:
        first = lst[0]
        if first - min_bound > 3:
            return 0
        return arrange_count(lst[1:], first, max_bound) + arrange_count(lst[1:], min_bound, max_bound)


silly_list: List[int] = [int(line) for line in open("input/day10.txt", "r").readlines()]
sorted_list = sorted(silly_list)
handled_input: List[int] = [0] + sorted_list + [sorted_list[-1] + 3]

# Part 1
c1, c3 = diff_count(handled_input)
print(f"Part 1: c1 = {c1}, c3 = {c3}, product = {c1 * c3}")

# Part 2
total = arrange_count(sorted_list, 0, 22)
print(f"Part 2: total = {total}")
