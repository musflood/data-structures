"""Implements a merge sorting algorithm.

Merge sort halves a list repeatedly into the smallest possible pieces,
then sorts them. Compares each pair of pieces to each other one element
at a time, merging them into a larger, sorted piece. Completed when
both halves of the list are merged back together.
"""


def merge_sort(values):
    """Create a sorted copy of the given list using merge sort."""
    sort_list = values[:]
    pass


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
