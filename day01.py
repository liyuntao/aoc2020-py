from typing import Optional, Tuple, Set


def sum_of_k(numbers: Set[int], d: int, k: int) -> Optional[Tuple[int, ...]]:
    """
        Returns A tuple of numbers `T` such that: `T ⊆ numbers`, `|T| = k` and `sum(T) = d`.
    """
    if k == 1:
        return (d,) if d in numbers else None

    for n in numbers:
        n_comp = sum_of_k(numbers, d - n, k - 1)
        if n_comp:
            return n_comp + (n,)


numbers = {int(line) for line in open("input/day01.txt", "r").readlines()}

# Part 1
n1, n2 = sum_of_k(numbers, 2020, 2)
print(f"Part 1: N1 = {n1}, N2 = {n2}, product = {n1 * n2}")

# Part 2
n1, n2, n3 = sum_of_k(numbers, 2020, 3)
print(f"Part 2: N1 = {n1}, N2 = {n2}, N3 = {n3} product = {n1 * n2 * n3}")
