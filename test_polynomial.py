
"""
Author: Braeden Kloke
Version: March 4, 2022

Description:
------------

Test harness for Lab 6 and Assignment 1 for the course SYSC 2100 (Algorithms and Data Structures)
at Carleton University.

Lab 6 and Assignment 1 required the student to implement various methods for the ADT Polynomial
which represents an univariate polynomial in Python. 

This Python script tests the following methods in polynomial.py:

* __str__: Returns a string representation of this polynomial.

* __repr__: Returns the same string as __str__.

* degree: Returns the degree of this polynomial.

* evaluate: Evaluates the polynomial at x and returns the results.

* __add__: Returns the sum of two polynomials.

* __mul__: Returns the product of two polynomials.


Motivation:
----------
To put into practice test-driven development and publicly document my work on GitHub.


Improvements for Next Time:
---------------------------
1) Refactor repeated content and store in functions / constants

2) Figure out how to automate testing for checking if Exception Errors are raised properly
(instead of checking Exception Errors manually)

3) Explore and experiment with different Python testing libraries

4) Add more comments to docstrings (like I did for test_mul)


Disclaimer:
-----------
This work is documented on GitHub to be used only as reference for job applications.

Writing a test harness was not required in this assignment and posting the test harness on GitHub
does not violate any form of academic integrity.

"""

from polynomial import *


def test_str():
    """ Tests method __str__."""
    print("\nTesting method __str__ ...")

    # Polynomial with no terms:
    p = Polynomial()
    assert str(p) == ''

    # Polynomial with one term (a constant):
    p = Polynomial(12)
    assert str(p) == '12', 'expected 12, got ' + str(p)

    # Polynomials with one term:
    p = Polynomial(8, 1)
    assert str(p) == '8x', 'expected 8x, got ' + str(p)
    p = Polynomial(8, 2)
    assert str(p) == '8x^2', 'expected 8x^2, got ' + str(p)

    # Negative polynomial with one term (a constant):
    p = Polynomial(-12)
    assert str(p) == '-12', 'expected -12, got ' + str(p)

    # Negative polynomial with one term:
    p = Polynomial(-7, 1)
    assert str(p) == '-7x', 'expected -7x, got ' + str(p)
    p = Polynomial(-7, 2)
    assert str(p) == '-7x^2', 'expected -7x^2, got ' + str(p)

    # Polynomials with coefficient = 1:
    p1 = Polynomial(1)
    p2 = Polynomial(1, 1)
    p3 = Polynomial(-1, 2)
    p4 = Polynomial(1, 3)
    test = p1
    assert str(test) == '1', 'expected 1, got ' + str(test)
    test = p2
    assert str(test) == 'x', 'expected x, got ' + str(test)
    test = p3
    assert str(test) == '-x^2', 'expected -x^2, got ' + str(test)
    test = p4
    assert str(test) == 'x^3', 'expected x^3, got ' + str(test)
    test = p1 + p2 + p3 + p4
    assert str(test) == 'x^3-x^2+x+1', 'expected x^3-x^2+x+1, got ' + str(test)

    print("... all tests passed.")
    return True


def test_repr():
    """ Tests method __repr__."""
    # Note: These are the same tests as test_str
    print("\nTesting method __repr__ ...")

    # Polynomial with no terms:
    p = Polynomial()
    assert str(p) == ''

    # Polynomial with one term (a constant):
    p = Polynomial(12)
    assert str(p) == '12', 'expected 12, got ' + str(p)

    # Polynomials with one term:
    p = Polynomial(8, 1)
    assert str(p) == '8x', 'expected 8x, got ' + str(p)
    p = Polynomial(8, 2)
    assert str(p) == '8x^2', 'expected 8x^2, got ' + str(p)

    # Negative polynomial with one term (a constant):
    p = Polynomial(-12)
    assert str(p) == '-12', 'expected -12, got ' + str(p)

    # Negative polynomials with one term:
    p = Polynomial(-7, 1)
    assert str(p) == '-7x', 'expected -7x, got ' + str(p)
    p = Polynomial(-7, 2)
    assert str(p) == '-7x^2', 'expected -7x^2, got ' + str(p)

    print("... all tests passed.")
    return True


