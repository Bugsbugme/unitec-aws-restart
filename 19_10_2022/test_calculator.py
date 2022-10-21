import calculator
import pytest


def test_two_plus_two_equals_four():
    assert calculator.add(2, 2) == 4


def test_minus_five_plus_six_equals_1():
    assert calculator.add(-5, 6) == 1


def test_one_plus_one_equals_1():
    assert calculator.add(1, 1) == 2


def test_a_plus_two_equals_type_error():
    assert calculator.add("a", 2) == 0
