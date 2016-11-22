from fileanalyzer import FileAnalyzer
from unittest import TestCase


class TestFileAnalyzer(TestCase):
    def setUp(self):
        self.analyzer = FileAnalyzer()

    def test_get_line_count(self):
        assert self.analyzer.get_line_count("this is a line") == 1

    def test_get_line_count(self):
        assert self.analyzer.get_line_count("this\nis two") == 2

