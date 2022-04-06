"""
Author: Braeden Kloke
Version: April 6, 2022

Description:
------------
Test harness for Assignment 2 for the course SYSC 2100 (Algorithms and Data Structures) at Carleton University.

Assignment 2 required the student to implement various methods on the Binary Heap Priority Queue data structure in Python. 

This Python script tests the following methods in heappriorityqueue.py:

* [X] add: Insert item in this PriorityQueue, assigning it the specified priority, and return True.

* [X] remove: Remove and return the item with the highest priority in this PriorityQueue.

* [X] str: Return a string representation of this PriorityQueue.


Improvements for Next Time:
---------------------------
1) Get familar with unittest command line functions (like -v)

2) Figure out if there is a better way to test print statements rather than visual verification
"""
import unittest
from heappriorityqueue import *


class TestHeapPriorityQueue(unittest.TestCase):

    def setUp(self):
        self.items = ["white", "blue", "green", "red", "black"]
        self.pq0 = PriorityQueue()

    def testPriorityQueue0(self):
        self.assertEqual(0, len(self.pq0))
        self.assertRaises(IndexError, lambda: self.pq0.remove())

    def testPriorityQueue1(self):
        # Add in ascending order
        count = 0
        for item in self.items:
            self.assertEqual(True, self.pq0.add(item, count))  # item, priority
            self.assertEqual("white", self.pq0._a[0][0])
            self.assertEqual(0, self.pq0._a[0][1])
            count += 1
            self.assertEqual(count, len(self.pq0))

        self.assertEqual(
            "[[white,0],[blue,1],[green,2],[red,3],[black,4]]", str(self.pq0)
        )

        # Remove items
        for item in self.items:
            self.assertEqual(item, self.pq0.remove())
            count -= 1
            self.assertEqual(count, len(self.pq0))

    def testPriorityQueue2(self):
        # Add in descending order
        count = 4
        for item in self.items:
            self.assertEqual(True, self.pq0.add(item, count))  # item, priority
            self.assertEqual(item, self.pq0._a[0][0])
            self.assertEqual(count, self.pq0._a[0][1])
            count -= 1

        self.assertEqual(
            "[[black,0],[red,1],[blue,3],[white,4],[green,2]]", str(self.pq0)
        )

        # Remove items
        for i in range(5):
            self.assertEqual(self.items[4 - i], self.pq0.remove())

    def testPriorityQueue3(self):
        # Test str method
        self.assertEqual("[]", str(self.pq0))
        self.pq0.add("white", 0)
        self.assertEqual("[[white,0]]", str(self.pq0))
        self.pq0.add("blue", 1)
        self.assertEqual("[[white,0],[blue,1]]", str(self.pq0))


if __name__ == '__main__':
    unittest.main()
