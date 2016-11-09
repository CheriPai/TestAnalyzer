from javaanalyzer import JavaAnalyzer
from unittest import TestCase


class TestPythonAnalyzer(TestCase):
    def setUp(self):
        self.analyzer = JavaAnalyzer()

    def test_get_class_count_basic(self):
        assert self.analyzer.get_class_count("public class test {") == 1

    def test_get_class_count_inherit(self):
        assert self.analyzer.get_class_count("public class test extends test {") == 1

    def test_get_class_count_multiple(self):
        assert self.analyzer.get_class_count("""private static class test {
                                                    pass
                                                public class test1{ 
                                                    pass
                                            """) == 2

    def test_get_class_count_none(self):
        assert self.analyzer.get_class_count("") == 0

    def test_get_function_count_basic(self):
        assert self.analyzer.get_function_count("public int test() {") == 1

    def test_get_function_count_arg(self):
        assert self.analyzer.get_function_count("public static void main test(String[] args){") == 1

    def test_get_function_count_multiple(self):
        assert self.analyzer.get_function_count("""private generic<a, b> test() 
                                                   { }
                                                   public int test1(test_1, test_2){}
                                                """) == 2

    def test_get_function_count_none(self):
        assert self.analyzer.get_function_count("") == 0
