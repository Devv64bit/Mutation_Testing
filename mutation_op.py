import random
import mutpy

class PolynomialMutationOperators:
    @staticmethod
    def change_coefficients(source_code):
        tree = mutpy.ast_parse(source_code)
        class_definition = tree.body[0]
        init_method = next((node for node in class_definition.body if isinstance(node, mutpy.ast.FunctionDef) and node.name == 'init'), None)
        if init_method:
            for node in mutpy.walk(init_method):
                if isinstance(node, mutpy.ast.List):
                    for i, element in enumerate(node.elts):
                        if isinstance(element, mutpy.ast.Num):
                            node.elts[i] = mutpy.ast.Num(n=random.randint(-10, 10))
        mutated_code = mutpy.to_source(tree)
        return mutated_code

    @staticmethod
    def modify_arithmetic_operations(source_code):
        tree = mutpy.ast_parse(source_code)
        class_definition = tree.body[0]
        add_method = next((node for node in class_definition.body if isinstance(node, mutpy.ast.FunctionDef) and node.name == 'add'), None)
        sub_method = next((node for node in class_definition.body if isinstance(node, mutpy.ast.FunctionDef) and node.name == 'sub'), None)
        if add_method:
            for node in mutpy.walk(add_method):
                if isinstance(node, mutpy.ast.BinOp) and isinstance(node.op, mutpy.ast.Add):
                    node.op = mutpy.ast.Sub()
        if sub_method:
            for node in mutpy.walk(sub_method):
                if isinstance(node, mutpy.ast.BinOp) and isinstance(node.op, mutpy.ast.Sub):
                    node.op = mutpy.ast.Add()
        mutated_code = mutpy.to_source(tree)
        return mutated_code

    @staticmethod
    def introduce_redundant_code(source_code):
        tree = mutpy.ast_parse(source_code)
        class_definition = tree.body[0]
        evaluate_method = next((node for node in class_definition.body if isinstance(node, mutpy.ast.FunctionDef) and node.name == 'evaluate'), None)
        if evaluate_method:
            for node in mutpy.walk(evaluate_method):
                if isinstance(node, mutpy.ast.For):
                    node.body.append(mutpy.ast.Pass())
        mutated_code = mutpy.to_source(tree)
        return mutated_code

    @staticmethod
    def change_exponents(source_code):
        tree = mutpy.ast_parse(source_code)
        class_definition = tree.body[0]
        str_method = next((node for node in class_definition.body if isinstance(node, mutpy.ast.FunctionDef) and node.name == 'str'), None)
        if str_method:
            for node in mutpy.walk(str_method):
                if isinstance(node, mutpy.ast.BinOp) and isinstance(node.op, mutpy.ast.Add) and isinstance(node.right, mutpy.ast.BinOp) and isinstance(node.right.op, mutpy.ast.Add):
                    node.right.op = mutpy.ast.Sub()
        mutated_code = mutpy.to_source(tree)
        return mutated_code