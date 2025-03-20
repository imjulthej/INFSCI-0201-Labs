import ast
import os

class StyleChecker:
    def __init__(self, file_path):
        self.file_path = file_path
        self.tree = None
        self.report = {
            "file_structure": {
                "total_lines": 0,
                "imports": [],
                "classes": [],
                "functions": [],
            },
            "docstrings": {},
            "type_annotations": {
                "missing_type_annotations": [],
                "all_annotated": False,
            },
            "naming_conventions": {
                "invalid_class_names": [],
                "invalid_function_names": [],
                "all_valid": False,
            },
        }

    def parse_file(self):
        """Read and parse the Python file using AST."""
        with open(self.file_path, "r") as file:
            content = file.read()
            self.tree = ast.parse(content, filename=self.file_path)
            self.report["file_structure"]["total_lines"] = len(content.splitlines())

    def analyze_structure(self):
        """Analyze the file structure (imports, classes, functions)."""
        stack = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    self.report["file_structure"]["imports"].append(alias.name)
            elif isinstance(node, ast.ClassDef):
                self.report["file_structure"]["classes"].append(node.name)
                self._extract_docstring(node, "class")
                stack.append(node)
            elif isinstance(node, ast.FunctionDef):
                if stack and isinstance(stack[-1], ast.ClassDef):
                    func_name = f"{stack[-1].name}_{node.name}"
                else:
                    func_name = node.name
                self.report["file_structure"]["functions"].append(func_name)
                self._extract_docstring(node, "function")
            elif isinstance(node, ast.ClassDef) or isinstance(node, ast.FunctionDef):
                if stack and stack[-1] == node:
                    stack.pop()

    def _extract_docstring(self, node, node_type):
        """Extract docstrings for classes, methods, and functions."""
        docstring = ast.get_docstring(node)
        if docstring:
            self.report["docstrings"][node.name] = docstring
        else:
            self.report["docstrings"][node.name] = f"{node_type} {node.name}: DocString not found."

    def check_type_annotations(self):
        """Check for missing type annotations in functions and methods."""
        missing_annotations = []
        for node in ast.walk(self.tree):
            if isinstance(node, ast.FunctionDef):
                if not self._has_type_annotations(node):
                    missing_annotations.append(node.name)
        self.report["type_annotations"]["missing_type_annotations"] = missing_annotations
        self.report["type_annotations"]["all_annotated"] = not missing_annotations

    def _has_type_annotations(self, node):
        """Check if a function or method has type annotations."""
        return any(
            arg.annotation is not None
            for arg in node.args.args
        ) or (node.returns is not None)

    def check_naming_conventions(self):
        invalid_class_names = []
        invalid_function_names = []

        for node in ast.walk(self.tree):
            if isinstance(node, ast.ClassDef):
                if not node.name[0].isupper() or "_" in node.name:
                    invalid_class_names.append(node.name)
            elif isinstance(node, ast.FunctionDef):
                if not node.name.islower() or " " in node.name:
                    invalid_function_names.append(node.name)

        self.report["naming_conventions"]["invalid_class_names"] = invalid_class_names
        self.report["naming_conventions"]["invalid_function_names"] = invalid_function_names
        self.report["naming_conventions"]["all_valid"] = not (
            invalid_class_names or invalid_function_names
        )

    def generate_report(self):
        """Generate the report as a string."""
        report_lines = []

        # File Structure
        report_lines.append("=== File Structure ===")
        report_lines.append(f"Total lines of code: {self.report['file_structure']['total_lines']}")
        report_lines.append(f"Imported packages: {', '.join(self.report['file_structure']['imports'])}")
        report_lines.append(f"Classes: {', '.join(self.report['file_structure']['classes'])}")
        report_lines.append(f"Functions: {', '.join(self.report['file_structure']['functions'])}")
        report_lines.append("")

        # DocStrings
        report_lines.append("=== DocStrings ===")
        for name, docstring in self.report["docstrings"].items():
            report_lines.append(f"{name}:\n{docstring}\n")
        report_lines.append("")

        # Type Annotations
        report_lines.append("=== Type Annotations ===")
        if self.report["type_annotations"]["all_annotated"]:
            report_lines.append("All functions and methods use type annotations.")
        else:
            report_lines.append(
                "Functions/methods without type annotations: "
                + ", ".join(self.report["type_annotations"]["missing_type_annotations"])
            )
        report_lines.append("")

        # Naming Conventions
        report_lines.append("=== Naming Conventions ===")
        if self.report["naming_conventions"]["all_valid"]:
            report_lines.append("All names adhere to the specified naming conventions.")
        else:
            if self.report["naming_conventions"]["invalid_class_names"]:
                report_lines.append(
                    "Classes not in CamelCase: "
                    + ", ".join(self.report["naming_conventions"]["invalid_class_names"])
                )
            if self.report["naming_conventions"]["invalid_function_names"]:
                report_lines.append(
                    "Functions/methods not in snake_case: "
                    + ", ".join(self.report["naming_conventions"]["invalid_function_names"])
                )
        report_lines.append("")

        return "\n".join(report_lines)

    def write_report(self):
        report_content = self.generate_report()
        directory = os.path.dirname(self.file_path)
        report_file_name = f"style_report_{os.path.basename(self.file_path)}.txt"
        report_file_path = os.path.join(directory, report_file_name)
        with open(report_file_path, "w") as report_file:
            report_file.write(report_content)
        print(f"Report generated: {report_file_path}")

if __name__ == "__main__":
    file_path = "assignment1\example.py"
    checker = StyleChecker(file_path)
    checker.parse_file()
    checker.analyze_structure()
    checker.check_type_annotations()
    checker.check_naming_conventions()
    checker.write_report()