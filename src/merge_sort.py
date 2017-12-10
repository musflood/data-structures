"""Implements a merge sorting algorithm.

Merge sort halves a list repeatedly into the smallest possible pieces,
then sorts them. Compares each pair of pieces to each other one element
at a time, merging them into a larger, sorted piece. Completed when
both halves of the list are merged back together.
"""


def merge_sort(values):
    """Create a sorted copy of the given list using merge sort."""
    if not values:
        return []

    def merge(half1, half2):
        if half2 and not half1:
            return half2

        mid1 = len(half1) // 2
        half1 = merge(half1[:mid1], half1[mid1:])

        mid2 = len(half2) // 2
        half2 = merge(half2[:mid2], half2[mid2:])

        result = []
        idx1, idx2 = 0, 0
        while idx1 < len(half1) and idx2 < len(half2):
            if half1[idx1] < half2[idx2]:
                result.append(half1[idx1])
                idx1 += 1
            else:
                result.append(half2[idx2])
                idx2 += 1
        return result + half1[idx1:] + half2[idx2:]

    mid = len(values) // 2
    return merge(values[:mid], values[mid:])


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint
    setup = 'from merge_sort import merge_sort'

    print("""
Merge sort halves a list repeatedly into the smallest possible pieces,
then sorts them. Compares each pair of pieces to each other one element
at a time, merging them into a larger, sorted piece. Completed when
both halves of the list are merged back together.
""")

    print('-- Best Case --')
    for length in range(5, 20, 5):
        l = sorted([randint(-100, 100) for _ in range(length)])

        print("""Input: sorted([randint(-100, 100) for _ in range({})])
    number of runs: 1000000""".format(len(l)))
        time = timeit('merge_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Average Case --')
    for length in range(5, 20, 5):
        l = [randint(-100, 100) for _ in range(length)]

        print("""Input: [randint(-100, 100) for _ in range({})]
    number of runs: 1000000""".format(len(l)))
        time = timeit('merge_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Worst Case --')
    for length in range(5, 20, 5):
        l = sorted([randint(-100, 100) for _ in range(length)], reverse=True)

        print("""Input: sorted([randint(-100, 100) for _ in range({})], reverse=True)
    number of runs: 1000000""".format(len(l)))
        time = timeit('merge_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))
