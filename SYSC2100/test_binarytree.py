"""
Author: Braeden Kloke
Version: March 18, 2022

Description:
------------
Test harness for Lab 8 for the course SYSC 2100 (Algorithms and Data Structures) at Carleton University.

Lab 8 required the student to implement various methods on class BinaryTree in Python. Class BinaryTree implements 
the basic binary tree from Section 6.1 of 'Open Data Structures (in pseudocode)', Edition 0.1G Beta.


This Python script tests the following methods in lab8_binarytree.py:

* build_binary_tree: Builds the binary tree shown in exercise 1 of the lab handout, and returns a reference to the tree.

* build_full_binary_tree: Builds the binary tree shown in exercise 2 of the lab handout, and returns a reference to the tree.

* size: Returns the number of nodes in the binary tree.

* height: Returns the length of the longest path from the tree's root to one of its descendants.

* preorder_print: Prints the binary tree using a preorder traversal.

* inorder_print: Prints the binary tree using an inorder traversal.

* postorder_print: Prints the binary tree using a postorder traversal.

* count: Returns the number of occurences of an item in the binary tree.


Motivation:
----------
To put into practice test-driven development and publicly document my work on GitHub.


Improvements for Next Time:
---------------------------
1) Design a test fixture

2) Use AssertRaises() in unittest to test that exception errors are properly raised

3) Add print statements for when an error is raised, makes it easier to debug


Disclaimer:
-----------
This work is documented on GitHub to be used only as reference for job applications.

Writing a test harness was not required in this assignment. Posting the test harness on GitHub
does not violate any form of academic integrity.

"""
from lab8_binarytree import *
import unittest

class TestBinaryTree(unittest.TestCase):

    def test_build_binary_tree(self):
        tree = build_binary_tree()

        cases = [
            (tree.get_root()._x, 10),
            (tree.get_root().get_left_child()._x, 20),
            (tree.get_root().get_right_child()._x, 30)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_build_full_binary_tree(self):
        tree = build_full_binary_tree()
        root = tree.get_root()

        cases = [
            (root._x, 5),
            (root.get_left_child()._x, 7),
            (root.get_right_child()._x, 12),
            (root.get_left_child().get_left_child()._x, 17),
            (root.get_left_child().get_right_child()._x, 9),
            (root.get_right_child().get_left_child()._x, 3),
            (root.get_right_child().get_right_child()._x, 6)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_size(self) -> None:
        tree0 = BinaryTree()
        tree1 = build_binary_tree()
        tree2 = build_full_binary_tree()

        cases = [
            (tree0.size(), 0),
            (tree1.size(), 3),
            (tree2.size(), 7)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_height(self) -> None:
        tree0 = BinaryTree()
        tree1 = build_binary_tree()
        tree2 = build_full_binary_tree()

        cases = [
            (tree0.height(), -1),
            (tree1.height(), 1),
            (tree2.height(), 2)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])

    def test_preorder_print(self) -> None:
        printing = False
        tree1 = build_binary_tree()
        tree2 = build_full_binary_tree()

        if printing:
            print("\nTesting preorder_print ...")
            tree1.preorder_print()
            tree2.preorder_print()

    def test_inorder_print(self) -> None:
        printing = False
        tree1 = build_binary_tree()
        tree2 = build_full_binary_tree()

        if printing:
            print("\nTesting inorder_print ...")
            tree1.inorder_print()
            tree2.inorder_print()

    def test_postorder_print(self) -> None:
        printing = False
        tree1 = build_binary_tree()
        tree2 = build_full_binary_tree()

        if printing:
            print("\nTesting postorder_print ...")
            tree1.postorder_print()
            tree2.postorder_print()

    def test_count(self) -> None:
        tree0 = BinaryTree()
        tree1 = build_binary_tree()
        tree2 = build_full_binary_tree()

        # Builds a binary tree with duplicate payloads
        tree3 = BinaryTree()
        tree3.set_root(BinaryTree.Node(42))
        r = tree3.get_root()
        r.set_left_child(BinaryTree.Node(-1))
        r.set_right_child(BinaryTree.Node(42))
        lc = r.get_left_child()
        lc.set_left_child(BinaryTree.Node(42))

        cases = [
            (tree0.count(42), 0), (tree1.count(10), 1),
            (tree1.count(42), 0), (tree1.count(20), 1),
            (tree1.count(30), 1), (tree2.count(17), 1),
            (tree2.count(6), 1), (tree3.count(-1), 1),
            (tree3.count(42), 3), (tree3.count(43), 0)
        ]
        for case in cases:
            self.assertEqual(case[0], case[1])


if __name__ == '__main__':
    unittest.main()


