import os

# TODO: Make parent class FileAnalyzer
# TODO: Implement children JavaFileAnalyzer and PythonFileAnalyzer

class Analyzer:

    valid_ext = (".py", ".class")

    def __init__(self, project_name):
        self.project_name = project_name
        self.valid_files = self.get_valid_files()
        self.lines_test = 0
        self.lines_code = 0
        self.classes_test = 0
        self.classes_code = 0
        self.functions_test = 0
        self.functions_code = 0

    def run(self):
        for f in self.valid_files:
            print(f, self.get_line_count(f))
            if "test" in os.path.basename(f).lower():
                self.lines_test += self.get_line_count(f)
            else:
                self.lines_code += self.get_line_count(f)
        print("Lines of test:", self.lines_test)
        print("Lines of code:", self.lines_code)

    def get_valid_files(self):
        valid_files = []
        for root, dirs, files in os.walk(self.project_name):
            valid_files += [
                os.path.join(root, f) for f in files
                if not f[0] == "." and f.endswith(self.valid_ext)
            ]
        return valid_files

