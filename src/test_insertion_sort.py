"""Tests for insertion_sort."""
import pytest
import random


@pytest.mark.parametrize('nums', [[random.randint(-100, 100) for _ in range(y)]
                                  for y in range(0, 20)])
def test_insertion_sort_of_ints_orders_correctly(nums):
    """Test that bubble sort sorts ints correctly."""
    from insertion_sort import insertion_sort
    assert insertion_sort(nums) == sorted(nums)


@pytest.mark.parametrize('nums', [[random.uniform(-100, 100) for _ in range(y)]
                                  for y in range(0, 20)])
def test_insertion_sort_of_floats_orders_correctly(nums):
    """Test that bubble sort sorts floats correctly."""
    from insertion_sort import insertion_sort
    assert insertion_sort(nums) == sorted(nums)


WORDS = ['ostentatiously', 'panornithic', 'butyrone', 'lust', 'smriti',
         'planner', 'confutative', 'hyperalgesia', 'birdlore', 'cogger',
         'vacuumize', 'corporalship', 'erichtoid', 'iridochoroiditis',
         'fouter', 'compotation', 'benzophenazine', 'Inoceramus',
         'undivable', 'sugarless']


@pytest.mark.parametrize('strings', [random.sample(WORDS, y)
                                     for y in range(0, 20)])
def test_insertion_sort_of_strings_orders_correctly(strings):
    """Test that bubble sort sorts strings correctly."""
    from insertion_sort import insertion_sort
    assert insertion_sort(strings) == sorted(strings)


def test_insertion_sort_does_not_affect_the_original_list():
    """Test that bubble sort makes a new list, does not change the original."""
    from insertion_sort import insertion_sort
    l = [5, 2, 7, 4, 1]
    sorted_l = insertion_sort(l)
    assert l == [5, 2, 7, 4, 1]
    assert sorted_l is not l
