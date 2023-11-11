import ast
import sys

def traverse_and_print_functions(node, text, indent=0):
    if isinstance(node, ast.FunctionDef):
        # Print function name and parameters
        if node.name == text:
            for statement in node.body:
                print(ast.unparse(node).replace('\n', f'\n{" " * indent}'))

    for child_node in ast.iter_child_nodes(node):
        traverse_and_print_functions(child_node, text, indent=indent + 4)

if __name__ == "__main__":
    file = sys.argv[1]
    func = sys.argv[2]

    with open(file, 'r') as f:
        data = f.read()

    tree = ast.parse(data)

    traverse_and_print_functions(tree, func)