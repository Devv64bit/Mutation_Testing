# Import the Polynomial class from your module
from src import CustomPolynomial


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


def test_polynomial_add_zero():
    # Test that adding zero polynomial has no effect
    poly = CustomPolynomial([3, 0, 2])
    zero_poly = CustomPolynomial([0])
    assert (poly + zero_poly).coefficients == poly.coefficients


def test_polynomial_subtract_self():
    # Test that subtracting the same polynomial results in a zero polynomial
    poly = CustomPolynomial([3, 0, 2])
    assert (poly - poly).coefficients == [0] * len(poly.coefficients)


def test_polynomial_multiply_by_zero():
    # Test that multiplying by a zero polynomial results in all coefficients being zero
    poly = CustomPolynomial([3, 0, 2])
    zero_poly = CustomPolynomial([0])
    assert (poly * zero_poly).coefficients == [0] * (
        len(poly.coefficients) + len(zero_poly.coefficients) - 1)


def test_negative_and_fractional_coefficients():
    poly = CustomPolynomial([-1.5, 3, 0, -2.5])
    assert poly.coefficients == [-1.5, 3, 0, -
                                 2.5], "Should handle negative and fractional coefficients"


def test_str_with_leading_zeros():
    poly = CustomPolynomial([0, 0, 1])
    assert str(poly) == "1", "Should ignore leading zero coefficients"


def test_str_with_single_coefficient():
    poly = CustomPolynomial([42])
    assert str(
        poly) == "42", "Should handle single coefficient polynomials correctly"


def test_operations_with_zero_polynomial():
    zero_poly = CustomPolynomial([0])
    poly = CustomPolynomial([1, -1, 1])
    assert (poly + zero_poly).coefficients == poly.coefficients, "Adding zero should not change the polynomial"
    assert (poly - zero_poly).coefficients == poly.coefficients, "Subtracting zero should not change the polynomial"
    assert (poly * zero_poly).coefficients == [0 for _ in range(len(poly.coefficients) + len(
        zero_poly.coefficients) - 1)], "Multiplying by zero should result in a zero polynomial"


def test_multiply_by_monomial():
    poly1 = CustomPolynomial([2, 3])
    poly2 = CustomPolynomial([1, 0])  # Represents x
    product = poly1 * poly2
    assert product.coefficients == [
        2, 3, 0], "Should correctly multiply a polynomial by a monomial"


def test_find_root_edge_cases():
    poly = CustomPolynomial([1, 0, -4])  # Roots at x = -2 and x = 2
    root = poly.findRootBisection(-3, -1)
    assert abs(root + 2) < 1e-6, "Should find a negative root"
    root = poly.findRootBisection(1, 3)
    assert abs(root - 2) < 1e-6, "Should find a positive root"


def test_subtraction_to_zero():
    poly1 = CustomPolynomial([1, -1, 1])
    poly2 = CustomPolynomial([1, -1, 1])
    result = poly1 - poly2
    assert all(coef == 0 for coef in result.coefficients), "Subtracting the polynomial from itself should yield a zero polynomial"


def test_evaluate_at_zero():
    poly = CustomPolynomial([3, -4, 2])
    assert poly.evaluate(
        0) == 2, "Evaluating at x=0 should return the constant term"


def test_add_different_lengths():
    poly1 = CustomPolynomial([2, 3])
    poly2 = CustomPolynomial([1, 0, -5])
    result = poly1 + poly2
    assert result.coefficients == [
        1, 2, -2], "Should correctly add polynomials of different lengths"


def test_multiply_by_non_unit_monomial():
    poly1 = CustomPolynomial([1, 3, -2])
    poly2 = CustomPolynomial([2, 0])  # Represents 2x
    product = poly1 * poly2
    assert product.coefficients == [
        2, 6, -4, 0], "Should correctly multiply a polynomial by a monomial with a coefficient other than 1"
