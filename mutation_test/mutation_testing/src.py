from mutation_op import MutationOperators


class CustomPolynomial:
    def __init__(self, coefficients):
        """
        Initialize a custom polynomial with a list of coefficients.
        The coefficients list should be in descending order of the exponent,
        for example: [3, 0, 2] represents 3x^2 + 2.
        """
        self.coefficients = coefficients

    def __str__(self):
        """
        Return a string representation of the custom polynomial.
        """
        if len(self.coefficients) == 0:
            return "0"

        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef == 0:
                continue
            term = str(coef)
            if i < len(self.coefficients) - 1:
                if i == len(self.coefficients) - 2:
                    term += "x"
                else:
                    term += "x^" + str(len(self.coefficients) - i - 1)
            terms.append(term)
        return " + ".join(terms)

    def __add__(self, other):
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * \
            (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [
            0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a + b for a,
                               b in zip(padded_self, padded_other)]

        # Mutation: Change the sign of the first coefficient
        result_coefficients[0] = MutationOperators.mutateCoe(
            result_coefficients[0], index=0)

        return CustomPolynomial(result_coefficients)

    def __sub__(self, other):
        max_length = max(len(self.coefficients), len(other.coefficients))
        padded_self = [0] * \
            (max_length - len(self.coefficients)) + self.coefficients
        padded_other = [
            0] * (max_length - len(other.coefficients)) + other.coefficients
        result_coefficients = [a - b for a,
                               b in zip(padded_self, padded_other)]

        # Apply the mutation to coefficients only, not to the operation
        result_coefficients = [MutationOperators.mutateCoe(
            coef) for coef in result_coefficients]

        return CustomPolynomial(result_coefficients)

    def __mul__(self, other):
        result_deg = len(self.coefficients) + len(other.coefficients) - 1
        result_coefficients = [0] * result_deg
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                result_coefficients[i + j] += self.coefficients[i] * \
                    other.coefficients[j]

        # Mutation: Introduce a redundant multiplication by 1
        result_coefficients = MutationOperators.redundantCode(
            result_coefficients)

        return CustomPolynomial(result_coefficients)

    def evaluateCoe(self, x):
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** (len(self.coefficients) - i - 1))

        # Mutation: Multiply the result by a constant factor
        result *= MutationOperators.mutateCoe(2)

        return result

    def getDerivativeCoe(self):
        # Mutation: Change the coefficient of the derivative
        return [i * coef + MutationOperators.mutateCoe(1) for (i, coef) in enumerate(list(reversed(self.coefficients))[:-1])]

    def findRootBisection(self, interval_start, interval_end, epsilon=1e-6, max_iterations=100):
        """
        Find the root of the custom polynomial using the bisection method.

        Parameters:
        - interval_start: The start of the interval for the bisection.
        - interval_end: The end of the interval for the bisection.
        - epsilon: The desired precision for the root.
        - max_iterations: The maximum number of iterations for the bisection.

        Returns:
        - The estimated root within the specified interval and precision.
        """
        if self.evaluateCoe(interval_start) * self.evaluateCoe(interval_end) > 0:
            # Indicate that the chosen interval does not contain a root.
            return None

        for _ in range(max_iterations):
            midpoint = (interval_start + interval_end) / 2
            print(midpoint)
            if abs(self.evaluateCoe(midpoint)) < epsilon:
                return midpoint

            # Mutation: Increase the precision of the bisection
            if self.evaluateCoe(midpoint) * self.evaluateCoe(interval_start) < 0:
                interval_end = midpoint + \
                    MutationOperators.mutateCoe(1)
            else:
                interval_start = midpoint - \
                    MutationOperators.mutateCoe(1)

        return None  # Indicate that the bisection method did not converge within the maximum number of iterations
