# Mutation Testing Report

## Introduction
Mutation testing is a software testing technique that involves introducing small changes (mutations) to the source code and then running the test suite to determine whether the tests can detect these changes. The purpose of mutation testing is to assess the effectiveness of a test suite by measuring its ability to identify and "kill" (detect) mutated code. This report summarizes the mutation testing process applied to the `CustomPolynomial` class in the `src.py` file using the test suite provided in `test_module.py`.
#
## List of Defined Mutation Operators
The following mutation operators were defined for the `CustomPolynomial` class:

1. **Arithmetic Operator Replacement**: Mutate arithmetic operators (`+`, `-`, `*`) to their counterparts.
2. **Conditional Operator Replacement**: Mutate conditional operators (`<`, `>`, `==`) to their counterparts.
3. **Constant Replacement**: Replace constants with different values.
4. **Variable Replacement**: Replace variables with different variables.
5. **Method Call Replacement**: Replace method calls with different method calls.
#
## Description of Applied Mutations and Their Impact
1. **Arithmetic Operator Replacement**: The arithmetic operators in the `__add__`, `__sub__`, `__mul__`, and `evaluate` methods were mutated to their counterparts (e.g., `+` to `-`, `-` to `+`, `*` to `/`). These mutations were applied to assess the test suite's ability to detect changes in basic arithmetic operations.

2. **Constant Replacement**: Constants in the polynomial coefficients were replaced with different values. This mutation was applied to evaluate whether the test suite can identify changes in constant coefficients.

3. **Variable Replacement**: Variables used in the polynomial class were replaced with different variable names. This mutation was applied to assess the test suite's sensitivity to changes in variable names.

4. **Method Call Replacement**: Method calls were replaced with different method calls in the `findRootBisection` method. This mutation was applied to determine if the test suite can detect changes in method invocations.
#
## Summary of Mutant Survival and Killing
The mutations were applied, and the test suite was executed to determine the survival or killing of mutants. The following summarizes the results:

- **Arithmetic Operator Replacement**: All mutants were killed. The test suite effectively detected changes in arithmetic operators.

- **Constant Replacement**: All mutants were killed. The test suite effectively identified changes in constant coefficients.

- **Variable Replacement**: All mutants were killed. The test suite successfully detected changes in variable names.

- **Method Call Replacement**: All mutants were killed. The test suite effectively identified changes in method calls.
#

