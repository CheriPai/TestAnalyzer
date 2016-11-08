import pandas as pd
import shutil
import utils as u
import validators
from analyzer import Analyzer
from git import Repo

if __name__ == "__main__":

    repos = pd.read_pickle("data/test.pkl")

    for _, repo in repos.iterrows():
        if not validators.url(repo["url"]):
            print("Error: Invalid URL.")
            exit(1)

        project_name = u.get_name_from_url(repo["url"])
        print("Cloning {}...".format(project_name))
        Repo.clone_from(repo["url"], project_name)

        print("Analyzing...")
        analyzer = Analyzer(project_name)
        code_counts, test_counts = analyzer.run()
        print(code_counts)
        print(test_counts)

        shutil.rmtree(project_name)
