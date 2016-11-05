import os
from javaanalyzer import JavaAnalyzer
from pythonanalyzer import PythonAnalyzer


class Analyzer:

    valid_ext = (".py", ".java")

    def __init__(self, project_name):
        self.project_name = project_name
        self.valid_files = self.get_valid_files()
        self.file_analyzer = None
        self.test_counts = {
            "line_count": 0,
            "class_count": 0,
            "function_count": 0
            }
        self.code_counts = {
            "line_count": 0,
            "class_count": 0,
            "function_count": 0
            }

    def run(self):
        for f in self.valid_files:
            if ".py" in os.path.basename(f).lower():
                file_analyzer = PythonAnalyzer()
            elif ".java" in os.path.basename(f).lower():
                file_analyzer = JavaAnalyzer()
                pass
            else:
                raise Exception("Invalid file.")
                
            if "test" in os.path.basename(f).lower():
                for k, v in file_analyzer.analyze(f).items():
                    self.test_counts[k] += v
            else:
                for k, v in file_analyzer.analyze(f).items():
                    self.code_counts[k] += v

        print(self.test_counts)
        print(self.code_counts)

    def get_valid_files(self):
        valid_files = []
        for root, dirs, files in os.walk(self.project_name):
            valid_files += [
                os.path.join(root, f) for f in files
                if not f[0] == "." and f.endswith(self.valid_ext)
            ]
        return valid_files
