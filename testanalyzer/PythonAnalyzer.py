from testanalyzer.Analyzer import Analyzer


class PythonAnalyzer(Analyzer):

    def __init__(self, filename):
        self.filename = filename
        self.lines_test = 0
        self.lines_code = 0
        self.classes_test = 0
        self.classes_code = 0
        self.functions_test = 0
        self.functions_code = 0

    def get_classes_count():
        pass
