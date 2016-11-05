import re
from fileanalyzer import FileAnalyzer


class PythonAnalyzer(FileAnalyzer):

    def get_class_count(self, content):
        return len(
            re.findall("class +[a-zA-Z0-9_]+ *\(?[a-zA-Z0-9_, ]*\)? *:", content))

    def get_function_count(self, content):
        return len(
            re.findall("def +[a-zA-Z0-9_]+ *\([a-zA-Z0-9_, ]*\) *:", content))
