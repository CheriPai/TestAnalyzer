import re
from fileanalyzer import FileAnalyzer


class PythonAnalyzer(FileAnalyzer):

    def analyze(self, filename):
        with open(filename) as f:
            content = f.read()
        line_count = self.get_line_count(content)
        class_count = self.get_class_count(content)
        function_count = self.get_function_count(content)
        print(line_count, class_count, function_count)

    def get_class_count(self, content):
        return len(re.findall("class [a-zA-Z0-9_]+\(?[a-zA-Z0-9_, ]*\)?:", content))
            
    def get_function_count(self, content):
        return len(re.findall("def [a-zA-Z0-9_]+\([a-zA-Z0-9_, ]*\):", content))
