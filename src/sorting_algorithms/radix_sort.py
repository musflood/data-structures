"""Implements a radix sorting algorithm.

Radix sort groups positive integers by the value of a position in
the number. First the one's place is compared, then the ten's, etc.
The numbers are repeatedly sorted into buckets and then flattened
until all the positions have been examined.
"""


def radix_sort(values):
    """Create a sorted copy of the given list using radix sort."""
    if len(values) <= 1:
        return values[:]

    digits = len(str(max(values)))
    for power in range(digits):
        buckets = [[] for _ in range(10)]
        for val in values:
            trunc_val = val % (10 ** (power + 1))
            index = trunc_val // (10 ** power)
            buckets[index].append(val)
        result = []
        for bucket in buckets:
            for val in bucket:
                result.append(val)
        values = result
    return values


if __name__ == '__main__':  # pragma: no cover
    from timeit import timeit
    from random import randint
    setup = 'from radix_sort import radix_sort'

    print("""
Radix sort groups positive integers by the value of a position in
the number. First the one's place is compared, then the ten's, etc.
The numbers are repeatedly sorted into buckets and then flattened
until all the positions have been examined.
""")

    print('-- Best Case --')
    for length in range(5, 20, 5):
        l = [randint(0, 10) for _ in range(length)]

        print("""Input: [randint(0, 10) for _ in range({})]
    number of runs: 1000000""".format(len(l)))
        time = timeit('radix_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Average Case --')
    for length in range(5, 20, 5):
        l = [randint(0, 1000) for _ in range(length)]

        print("""Input: [randint(0, 1000) for _ in range({})]
    number of runs: 1000000""".format(len(l)))
        time = timeit('radix_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))

    print('-- Worst Case --')
    for length in range(5, 20, 5):
        l = [randint(0, 1000000) for _ in range(length)]

        print("""Input: [randint(0, 1000000) for _ in range({})]
    number of runs: 1000000""".format(len(l)))
        time = timeit('radix_sort({})'.format(l), setup)
        print('    average time: {}ms\n'.format(time))
