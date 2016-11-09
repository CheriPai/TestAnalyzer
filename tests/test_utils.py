from utils import *

class Test_Utils:
    def test_get_name_from_url_with_git(self):
        assert get_name_from_url("http://github.com/user/project.git") == "project"

    def test_get_name_from_url_without_git(self):
        assert get_name_from_url("http://github.com/user/project") == "project"
