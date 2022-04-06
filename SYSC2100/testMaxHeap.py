"""
Author: Braeden Kloke
Version: April 6, 2022

Description:
------------
Test harness for Lab 11 for the course SYSC 2100 (Algorithms and Data Structures) at Carleton University.

Lab 11 required the student to implement various methods on the Binary Heap data structure in Python. 

This Python script tests the following methods in maxheap.py:

* [X] add: Insert x in this BinaryHeap.

* [X] remove: Remove the largest value from this BinaryHeap and return it.

* [X] find_max: Return the largest value in this BinaryHeap.


Improvements for Next Time:
---------------------------
1) Get familar with unittest command line functions (like -v)

2) Figure out if there is a better way to test print statements rather than visual verification
"""
import unittest
from maxheap import *


class TestHeap(unittest.TestCase):

    def setUp(self):
        self.maxHeap0 = BinaryHeap()

    def testMaxHeap1(self):
        self.assertEqual(0, len(self.maxHeap0))
        self.assertRaises(IndexError, lambda: self.maxHeap0.find_max())
        self.assertRaises(IndexError, lambda: self.maxHeap0.remove())

    def testMaxHeap2(self):
        # Remove from heap with elements added in ascending order
        for j in range(6):
            for i in range(j):
                self.maxHeap0.add(i)  # Add elements in ascending order
            for i in range(j):
                self.assertEqual(j - i - 1, self.maxHeap0.remove())
                self.assertEqual(j - i - 1, len(self.maxHeap0))

    def testMaxHeap3(self):
        # Remove from heap with elements added in descending order
        for j in range(6):
            for i in range(j):
                self.maxHeap0.add(j - i - 1)  # Add in descending order
                self.assertEqual(j - i - 1, self.maxHeap0._a[i])
            for i in range(j):
                self.assertEqual(j - i - 1, self.maxHeap0.remove())
                self.assertEqual(j - i - 1, len(self.maxHeap0))

    def testMaxHeap4(self):
        maxHeap = BinaryHeap([0, 1, 2, 3, 4])
        self.assertEqual(4, maxHeap._a[0])
        self.assertEqual(3, maxHeap._a[1])
        self.assertEqual(1, maxHeap._a[2])
        self.assertEqual(0, maxHeap._a[3])
        self.assertEqual(2, maxHeap._a[4])

    def testMaxHeap5(self):
        maxHeap = BinaryHeap([1, 4, 5, 9, 3, 7, 0, 2, 8, 6])  # Random permutation, no duplicates
        for i in range(10):
            self.assertEqual(9 - i, maxHeap.remove())


if __name__ == '__main__':
    unittest.main()
