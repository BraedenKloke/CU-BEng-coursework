"""
Author: Braeden Kloke
Version: March 30, 2022

Description:
------------
Test harness for Lab 10 for the course SYSC 2100 (Algorithms and Data Structures) at Carleton University.

Lab 10 required the student to implement various methods on class BSTMap in Python. 

This Python script tests the following methods in BSTMap.py:

* [X] BSTMap: Initializes a map with the contents of iterable. If iterable isn't provided, the new BST is empty.

* [X] put: Insert key and the associated value in this map. If key is already in the map, replace the old value with value.

* [X] get: If key is in this map, return the value associated with key; otherwise return None.

* [X] __contains__: Return True if key is in this map; otherwise False.

* [X] pop: If key is in the map, remove it and return the value associated with the key.


Improvements for Next Time:
---------------------------
1) Get familar with unittest command line functions (like -v)

2) Research into testing methodology. Yes, this is test-driven development, but is there a formula
to determine the cases for any given function?

3) Figure out if there is a better way to test print statements rather than visual verification
"""
from BSTMap import *
import unittest

class TestBSTMap(unittest.TestCase):

    def setUp(self):
        """Sets up the test fixture."""
        self.node0 = BSTMap.Node(4, 2)
        self.node1 = BSTMap.Node('pencils', 3)
        self.grades0 = BSTMap()
        self.grades1 = BSTMap([(111537, 'A+'), (111000, 'B'), (211000, 'C')])
        self.grades2 = BSTMap(
            [(5, 'B'), (6, 'B-'), (7, 'C+'), (8, 'C'), (9, 'C-'),  # RS is unbalanced
                (3, 'A-'), (4, 'B+'), (1, 'A+'), (2, 'A')
             ]
        )
        self.supplies0 = BSTMap()
        self.supplies1 = BSTMap([('pencils', 1), ('erasers', 3), ('pens', 4)])

    def testNode1(self):
        cases = [
            (self.node0._key, 4),
            (self.node0._value, 2),
            (self.node0._parent, None),
            (self.node0._left, None),
            (self.node0._right, None)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testNode2(self):
        cases = [
            (self.node1._key, 'pencils'),
            (self.node1._value, 3),
            (self.node1._parent, None),
            (self.node1._left, None),
            (self.node1._right, None)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testPut1(self):
        cases = [
            (self.grades0._root, None),
            (self.grades0._size, 0)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testPut2(self):
        self.grades0.put(111537, 'A+')

        cases = [
            (self.grades0._root._key, 111537),
            (self.grades0._root._value, 'A+'),
            (self.grades0._size, 1)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

        self.grades0.put(111000, 'B')

        cases = [
            (self.grades0._root._left._key, 111000),
            (self.grades0._root._left._value, 'B'),
            (self.grades0._size, 2)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

        self.grades0.put(211000, 'C')

        cases = [
            (self.grades0._root._right._key, 211000),
            (self.grades0._root._right._value, 'C'),
            (self.grades0._size, 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

        # Updates a node in the tree
        self.grades0.put(211000, 'F')

        cases = [
            (self.grades0._root._right._key, 211000),
            (self.grades0._root._right._value, 'F'),
            (self.grades0._size, 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testPut3(self):
        self.supplies0.put('pencils', '1')

        cases = [
            (self.supplies0._root._key, 'pencils'),
            (self.supplies0._root._value, '1'),
            (self.supplies0._size, 1)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

        self.supplies0.put('erasers', 3)

        cases = [
            (self.supplies0._root._left._key, 'erasers'),
            (self.supplies0._root._left._value, 3),
            (self.supplies0._size, 2)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

        self.supplies0.put('pens', 4)

        cases = [
            (self.supplies0._root._right._key, 'pens'),
            (self.supplies0._root._right._value, 4),
            (self.supplies0._size, 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

        # Update a node in tree
        self.supplies0.put('erasers', 7)

        cases = [
            (self.supplies0._root._left._key, 'erasers'),
            (self.supplies0._root._left._value, 7),
            (self.supplies0._size, 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testPut4(self):
        cases = [
            (self.grades1._root._key, 111537),
            (self.grades1._root._value, 'A+'),
            (self.grades1._root._left._key, 111000),
            (self.grades1._root._left._value, 'B'),
            (self.grades1._root._right._key, 211000),
            (self.grades1._root._right._value, 'C'),
            (self.grades1._size, 3),
            (len(self.grades1), 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testPut5(self):
        cases = [
            (self.supplies1._root._key, 'pencils'),
            (self.supplies1._root._value, 1),
            (self.supplies1._root._left._key, 'erasers'),
            (self.supplies1._root._left._value, 3),
            (self.supplies1._root._right._key, 'pens'),
            (self.supplies1._root._right._value, 4),
            (self.supplies1._size, 3),
            (len(self.supplies1), 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testGet1(self):
        cases = [
            (self.grades0.get(111537), None),
            (self.grades1.get(111537), 'A+'),
            (self.grades1.get(111000), 'B'),
            (self.grades1.get(211000), 'C'),
            (self.grades1.get(999999), None),
            (len(self.grades1), 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testGet2(self):
        cases = [
            (self.supplies0.get('bananas'), None),
            (self.supplies1.get('pencils'), 1),
            (self.supplies1.get('erasers'), 3),
            (self.supplies1.get('pens'), 4),
            (len(self.supplies1), 3)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testContains1(self):
        cases = [
            (42 in self.grades0, False),
            (111537 in self.grades1, True),
            (111000 in self.grades1, True),
            (211000 in self.grades1, True),
            (999999 in self.grades1, False)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testPop1(self):
        # Tests exception errors
        self.assertRaises(KeyError, lambda: self.grades0.pop(42))
        self.assertRaises(KeyError, lambda: self.supplies0.pop('bananas'))
        self.assertRaises(KeyError, lambda: self.supplies1.pop('bananas'))

    def testPop2(self):
        # Tests removing leaf nodes from a tree
        # Tests removing integer keys from a tree

        self.grades0.put(123456, 'D')  # Single node tree

        cases = [
            (self.grades0.pop(123456), 'D'),
            (self.grades1.pop(111000), 'B'),
            (self.grades1.pop(211000), 'C'),
            (self.grades1.pop(111537), 'A+'),
            (len(self.grades1), 0),
            (self.grades1._root, None)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

        self.assertRaises(KeyError, lambda: self.grades1.pop(211000))  # Tree is now empty

    def testPop3(self):
        # Tests repeatedly removing the root from the tree
        # Tests a tree with strings as keys
        cases = [
            (self.supplies1.pop('pencils'), 1),
            (len(self.supplies1), 2),
            (self.supplies1._root._key, 'pens'),
            (self.supplies1.pop('pens'), 4),
            (len(self.supplies1), 1),
            (self.supplies1._root._key, 'erasers'),
            (self.supplies1.pop('erasers'), 3),
            (len(self.supplies1), 0),
            (self.supplies1._root, None)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'

    def testPop4(self):
        # Popping from a large BSTMap
        cases = [
            (self.grades2.pop(5), 'B'),
            (len(self.grades2), 8),
            (self.grades2._root._key, 6),
            (self.grades2.pop(3), 'A-'),
            (len(self.grades2), 7),
            (self.grades2._root._left._key, 4),
            (self.grades2.pop(6), 'B-'),
            (self.grades2.pop(7), 'C+'),
            (self.grades2.pop(8), 'C'),
            (self.grades2.pop(9), 'C-'),
            (self.grades2._root._key, 4),
            (self.grades2.pop(4), 'B+'),
            (self.grades2.pop(1), 'A+'),
            (self.grades2.pop(2), 'A'),
            (len(self.grades2), 0),
            (self.grades2._root, None)
        ]
        for case in cases:
            self.assertEqual(case[1], case[0]), f'expected {case[1]}, got {case[0]}'


if __name__ == '__main__':
    unittest.main()
