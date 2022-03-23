"""
Author: Braeden Kloke
Version: March 23, 2022

Description:
------------
Test harness for Lab 9 for the course SYSC 2100 (Algorithms and Data Structures) at Carleton University.

Lab 9 required the student to implement various methods on class BinarySearchTree in Python. Class BinarySearchTree 
implements the binary search tree from Section 6.2 of 'Open Data Structures (in pseudocode)', Edition 0.1G Beta.

This Python script tests the following methods in lab9_binarysearchtree.py:

* add: If key x is not in this BinarySearchTree, insert x and return True; otherwise return False.

* find_eq: If key x is in this BinarySearchTree, return the key; otherwise return None.

* find: If key x is in this BinarySearchTree, return the key; otherwise return the smallest value
in the BST that is greater than x. If no key in the BST is greater than or equal to x, return None.

* remove: If key x is in this BinarySearchTree, remove it and return True; otherwise return False.

* preorder_print: Print this BST using a preorder traversal.

* inorder_print: Print this BST using an inorder traversal.

* postorder_print: Print this BST using a postorder traversal.


Motivation:
----------
* To put into practice test-driven development

* To learn how to use Python's unittest library

* To publicly document my work on GitHub


Improvements for Next Time:
---------------------------
1) Use AssertRaises() in unittest to test that exception errors are properly raised

2) Add print statements for when an error is raised, makes it easier to debug

3) Get familar with unittest command line functions (like -v)

4) Organize my cases better, they just look messy and unstructured

5) Figure out if there is a better way to test print statements rather than visual verification

6) Reduce the number of variables in my test fixture. Pick 3-4 that can be manipulated and cover
all test cases.


Disclaimer:
-----------
This work is documented on GitHub to be used only as reference for job applications.

Writing a test harness was not required in this assignment. Posting the test harness on GitHub
does not violate any form of academic integrity.

"""
from lab9_binarysearchtree import *
import unittest