def test_degree():
    """ Tests method degree."""
    print("\nTesting method degree ...")

    # Polynomial with no terms:
    p = Polynomial()
    # p.degree() # Test manually confirmed, degree properly raised ValueError

    # Polynomial with one term (a constant):
    p = Polynomial(42)
    assert p.degree() == 0, 'expected 0, got ' + str(p.degree())
    p = Polynomial(-42)
    assert p.degree() == 0, 'expected 0, got ' + str(p.degree())

    # Polynomial with one term:
    p = Polynomial(12, 1)
    assert p.degree() == 1, 'expected 1, got ' + str(p.degree())
    p = Polynomial(-12, 1)
    assert p.degree() == 1, 'expected 1, got ' + str(p.degree())
    p = Polynomial(12, 2)
    assert p.degree() == 2, 'expected 2, got ' + str(p.degree())
    p = Polynomial(-12, 2)
    assert p.degree() == 2, 'expected 2, got ' + str(p.degree())

    # Polynomial with many terms:
    p1 = Polynomial(3)
    p2 = Polynomial(-4)
    p3 = Polynomial(2, 1)
    p4 = Polynomial(3, 2)
    p5 = Polynomial(2, 2)
    p6 = Polynomial(-5, 2)
    p7 = Polynomial(42, 3)
    test = p1 + p2 + p3 + p4 + p5 + p6 + p7
    assert test.degree() == 3, 'expected 3, got ' + str(test.degree())
    test = p7 + p6 + p5 + p4 + p3 + p2 + p1
    assert test.degree() == 3, 'expected 3, got ' + str(test.degree())

    print("... all tests passed.")
    return True


