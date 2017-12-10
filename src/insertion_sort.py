"""Implements a insertion sorting algorithm.

Insertion sort moves values into place by iterating forward through
a list and comparing each value to the values that came before it.
"""


def insertion_sort(values):
    """Create a sorted copy of the given list using bubble sort."""
    pass


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint
    setup = 'from insertion_sort import insertion_sort'

    print("""
Insertion sort moves values into place by iterating forward through
a list and comparing each value to the values that came before it.
""")

    print('-- Best Case --')
    for length in range(5, 20, 5):
        l = sorted([randint(-100, 100) for _ in range(length)])

        print("""Input: sorted([randint(-100, 100) for _ in range({})])
    number of runs: 1000000""".format(len(l)))
        time = timeit('insertion_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Average Case --')
    for length in range(5, 20, 5):
        l = [randint(-100, 100) for _ in range(length)]

        print("""Input: [randint(-100, 100) for _ in range({})]
    number of runs: 1000000""".format(len(l)))
        time = timeit('insertion_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Worst Case --')
    for length in range(5, 20, 5):
        l = sorted([randint(-100, 100) for _ in range(length)], reverse=True)

        print("""Input: sorted([randint(-100, 100) for _ in range({})], reverse=True)
    number of runs: 1000000""".format(len(l)))
        time = timeit('insertion_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))
