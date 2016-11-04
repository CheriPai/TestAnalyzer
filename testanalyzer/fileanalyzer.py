class FileAnalyzer():

    def analyze(self, filename):
        with open(filename) as f:
            content = f.read()
        line_count = self.get_line_count(content)
        class_count = self.get_class_count(content)
        function_count = self.get_function_count(content)
        return {
            "line_count": line_count,
            "class_count": class_count,
            "function_count": function_count
        }

    def get_line_count(self, content):
        return len(content.split("\n"))

    def get_class_count(self, content):
        pass

    def get_function_count(self, content):
        pass