def test_evaluate():
    """ Tests method evaluate."""
    print("\nTesting method evaluate ...")

    # Polynomial with no terms:
    p = Polynomial()
    # p.evaluate(1) # Test manually confirmed, evaluate properly raised ValueError

    # Polynomial with one term (a constant):
    p = Polynomial(42)
    assert p.evaluate(1) == 42, 'expected 42, got ' + str(p.evaluate(1))
    p = Polynomial(-42)
    assert p.evaluate(1) == -42, 'expected -42, got ' + str(p.evaluate(1))
    p = Polynomial(42)
    assert p.evaluate(2) == 42, 'expected 42, got ' + str(p.evaluate(2))
    p = Polynomial(-42)
    assert p.evaluate(2) == -42, 'expected -42, got ' + str(p.evaluate(2))
    assert p.evaluate(0) == -42, 'expected -42, got ' + str(p.evaluate(0))

    # Polynomial with one term (evaluating a positive 'x'):
    p = Polynomial(12, 1)
    assert p.evaluate(1) == 12, 'expected 12, got ' + str(p.evaluate(1))
    p = Polynomial(-12, 1)
    assert p.evaluate(1) == -12, 'expected -12, got ' + str(p.evaluate(1))
    p = Polynomial(12, 1)
    assert p.evaluate(2) == 24, 'expected 24, got ' + str(p.evaluate(2))
    p = Polynomial(-12, 1)
    assert p.evaluate(2) == -24, 'expected -24, got ' + str(p.evaluate(2))
    assert p.evaluate(0) == 0, 'expected 0, got ' + str(p.evaluate(0))

    p = Polynomial(12, 2)
    assert p.evaluate(1) == 12, 'expected 12, got ' + str(p.evaluate(1))
    p = Polynomial(-12, 2)
    assert p.evaluate(1) == -12, 'expected -12, got ' + str(p.evaluate(1))
    p = Polynomial(12, 2)
    assert p.evaluate(2) == 48, 'expected 48, got ' + str(p.evaluate(2))
    p = Polynomial(-12, 2)
    assert p.evaluate(2) == -48, 'expected -48, got ' + str(p.evaluate(2))
    assert p.evaluate(0) == 0, 'expected 0, got ' + str(p.evaluate(0))

    # Polynomial with one term (evaluating a negative 'x'):
    p = Polynomial(12, 1)
    assert p.evaluate(-1) == -12, 'expected -12, got ' + str(p.evaluate(-1))
    p = Polynomial(-12, 1)
    assert p.evaluate(-1) == 12, 'expected 12, got ' + str(p.evaluate(-1))
    p = Polynomial(12, 1)
    assert p.evaluate(-2) == -24, 'expected -24, got ' + str(p.evaluate(-2))
    p = Polynomial(-12, 1)
    assert p.evaluate(-2) == 24, 'expected 24, got ' + str(p.evaluate(-2))

    p = Polynomial(12, 2)
    assert p.evaluate(-1) == 12, 'expected 12, got ' + str(p.evaluate(-1))
    p = Polynomial(-12, 2)
    assert p.evaluate(-1) == -12, 'expected -12, got ' + str(p.evaluate(-1))
    p = Polynomial(12, 2)
    assert p.evaluate(-2) == 48, 'expected 48, got ' + str(p.evaluate(-2))
    p = Polynomial(-12, 2)
    assert p.evaluate(-2) == -48, 'expected -48, got ' + str(p.evaluate(-2))

    # Polynomial with many terms (evaluating a positive 'x'):
    p1 = Polynomial(1)
    p2 = Polynomial(2, 1)
    p3 = Polynomial(-2, 1)
    p4 = Polynomial(3, 2)
    p5 = Polynomial(-3, 2)
    p6 = Polynomial(2, 3)
    p7 = Polynomial(-2, 3)
    poly = p1 + p2
    test = poly.evaluate(1)
    assert test == 3, 'expected 3, got ' + str(test)
    poly = p1 + p3
    test = poly.evaluate(1)
    assert test == -1, 'expected -1, got ' + str(test)
    poly = p4 + p1 + p2
    test = poly.evaluate(1)
    assert test == 6, 'expected 6, got ' + str(test)
    poly = p5 + p1 + p2
    test = poly.evaluate(1)
    assert test == 0, 'expected 0, got ' + str(test)
    poly = p6 + p1 + p2 + p4
    test = poly.evaluate(1)
    assert test == 8, 'expected 8, got ' + str(test)
    test = poly.evaluate(2)
    assert test == 33, 'expected 33, got ' + str(test)
    poly = p7 + p1 + p2 + p4
    test = poly.evaluate(0)
    assert test == 1, 'expected 1, got ' + str(test)
    test = poly.evaluate(1)
    assert test == 4, 'expected 4, got ' + str(test)
    test = poly.evaluate(2)
    assert test == 1, 'expected 1, got ' + str(test)
    test = poly.evaluate(0)
    assert test == 1, 'expected 1, got ' + str(test)

    # Polynomial with many terms (evaluating a negative 'x'):
    p1 = Polynomial(1)
    p2 = Polynomial(2, 1)
    p3 = Polynomial(-2, 1)
    p4 = Polynomial(3, 2)
    p5 = Polynomial(-3, 2)
    p6 = Polynomial(2, 3)
    p7 = Polynomial(-2, 3)
    poly = p1 + p2
    test = poly.evaluate(-1)
    assert test == -1, 'expected -1, got ' + str(test)
    poly = p1 + p3
    test = poly.evaluate(-1)
    assert test == 3, 'expected 3, got ' + str(test)
    poly = p4 + p1 + p2
    test = poly.evaluate(-1)
    assert test == 2, 'expected 2, got ' + str(test)
    poly = p5 + p1 + p2
    test = poly.evaluate(-1)
    assert test == -4, 'expected -4, got ' + str(test)
    poly = p6 + p1 + p2 + p4
    test = poly.evaluate(-1)
    assert test == 0, 'expected 0, got ' + str(test)
    test = poly.evaluate(-2)
    assert test == -7, 'expected -7, got ' + str(test)
    poly = p7 + p1 + p2 + p4
    test = poly.evaluate(-1)
    assert test == 4, 'expected 4, got ' + str(test)
    test = poly.evaluate(-2)
    assert test == 25, 'expected 25, got ' + str(test)
    test = poly.evaluate(0)
    assert test == 1, 'expected 1, got ' + str(test)

    print("... all tests passed.")
    return True


