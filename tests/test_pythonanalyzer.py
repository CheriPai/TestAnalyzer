from pythonanalyzer import PythonAnalyzer
from unittest import TestCase


class TestPythonAnalyzer(TestCase):
    def setUp(self):
        self.analyzer = PythonAnalyzer()

    def test_get_class_count_basic(self):
        assert self.analyzer.get_class_count("class test:") == 1

    def test_get_class_count_inherit(self):
        assert self.analyzer.get_class_count("class test(object_1):") == 1

    def test_get_class_count_multiple(self):
        assert self.analyzer.get_class_count("""class test():
                                                    pass
                                                class test1(): 
                                                    pass
                                            """) == 2

    def test_get_class_count_none(self):
        assert self.analyzer.get_class_count("") == 0

    def test_get_function_count_basic(self):
        assert self.analyzer.get_function_count("def test():") == 1

    def test_get_function_count_arg(self):
        assert self.analyzer.get_function_count("def test(arg_1, arg_2):") == 1

    def test_get_function_count_multiple(self):
        assert self.analyzer.get_function_count("""def test():
                                                       pass
                                                   def test1():
                                                       pass
                                                """) == 2

    def test_get_function_count_none(self):
        assert self.analyzer.get_function_count("") == 0
