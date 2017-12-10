"""Implements a bubble sorting algorithm.

Bubble sort moves the largest values to the end of a list by
iterating through the list repeatedly and swapping values if
they are not in the correct order.
"""


def bubble_sort(values):
    """Create a sorted copy of the given list using bubble sort."""
    sort_list = values[:]
    end = len(sort_list)
    is_sorted = False

    while end > 1 and not is_sorted:
        is_sorted = True
        for i in range(0, end - 1):
            if sort_list[i] > sort_list[i + 1]:
                sort_list[i], sort_list[i + 1] = sort_list[i + 1], sort_list[i]
                is_sorted = False
        end -= 1

    return sort_list


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint
    setup = 'from bubble_sort import bubble_sort'

    print("""
Bubble sort moves the largest values to the end of a list by
iterating through the list repeatedly and swapping values if
they are not in the correct order.
""")

    print('-- Best Case --')
    for length in range(5, 20, 5):
        l = sorted([randint(-100, 100) for _ in range(length)])

        print("""Input: sorted([randint(-100, 100) for _ in range({})])
    number of runs: 1000000""".format(len(l)))
        time = timeit('bubble_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Average Case --')
    for length in range(5, 20, 5):
        l = [randint(-100, 100) for _ in range(length)]

        print("""Input: [randint(-100, 100) for _ in range({})]
    number of runs: 1000000""".format(len(l)))
        time = timeit('bubble_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Worst Case --')
    for length in range(5, 20, 5):
        l = sorted([randint(-100, 100) for _ in range(length)], reverse=True)

        print("""Input: sorted([randint(-100, 100) for _ in range({})], reverse=True)
    number of runs: 1000000""".format(len(l)))
        time = timeit('bubble_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))
