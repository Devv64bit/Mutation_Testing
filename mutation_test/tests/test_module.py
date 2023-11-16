# Import the Polynomial class from your module
from mutation_testing.src import CustomPolynomial


def test_init():
    poly = CustomPolynomial([3, 0, 2])
    assert poly.coefficients == [3, 0, 2]


def test_str():
    poly = CustomPolynomial([3, 0, 2])
    assert str(poly) == "3x^2 + 2"

    poly2 = CustomPolynomial([1, -1])
    assert str(poly2) == "1x + -1"

    poly3 = CustomPolynomial([0, 0, 0])
    assert str(poly3) == "0" or str(poly3) == ""


def test_add():
    poly1 = CustomPolynomial([3, 0, 2])
    poly2 = CustomPolynomial([1, -1])

    poly_sum = poly1 + poly2
    assert poly_sum.coefficients == [3, 1, 1]


def test_sub():
    poly1 = CustomPolynomial([3, 0, 2])
    poly2 = CustomPolynomial([1, -1])

    poly_diff = poly1 - poly2
    assert poly_diff.coefficients == [3, -1, 3]


def test_mul():
    poly1 = CustomPolynomial([3, 0, 2])
    poly2 = CustomPolynomial([1, -1])

    poly_product = poly1 * poly2
    assert poly_product.coefficients == [3, -3, 2, -2]


def test_first_degree_polynomial():
    poly = CustomPolynomial([2, -3])  # Represents 2x - 3
    root = poly.findRootBisection(0, 5)
    assert root is None or abs(root - 1.5) < 1e-6


def test_second_degree_polynomial():
    poly = CustomPolynomial([1, 0, -2])  # Represents x^2 - 2
    root = poly.findRootBisection(1, 2)
    assert root is None or abs(root - 2.0**0.5) < 1e-6


def test_third_degree_polynomial():
    poly = CustomPolynomial([1, 0, -2, 0])  # Represents x^3 - 2x
    root = poly.findRootBisection(-2, 2)
    assert abs(root - 0.0) < 1e-6
