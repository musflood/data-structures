"""Implements a quick sorting algorithm.

Quick sort partitions a list into two pieces repeatedly by
selecting a pivot value and rearranges the elements such that
all values less than the pivot are before it and those greater
are after. Each partition is partitioned until the list is
completely sorted.
"""


def quick_sort(values):
    """Create a sorted copy of the given list using quick sort."""
    if len(values) <= 1:
        return values[:]

    pivot = values[0]
    left = []
    right = []

    for val in values[1:]:
        if val <= pivot:
            left.append(val)
        else:
            right.append(val)

    return quick_sort(left) + [pivot] + quick_sort(right)


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint
    setup = 'from quick_sort import quick_sort'

    print("""
Quick sort partitions a list into two pieces repeatedly by
selecting a pivot value and rearranges the elements such that
all values less than the pivot are before it and those greater
are after. Each partition is partitioned until the list is
completely sorted.
""")

    print('-- Best Case --')
    for length in range(5, 20, 5):
        l = [randint(-100, 100) for _ in range(length)]

        print("""Input: [randint(-100, 100) for _ in range({})]
    number of runs: 1000000""".format(len(l)))
        time = timeit('quick_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Worst Case --')
    for length in range(5, 20, 5):
        l = sorted([randint(-100, 100) for _ in range(length)])

        print("""Input: sorted([randint(-100, 100) for _ in range({})])
    number of runs: 1000000""".format(len(l)))
        time = timeit('quick_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))
