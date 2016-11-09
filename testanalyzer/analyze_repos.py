import pandas as pd
import shutil
import utils as u
import validators
from analyzer import Analyzer
from git import Repo

if __name__ == "__main__":

    repos = pd.read_pickle("data/repos.pkl")
    repos["code_lines"] = 0
    repos["code_classes"] = 0
    repos["code_functions"] = 0
    repos["test_lines"] = 0
    repos["test_classes"] = 0
    repos["test_functions"] = 0

    for i, repo in repos.iterrows():
        if not validators.url(repo["url"]):
            print("Error: Invalid URL.")
            exit(1)

        project_name = u.get_name_from_url(repo["url"])
        print("Cloning {}...".format(project_name))
        Repo.clone_from(repo["url"], project_name)

        print("Analyzing...")
        analyzer = Analyzer(project_name)
        code_counts, test_counts = analyzer.run()
        repos.set_value(i, "code_lines", code_counts["line_count"])
        repos.set_value(i, "code_classes", code_counts["class_count"])
        repos.set_value(i, "code_functions", code_counts["function_count"])
        repos.set_value(i, "test_lines", test_counts["line_count"])
        repos.set_value(i, "test_classes", test_counts["class_count"])
        repos.set_value(i, "test_functions", test_counts["function_count"])

        shutil.rmtree(project_name)

    repos.to_pickle("data/dataset.pkl")