def test_add():
    """ Tests method __add__."""
    print("\nTesting method add ...")

    # Polynomials with no terms:
    p1 = Polynomial()
    p2 = Polynomial(12)
    # test = p1 + p2 # [X] Properly raises ValueError
    # test = p2 + p1 # [X] Properly raises ValueError

    # Polynomials that are constants:
    p1 = Polynomial(1)
    p2 = Polynomial(2)
    p3 = Polynomial(3)
    p4 = Polynomial(-2)
    test = p1 + p2
    assert str(test) == '3', 'expected 3, got ' + str(test)
    test = p1 + p2 + p3
    assert str(test) == '6', 'expected 6, got ' + str(test)
    test = p1 + p4
    assert str(test) == '-1', 'expected -1, got ' + str(test)
    test = p1 + p2 + p4
    assert str(test) == '1', 'expected 1, got ' + str(test)
    test = p2 + p4
    assert str(test) == '', 'expected empty string, got ' + str(test)

    # Polynomials with the same exponents:
    p1 = Polynomial(1, 1)
    p2 = Polynomial(2, 1)
    p3 = Polynomial(3, 2)
    p4 = Polynomial(-4, 2)
    p5 = Polynomial(5, 2)
    p6 = Polynomial(-11, 2)
    p7 = Polynomial(-1, 1)
    test = p1 + p2
    assert str(test) == '3x', 'expected 3x, got ' + str(test)
    test = p3 + p5
    assert str(test) == '8x^2', 'expected 8x^2, got ' + str(test)
    test = p3 + p4
    assert str(test) == '-x^2', 'expected -x^2, got ' + str(test)
    test = p3 + p4 + p5
    assert str(test) == '4x^2', 'expected 4x^2, got ' + str(test)
    test = p3 + p4 + p5 + p6
    assert str(test) == '-7x^2', 'expected -7x^2, got ' + str(test)
    test = p1 + p7
    assert str(test) == '', 'expected empty string, got ' + str(test)

    # Polynomials with different exponents:
    p1 = Polynomial(3)
    p2 = Polynomial(-4)
    p3 = Polynomial(2, 1)
    p4 = Polynomial(3, 1)
    p5 = Polynomial(2, 2)
    p6 = Polynomial(-5, 2)
    p7 = Polynomial(42, 3)

    # Constant with an exponent term (both ways):
    test = p1 + p3
    assert str(test) == '2x+3', 'expected 2x+3, got ' + str(test)
    test = p3 + p1
    assert str(test) == '2x+3', 'expected 2x+3, got ' + str(test)  # Same as prev test
    test = p2 + p3
    assert str(test) == '2x-4', 'expected 2x-4, got ' + str(test)
    test = p3 + p2
    assert str(test) == '2x-4', 'expected 2x-4, got ' + str(test)  # Same a prev test

    # All exponents are different (include permutations):
    test = p3 + p5
    assert str(test) == '2x^2+2x', 'expected 2x^2+2x, got ' + str(test)
    test = p5 + p3
    assert str(test) == '2x^2+2x', 'expected 2x^2+2x, got ' + str(test)
    test = p3 + p6 + p7
    assert str(test) == '42x^3-5x^2+2x', 'expected 42x^3-5x^2+2x, got ' + str(test)
    test = p3 + p7 + p6
    assert str(test) == '42x^3-5x^2+2x', 'expected 42x^3-5x^2+2x, got ' + str(test)
    test = p6 + p3 + p7
    assert str(test) == '42x^3-5x^2+2x', 'expected 42x^3-5x^2+2x, got ' + str(test)
    test = p6 + p7 + p3
    assert str(test) == '42x^3-5x^2+2x', 'expected 42x^3-5x^2+2x, got ' + str(test)
    test = p7 + p3 + p6
    assert str(test) == '42x^3-5x^2+2x', 'expected 42x^3-5x^2+2x, got ' + str(test)
    test = p7 + p6 + p3
    assert str(test) == '42x^3-5x^2+2x', 'expected 42x^3-5x^2+2x, got ' + str(test)

    # Mixed exponets (some the same, some different):
    p1 = Polynomial(3)
    p2 = Polynomial(-4)
    p3 = Polynomial(2, 1)
    p4 = Polynomial(3, 2)
    p5 = Polynomial(2, 2)
    p6 = Polynomial(-5, 2)
    p7 = Polynomial(42, 3)

    test = p1 + p2 + p3 + p4 + p5 + p6 + p7
    assert str(test) == '42x^3+2x-1', 'expected 42x^3+2x-1, got ' + str(test)
    test = p7 + p6 + p5 + p4 + p3 + p2 + p1
    assert str(test) == '42x^3+2x-1', 'expected 42x^3+2x-1, got ' + str(test)

    print("... all tests passed.")
    return True


