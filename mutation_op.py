from copy import deepcopy
import random


class MutationOperators:
    # @staticmethod
    def mutateCoe(coefficient, index=0):
        mutation_type = random.choice(["replace", "scale", "add"])

        if mutation_type == "replace":
            mutated_coefficient = random.uniform(-10, 10)
        elif mutation_type == "scale":
            mutation_factor = random.uniform(0.5, 1.5)
            mutated_coefficient = coefficient * mutation_factor
        else:  # mutation_type == "add"
            mutation_value = random.uniform(-5, 5)
            mutated_coefficient = coefficient + mutation_value
        return mutated_coefficient

    # @staticmethod
    def mutateArithmeticOp(poly, operation):
        mutated_poly = deepcopy(poly)
        mutated_poly.coefficients = [
            operation(coef) for coef in mutated_poly.coefficients]
        return mutated_poly

    # @staticmethod
    def mutateZeroCoe(poly, index):
        mutated_poly = deepcopy(poly)
        mutated_poly.coefficients[index] = 0
        return mutated_poly

    # @staticmethod
    def redundantCode(coefficients):
        # Mutation: Introduce a redundant multiplication by 1
        return [coef * 1 for coef in coefficients]

    # @staticmethod
    def degreeMutate(poly):
        mutated_poly = deepcopy(poly)
        mutated_poly.coefficients.insert(1, 1)
        return mutated_poly
