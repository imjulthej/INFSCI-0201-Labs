import ast
import os
from typing import Tuple, List, Dict, Union

def read_python_file(file_path: str) -> Tuple[str, ast.AST]:
    with open(file_path, "r") as file:
        content = file.read()
    tree = ast.parse(content, filename=file_path)
    return content, tree

def extract_file_structure(content: str, tree: ast.AST) -> Dict[str, Union[int, List[str]]]:
    total_lines = len(content.splitlines())
    imports = [alias.name for node in ast.walk(tree)
               if isinstance(node, (ast.Import, ast.ImportFrom))
               for alias in node.names]

    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    functions = [node.name for node in ast.walk(tree)
                 if isinstance(node, ast.FunctionDef) and not isinstance(getattr(node, 'parent', None), ast.ClassDef)]

    return {
        "total_lines": total_lines,
        "imports": imports,
        "classes": classes,
        "functions": functions,
    }

def extract_docstrings(tree: ast.AST) -> Dict[str, str]:
    docstrings = {}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            name = node.name
            docstring = ast.get_docstring(node)
            if docstring:
                docstrings[name] = docstring
            else:
                kind = "class" if isinstance(node, ast.ClassDef) else "function"
                docstrings[name] = f"{kind} {name}: DocString not found."
    return docstrings

def has_type_annotations(node: ast.FunctionDef) -> bool:
    return any(arg.annotation is not None for arg in node.args.args) or (node.returns is not None)

def check_type_annotations(tree: ast.AST) -> Dict[str, Union[List[str], bool]]:
    missing = [node.name for node in ast.walk(tree)
               if isinstance(node, ast.FunctionDef) and not has_type_annotations(node)]
    return {
        "missing_type_annotations": missing,
        "all_annotated": len(missing) == 0
    }

def check_naming_conventions(tree: ast.AST) -> Dict[str, Union[List[str], bool]]:
    invalid_classes = [node.name for node in ast.walk(tree)
                       if isinstance(node, ast.ClassDef) and (not node.name[0].isupper() or '_' in node.name)]

    invalid_functions = [node.name for node in ast.walk(tree)
                         if isinstance(node, ast.FunctionDef) and (not node.name.islower() or " " in node.name)]

    return {
        "invalid_class_names": invalid_classes,
        "invalid_function_names": invalid_functions,
        "all_valid": len(invalid_classes) == 0 and len(invalid_functions) == 0
    }

def generate_report(structure: dict, docstrings: dict,
                     annotations: dict, naming: dict) -> str:
    lines = ["=== File Structure ==="]
    lines.append(f"Total lines of code: {structure['total_lines']}")
    lines.append(f"Imported packages: {', '.join(structure['imports'])}")
    lines.append(f"Classes: {', '.join(structure['classes'])}")
    lines.append(f"Functions: {', '.join(structure['functions'])}\n")

    lines.append("=== DocStrings ===")
    for name, doc in docstrings.items():
        lines.append(f"{name}:")
        lines.append(f"{doc}\n")

    lines.append("=== Type Annotations ===")
    if annotations["all_annotated"]:
        lines.append("All functions and methods use type annotations.\n")
    else:
        lines.append("Functions/methods without type annotations: " + ", ".join(annotations["missing_type_annotations"]) + "\n")

    lines.append("=== Naming Conventions ===")
    if naming["all_valid"]:
        lines.append("All names adhere to the specified naming conventions.\n")
    else:
        if naming["invalid_class_names"]:
            lines.append("Classes not in CamelCase: " + ", ".join(naming["invalid_class_names"]))
        if naming["invalid_function_names"]:
            lines.append("Functions/methods not in snake_case: " + ", ".join(naming["invalid_function_names"]))

    return "\n".join(lines)

def write_report(file_path: str, content: str) -> None:
    directory = os.path.dirname(file_path)
    base_name = os.path.basename(file_path)
    report_name = f"style_report_{base_name}.txt"
    full_path = os.path.join(directory, report_name)
    with open(full_path, "w") as file:
        file.write(content)
    print(f"Report generated: {full_path}")

def main():
    file_path = input("Please enter the path to your Python file (no quotations): ").strip()
    content, tree = read_python_file(file_path)

    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            setattr(child, 'parent', node)

    structure = extract_file_structure(content, tree)
    docstrings = extract_docstrings(tree)
    annotations = check_type_annotations(tree)
    naming = check_naming_conventions(tree)

    report = generate_report(structure, docstrings, annotations, naming)
    write_report(file_path, report)

if __name__ == "__main__":
    main()
