
"""
Author: Braeden Kloke
Version: March 10, 2022

Description:
------------
Test harness for Lab 7 for the course SYSC 2100 (Algorithms and Data Structures) at Carleton University.

Lab 7 required the student to implement various methods using recursive functions on singly-linked lists in Python.


This Python script tests the following methods in recursive_functions.py:

* power: Returns x raised to the power of n.

* num_digits: Returns the number of digits in a given integer.

* count: Returns the total number of occurences of an integer in a linked list.

* last: Returns the last integer in a linked list.

* copy: Makes a copy of a linked list.


The following helper functions are defined:

* _start_tests: Prints that tests are starting for a given method.

* _end_tests: Prints if all tests have passed for a method.

* _test_ints: Tests two integers to see if they are equal. Asserts if false.

* _test_floats: Tests two floats to see if they are within a certain tolerance. Asserts if false.

* _test_strings: Tests two strings to see if they are equal. Asserts if false.


Motivation:
----------
To put into practice test-driven development and publicly document my work on GitHub.


Improvements for Next Time:
---------------------------
1) Figure out how to automate test if exception errors are raised properly

2) Explore and experiment with different Python testing libraries


Disclaimer:
-----------
This work is documented on GitHub to be used only as reference for job applications.

Writing a test harness was not required in this assignment and posting the test harness on GitHub
does not violate any form of academic integrity.

"""

from recursive_functions import *


def test_power() -> None:
    """Tests the method power in recursive_functions.py"""
    method = 'power'

    _start_tests(method)

    # Invalid Input
    # test = power(3.5, -1) # [X] Properly raises ValueError

    # Base Case
    test = power(3.5, 0)
    _test_floats(method, test, 1)

    # Recursive Cases
    test = power(3.5, 1)
    _test_floats(method, test, 3.5)
    test = power(3.5, 2)
    _test_floats(method, test, 12.25)

    _end_tests()


def test_num_digits() -> None:
    """Tests the method num_digits in recursive_functions.py"""
    method = 'num_digits'

    _start_tests(method)

    # Invalid Input
    # test = num_digits(-1) # [X] Properly raises ValueError

    # Base Cases
    test = num_digits(0)
    _test_ints(method, test, 1)
    test = num_digits(9)
    _test_ints(method, test, 1)

    # Recursive Cases
    test = num_digits(10)
    _test_ints(method, test, 2)
    test = num_digits(99)
    _test_ints(method, test, 2)
    test = num_digits(100)
    _test_ints(method, test, 3)
    test = num_digits(492)
    _test_ints(method, test, 3)

    _end_tests()


def test_count() -> None:
    """Tests the method count in recursive_functions.py"""
    method = 'count'

    _start_tests(method)

    # Invalid Input
    # test = num_digits(-1) # [X] Properly raises ValueError

    # Base Case
    head = None
    test = count(head, 5)
    _test_ints(method, test, 0)

    # Recursive Cases
    head = build_linked_list([10, 20, 10, 30, 20, 10])
    test = count(head, 10)
    _test_ints(method, test, 3)
    test = count(head, 30)
    _test_ints(method, test, 1)

    _end_tests()


def test_last() -> None:
    """Tests the method last in recursive_functions.py"""
    method = 'last'

    _start_tests(method)

    # Invalid Input
    head = None
    # test = last(head) # [X] Properly raises ValueError

    # Base Case
    head = build_linked_list([10])
    test = last(head)
    _test_ints(method, test, 10)

    # Recursive Cases
    head = build_linked_list([1, 2, 4, 4, 6, 5])
    test = last(head)
    _test_ints(method, test, 5)

    _end_tests()


def test_copy():
    """Tests the method copy in recursive_functions.py"""
    method = 'copy'

    _start_tests(method)

    # Base Cases
    head = None
    test = copy(head)
    _test_strings(method, to_string(test), 'None')

    # Recursive Cases
    head = build_linked_list([1])
    test = copy(head)
    _test_strings(method, to_string(test), '1')
    _test_ints(method, last(test), 1)

    head = build_linked_list([1, 7])
    test = copy(head)
    _test_strings(method, to_string(test), '1 -> 7')
    _test_ints(method, last(test), 7)

    head = build_linked_list([1, 2, 4, 4, 6, 5])
    test = copy(head)
    _test_strings(method, to_string(test), '1 -> 2 -> 4 -> 4 -> 6 -> 5')
    _test_ints(method, last(test), 5)

    _end_tests()


def _start_tests(method: str) -> None:
    """Prints that tests have begun."""
    print("Testing method " + method + " ...")


def _end_tests() -> None:
    """Prints that tests have passed."""
    print("... all tests passed.")


def _test_ints(method: str, test: int, expected: int) -> None:
    """Compares two integers. Asserts if they are not the same."""
    assert_statement = method + ': expected ' + str(expected) + ', got ' + str(test)

    assert test == expected, assert_statement


def _test_floats(method: str, test: float, expected: float) -> None:
    """Compares two floats. Asserts if they are not within a certain tolerance."""
    tolerance = 0.0001
    assert_statement = method + ': expected ' + str(expected) + ', got ' + str(test)

    assert expected - tolerance <= test <= expected + tolerance, assert_statement


def _test_strings(method: str, test: str, expected: str) -> None:
    """Compares two strings. Asserts if they are not the same."""
    assert_statement = method + ': expected ' + expected + ', got ' + test

    assert test == expected, assert_statement


if __name__ == "__main__":
    test_power()
    test_num_digits()
    test_count()
    test_last()
    test_copy()