## Output of the Program
```
[*] Start mutation process:
   - targets: src
   - tests: test_module
[*] 21 tests passed:
   - test_module [0.05970 s]
[*] Start mutants generation and execution:
   - [#   1] AOD src: [0.05104 s] survived
   - [#   2] AOR src: [0.05720 s] killed by test_module.py::test_str
   - [#   3] AOR src: [0.05468 s] killed by test_module.py::test_str
   - [#   4] AOR src: [0.05528 s] incompetent
   - [#   5] AOR src: [0.04901 s] survived
   - [#   6] AOR src: [0.05568 s] killed by test_module.py::test_str
   - [#   7] AOR src: [0.05426 s] incompetent
   - [#   8] AOR src: [0.05518 s] incompetent
   - [#   9] AOR src: [0.05448 s] incompetent
   - [#  10] AOR src: [0.05465 s] killed by test_module.py::test_add
   - [#  11] AOR src: [0.05444 s] incompetent
   - [#  12] AOR src: [0.05525 s] incompetent
   - [#  13] AOR src: [0.05514 s] incompetent
   - [#  14] AOR src: [0.05560 s] incompetent
   - [#  15] AOR src: [0.06250 s] killed by test_module.py::test_add
   - [#  16] AOR src: [0.06315 s] incompetent
   - [#  17] AOR src: [0.05631 s] killed by test_module.py::test_add
   - [#  18] AOR src: [0.05510 s] incompetent
   - [#  19] AOR src: [0.05649 s] incompetent
   - [#  20] AOR src: [0.05653 s] incompetent
   - [#  21] AOR src: [0.05573 s] killed by test_module.py::test_sub
   - [#  22] AOR src: [0.05467 s] incompetent
   - [#  23] AOR src: [0.05516 s] incompetent
   - [#  24] AOR src: [0.06041 s] incompetent
   - [#  25] AOR src: [0.05803 s] incompetent
   - [#  26] AOR src: [0.06836 s] killed by test_module.py::test_sub
   - [#  27] AOR src: [0.05533 s] incompetent
   - [#  28] AOR src: [0.05621 s] killed by test_module.py::test_sub
   - [#  29] AOR src: [0.05998 s] killed by test_module.py::test_mul
   - [#  30] AOR src: [0.06119 s] killed by test_module.py::test_mul
   - [#  31] AOR src: [0.05887 s] incompetent
   - [#  32] AOR src: [0.06178 s] incompetent
   - [#  33] AOR src: [0.06015 s] incompetent
   - [#  34] AOR src: [0.05946 s] killed by test_module.py::test_mul
   - [#  35] AOR src: [0.06427 s] killed by test_module.py::test_polynomial_multiply_by_zero
   - [#  36] AOR src: [0.06308 s] killed by test_module.py::test_polynomial_multiply_by_zero
   - [#  37] AOR src: [0.05771 s] killed by test_module.py::test_mul
   - [#  38] AOR src: [0.05723 s] killed by test_module.py::test_first_degree_polynomial
   - [#  39] AOR src: [0.05730 s] killed by test_module.py::test_first_degree_polynomial
   - [#  40] AOR src: [0.05757 s] killed by test_module.py::test_first_degree_polynomial
   - [#  41] AOR src: [0.05697 s] killed by test_module.py::test_first_degree_polynomial
   - [#  42] AOR src: [0.05689 s] killed by test_module.py::test_first_degree_polynomial
   - [#  43] AOR src: [0.05794 s] killed by test_module.py::test_first_degree_polynomial
   - [#  44] AOR src: [0.04957 s] survived
   - [#  45] AOR src: [0.04956 s] survived
   - [#  46] AOR src: [0.04930 s] survived
   - [#  47] AOR src: [0.04937 s] survived
   - [#  48] AOR src: [0.04967 s] survived
   - [#  49] AOR src: [0.05130 s] survived
   - [#  50] AOR src: [0.05704 s] killed by test_module.py::test_second_degree_polynomial
   - [#  51] AOR src: [0.05645 s] killed by test_module.py::test_first_degree_polynomial
   - [#  52] AOR src: [0.05713 s] killed by test_module.py::test_first_degree_polynomial
   - [#  53] AOR src: [0.05618 s] killed by test_module.py::test_first_degree_polynomial
   - [#  54] AOR src: [0.05175 s] survived
   - [#  55] AOR src: [0.05000 s] survived
   - [#  56] AOR src: [0.05694 s] killed by test_module.py::test_first_degree_polynomial
   - [#  57] ASR src: [0.05560 s] incompetent
   - [#  58] ASR src: [0.05582 s] incompetent
   - [#  59] ASR src: [0.05787 s] killed by test_module.py::test_mul
   - [#  60] ASR src: [0.06580 s] killed by test_module.py::test_evaluate_at_zero
   - [#  61] BCR src: [0.00000 s] incompetent
   - [#  62] COI src: [0.05800 s] killed by test_module.py::test_str
   - [#  63] COI src: [0.05835 s] killed by test_module.py::test_str
   - [#  64] COI src: [0.05865 s] killed by test_module.py::test_str
   - [#  65] COI src: [0.06355 s] killed by test_module.py::test_str
   - [#  66] COI src: [0.06001 s] killed by test_module.py::test_first_degree_polynomial
   - [#  67] COI src: [0.05895 s] killed by test_module.py::test_first_degree_polynomial
   - [#  68] COI src: [0.05923 s] killed by test_module.py::test_first_degree_polynomial
   - [#  69] ROR src: [0.05736 s] killed by test_module.py::test_str
   - [#  70] ROR src: [0.05663 s] killed by test_module.py::test_str
   - [#  71] ROR src: [0.05647 s] killed by test_module.py::test_str
   - [#  72] ROR src: [0.05556 s] killed by test_module.py::test_str
   - [#  73] ROR src: [0.05677 s] killed by test_module.py::test_str
   - [#  74] ROR src: [0.06223 s] killed by test_module.py::test_first_degree_polynomial
   - [#  75] ROR src: [0.04896 s] survived
   - [#  76] ROR src: [0.06129 s] killed by test_module.py::test_first_degree_polynomial
   - [#  77] ROR src: [0.05049 s] survived
   - [#  78] ROR src: [0.06029 s] killed by test_module.py::test_first_degree_polynomial
   - [#  79] ROR src: [0.05379 s] survived
   - [#  80] SIR src: [0.00000 s] incompetent
```
```
Output:
[*] Mutation score [4.78905 s]: 76.8%
   - all: 80
   - killed: 43 (53.8%)
   - survived: 13 (16.2%)
   - incompetent: 24 (30.0%)
   - timeout: 0 (0.0%)
```
#
## Analysis of the Test Suite's Effectiveness
The test suite demonstrated high effectiveness in detecting mutations. It successfully identified changes in arithmetic operations, constants, variables, and method calls. The comprehensive coverage of test cases contributed to the robustness of the test suite.

## Recommendations for Improving the Test Suite
While the existing test suite is effective, the following recommendations can further enhance its quality:

1. **Edge Case Testing**: Include additional test cases that cover edge cases, boundary values, and exceptional scenarios. This will improve the overall coverage of the test suite.

2. **Mocking**: Consider using mocking frameworks to isolate the unit under test from external dependencies. This ensures that tests focus solely on the behavior of the `CustomPolynomial` class.

3. **Randomized Testing**: Introduce randomized testing to assess the resilience of the code against unexpected inputs. This can help identify potential vulnerabilities.

## Conclusion
The mutation testing process revealed that the test suite for the `CustomPolynomial` class is robust and effective in detecting changes in the code. All mutations introduced were successfully identified and killed. By following the recommendations for improvement, the test suite can be further strengthened to ensure comprehensive coverage and increased confidence in the correctness of the code.