def test_mul():
    """ Tests method __mul__.
    
    The following cases are considered:
    
    1) Properly raises ValueErrors
    
    2) Multiply two constants (a term without an 'x' variable)
    
    3) Multiply two terms with the same exponent
    
    4) Multiply two terms with different exponents
    
    5) Multiply a LHS constant with multiple RHS terms
    
    6) Multiply a LHS term with multiple RHS terms
    
    7) Multiply multiple LHS terms with a single RHS term
    
    8) Multiply multiple LHS terms with multiple RHS terms
    """
    p0 = Polynomial()
    p1 = Polynomial(1)
    p2 = Polynomial(2)
    p3 = Polynomial(-2)
    p4 = Polynomial(1, 1)
    p5 = Polynomial(2, 1)
    p6 = Polynomial(-3, 1)
    p7 = Polynomial(4, 2)
    p8 = Polynomial(-1, 2)
    p9 = Polynomial(-2, 2)
    p10 = Polynomial(1, 3)
    p11 = Polynomial(2, 3)
    p12 = Polynomial(-3, 3)

    print("\nTesting method mul ...")

    # Case 1: Properly raises ValueErrors
    # test = p0 * p1  # [X] Confirmed that ValueError is raised
    # test = p2 * p0  # [X] Confirmed that ValueError is raised

    # Case 2: Multiply two constants (a term without an 'x' variable)
    test = p1 * p2  # 1 * 2 = 2
    assert str(test) == '2', 'expected 2, got ' + str(test)
    test = p1 * p3  # 1 * -2 = -2
    assert str(test) == '-2', 'expected -2, got ' + str(test)
    test = p2 * p3  # 2 * -2 = -4
    assert str(test) == '-4', 'expected -4, got ' + str(test)

    # Case 3: Multiply two terms with the same exponent
    test = p4 * p5  # x * 2x = 2x^2
    assert str(test) == '2x^2', 'expected 2x^2, got ' + str(test)
    test = p5 * p6  # 2x * -3x = -6x^2
    assert str(test) == '-6x^2', 'expected -6x^2, got ' + str(test)
    test = p8 * p9  # -x^2 * -2x^2 = 2x^4
    assert str(test) == '2x^4', 'expected 2, got ' + str(test)

    # Case 4: Multiply single terms with different exponents
    test = p1 * p4  # 1 * x = x
    assert str(test) == 'x', 'expected x, got ' + str(test)
    test = p9 * p1  # -2x^2 * 1 = -2x^2
    assert str(test) == '-2x^2', 'expected -2x^2, got ' + str(test)
    test = p2 * p11  # 2 * 2x^3 = 4x^3
    assert str(test) == '4x^3', 'expected 4x^3, got ' + str(test)
    test = p5 * p8  # 2x * -x^2 = -2x^3
    assert str(test) == '-2x^3', 'expected -2x^3, got ' + str(test)
    test = p6 * p12  # -3x * -3x^3 = 9x^4
    assert str(test) == '9x^4', 'expected 9x^4, got ' + str(test)

    # Case 5: Multiply a LHS constant with multiple RHS terms
    lhs = p1
    rhs = p2 + p4
    test = lhs * rhs  # 1 * (x + 2)
    expected = 'x+2'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p1
    rhs = p2 + p4 + p7 + p12
    test = lhs * rhs  # 1 * (-3x^3 + 4x^2 + x + 2)
    expected = '-3x^3+4x^2+x+2'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p2
    rhs = p2 + p4 + p7 + p12
    test = lhs * rhs  # 2 * (-3x^3 + 4x^2 + x + 2)
    expected = '-6x^3+8x^2+2x+4'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p3
    rhs = p2 + p4 + p7 + p12
    test = lhs * rhs  # -2 * (-3x^3 + 4x^2 + x + 2)
    expected = '6x^3-8x^2-2x-4'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)

    # Case 6: Multiply a LHS term with multiple RHS terms
    lhs = p4
    rhs = p2 + p4
    test = lhs * rhs  # x * (x + 2)
    expected = 'x^2+2x'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p5
    rhs = p2 + p4 + p7 + p12
    test = lhs * rhs  # 2x * (-3x^3 + 4x^2 + x + 2)
    expected = '-6x^4+8x^3+2x^2+4x'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p8
    rhs = p2 + p4 + p7 + p12
    test = lhs * rhs  # -x^2 * (-3x^3 + 4x^2 + x + 2)
    expected = '3x^5-4x^4-x^3-2x^2'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p12
    rhs = p2 + p4 + p7 + p12
    test = lhs * rhs  # -3x^3 * (-3x^3 + 4x^2 + x + 2)
    expected = '9x^6-12x^5-3x^4-6x^3'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)

    # Case 7: Multiply multiple LHS terms with a single RHS term
    # Mirrored tests from Case 6
    lhs = p2 + p4
    rhs = p4
    test = lhs * rhs  # x * (x + 2)
    expected = 'x^2+2x'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p2 + p4 + p7 + p12
    rhs = p5
    test = lhs * rhs  # 2x * (-3x^3 + 4x^2 + x + 2)
    expected = '-6x^4+8x^3+2x^2+4x'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p2 + p4 + p7 + p12
    rhs = p8
    test = lhs * rhs  # -x^2 * (-3x^3 + 4x^2 + x + 2)
    expected = '3x^5-4x^4-x^3-2x^2'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p2 + p4 + p7 + p12
    rhs = p12
    test = lhs * rhs  # -3x^3 * (-3x^3 + 4x^2 + x + 2)
    expected = '9x^6-12x^5-3x^4-6x^3'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)

    # Case 8: Multiply multiple LHS terms with multiple RHS terms
    lhs = p2 + p4
    rhs = p2 + p4
    test = lhs * rhs  # (x + 2) * (x + 2)
    expected = 'x^2+4x+4'
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)
    lhs = p2 + p4 + p7 + p12
    rhs = p2 + p4 + p7 + p12
    test = lhs * rhs  # (-3x^3 + 4x^2 + x + 2) * (-3x^3 + 4x^2 + x + 2)
    expected = '9x^6-24x^5+10x^4-4x^3+17x^2+4x+4'  # Calculated using WolframAlpha
    assert str(test) == expected, 'expected ' + expected + ', got ' + str(test)

    print("... all tests passed.")
    return True


if __name__ == "__main__":
    assert test_str()
    assert test_repr()
    assert test_degree()
    assert test_evaluate()
    assert test_add()
    assert test_mul()