class TestBinarySearchTree(unittest.TestCase):

    def setUp(self):
        """Sets up the test fixture."""
        self.node1 = BinarySearchTree.Node(10)
        self.bst0 = BinarySearchTree()
        self.bst1 = BinarySearchTree([10])
        self.bst2 = BinarySearchTree([10, 20])
        self.bst3 = BinarySearchTree([10, 20, 5])
        self.bst4 = BinarySearchTree([1, 2, 3, 4])  # Unbalanced BST
        self.bst5 = BinarySearchTree([4, 2, 1, 3, 6, 5, 7])
        self.bst6 = BinarySearchTree([42, 42, 42, 42, 42, 42, 42])

    def test_init(self):
        cases = [
            (self.bst0.size(), 0), (self.bst0._root, None),
            (self.node1._x, 10)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_add(self):
        test1 = self.bst0.add(42)
        test2 = self.bst0.add(50)
        test3 = self.bst0.add(7)
        test4 = self.bst0.add(4)
        test5 = self.bst0.add(50)

        cases = [
            (self.bst1.size(), 1), (self.bst1._root._x, 10),
            (self.bst2.size(), 2), (self.bst2._root._x, 10), (self.bst2._root._right._x, 20),
            (self.bst3._root._right._x, 20), (self.bst3._root._left._x, 5),
            (self.bst0._root._x, 42), (test1, True),
            (self.bst0._root._right._x, 50), (test2, True),
            (self.bst0._root._left._x, 7), (test3, True),
            (self.bst0._root._left._left._x, 4), (test4, True),
            (test5, False), (self.bst0.size(), 4),
            (self.bst6.size(), 1)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_find_eq(self):
        cases = [
            (self.bst0.find_eq(42), None), (self.bst1.find_eq(11), None),
            (self.bst1.find_eq(10), 10), (self.bst4.find_eq(1), 1),
            (self.bst4.find_eq(2), 2), (self.bst4.find_eq(3), 3),
            (self.bst4.find_eq(4), 4), (self.bst4.find_eq(5), None),
            (self.bst5.find_eq(1), 1)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_find(self):
        cases = [
            (self.bst0.find(42), None), (self.bst1.find(10), 10),
            (self.bst1.find(9), 10), (self.bst1.find(11), None),
            (self.bst4.find(0), 1), (self.bst4.find(5), None),
            (self.bst5.find(0), 1), (self.bst5.find(8), None),
            (self.bst5.find(7), 7), (self.bst5.find(7.5), None),
            (self.bst5.find(6.5), 7)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_case1(self):
        # [X] Case 1: x in not in the BST, return false
        case1a = self.bst0.remove(42)  # Try removing from an empty BST
        case1b = self.bst4.remove(5)

        cases = [
            (case1a, False), (case1b, False), (self.bst4.size(), 4)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_case2(self):
        # [X] Case 2: x is found in a leaf
        case2a = self.bst4.remove(4)
        case2b = self.bst1.remove(10)  # Remove root

        cases = [
            (case2a, True), (case2b, True), (self.bst1.size(), 0),
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_case3a(self):
        # Case 3: x is found in a Node N that has only one child
        # [X] Case 3a: N is left child of its parent and N has a left child
            # L becomes the left child of P
        self.bst5.remove(3)
        case3a = self.bst5.remove(2)

        cases = [
            (case3a, True), (self.bst5._root._left._x, 1), (self.bst5.size(), 5)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_case3b(self):
        # Case 3: x is found in a Node N that has only one child
        # [X] Case 3b: N is the right child of its parent P and N has a left child
            # L becomes the right child of P
        self.bst5.remove(7)
        case3b = self.bst5.remove(6)

        cases = [
            (case3b, True), (self.bst5._root._right._x, 5), (self.bst5.size(), 5)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_case3c(self):
        # Case 3: x is found in a Node N that has only one child
        # [X] Case 3c: N is the left child of its parent P, and N has a right child R
            # R becomes the left child of P
        self.bst5.remove(1)
        case3c = self.bst5.remove(2)

        cases = [
            (case3c, True), (self.bst5._root._left._x, 3), (self.bst5.size(), 5)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_case3d(self):
        # Case 3: x is found in a Node N that has only one child
        # [X] Case 3d: N is the right child of its parent P, and N has a right child R
            # R becomes the right child of P
        self.bst5.remove(5)
        case3d = self.bst5.remove(6)

        cases = [
            (case3d, True), (self.bst5._root._right._x, 7), (self.bst5.size(), 5)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_case4(self):
        # [X] Case 4: X is found in a node N, that has two children
            # Copy the smallest key in N's right subtree into N
            # remove the node containing the smallest key in N's right subtree
        case4a = self.bst5.remove(4)
        case4b = self.bst5.remove(2)

        cases = [
            (case4a, True), (self.bst5._root._x, 5),
            (case4b, True), (self.bst5._root._left._x, 3),
            (self.bst5.size(), 5)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_remove_all(self):
        for i in range(8):
            self.bst5.remove(i)

        cases = [
            (self.bst5.size(), 0), (self.bst5.find(1), None), (self.bst5.find(7), None)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_preorder_print(self) -> None:
        printing = False

        if printing:
            print("\nTesting preorder_print ...")
            self.bst3.preorder_print()
            self.bst4.preorder_print()
            self.bst5.preorder_print()

    def test_inorder_print(self) -> None:
        printing = False

        if printing:
            print("\nTesting inorder_print ...")
            self.bst3.inorder_print()
            self.bst4.inorder_print()
            self.bst5.inorder_print()

    def test_postorder_print(self) -> None:
        printing = False

        if printing:
            print("\nTesting postorder_print ...")
            self.bst3.postorder_print()
            self.bst4.postorder_print()
            self.bst5.postorder_print()


if __name__ == '__main__':
    unittest.main()
