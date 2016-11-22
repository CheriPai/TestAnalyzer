import re
from fileanalyzer import FileAnalyzer


class PythonAnalyzer(FileAnalyzer):
    def get_class_count(self, content):
        matches = re.findall("\"*class +[a-zA-Z0-9_]+ *\(?[a-zA-Z0-9_, ]*\)? *:\"*", content)
        matches = [m for m in matches if m.strip()[0] != "\"" and m.strip()[-1] != "\""]
        return len(matches)

    def get_function_count(self, content):
        matches = re.findall("\"*def +[a-zA-Z0-9_]+ *\([a-zA-Z0-9_, ]*\) *:\"*", content)
        matches = [m for m in matches if m.strip()[0] != "\"" and m.strip()[-1] != "\""]
        return len(matches)
