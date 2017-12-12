"""Tests for radix_sort."""
import pytest
import random


@pytest.mark.parametrize('nums', [[random.randint(0, 1000) for _ in range(y)]
                                  for y in range(0, 20)])
def test_radix_sort_of_ints_orders_correctly(nums):
    """Test that bubble sort sorts ints correctly."""
    from radix_sort import radix_sort
    assert radix_sort(nums) == sorted(nums)


def test_radix_sort_does_not_affect_the_original_list():
    """Test that bubble sort makes a new list, does not change the original."""
    from radix_sort import radix_sort
    l = [5, 2, 7, 4, 1]
    sorted_l = radix_sort(l)
    assert l == [5, 2, 7, 4, 1]
    assert sorted_l is not l
