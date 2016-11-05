import re
from fileanalyzer import FileAnalyzer


class JavaAnalyzer(FileAnalyzer):
    def get_class_count(self, content):
        return len(
            re.findall("[a-zA-Z ]*class +[a-zA-Z0-9_]+ *\n*\{", content))

    # TODO: Accept angle brackets and decline "else if"
    def get_function_count(self, content):
        return len(
            re.findall(
                "[a-zA-Z ]+ +[a-zA-Z0-9_]+ *\n*\([a-zA-Z0-9_,\[\] \n]*\)[a-zA-Z \n]*\{",
                content))
