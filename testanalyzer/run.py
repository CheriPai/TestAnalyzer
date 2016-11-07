import shutil
import validators
import utils as u
from analyzer import Analyzer
from git import Repo

if __name__ == "__main__":

    project_url = input("Input URL to github project: ")

    if not validators.url(project_url):
        print("Error: Invalid URL.")
        exit(1)

    project_name = u.get_name_from_url(project_url)
    print("Cloning {}...".format(project_name))
    Repo.clone_from(project_url, project_name)

    print("Analyzing...")
    analyzer = Analyzer(project_name)
    code_counts, test_counts = analyzer.run()
    print(code_counts)
    print(test_counts)

    shutil.rmtree(project_name)
