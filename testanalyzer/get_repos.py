import pandas as pd
from github import Github

languages = ["Python", "Java"]
data = []
g = Github()

for language in languages:
    repos = g.search_repositories(
        "", sort="stars", order="desc", language=language)
    for repo in repos:
        data.append({
            "url": repo.html_url,
            "language": language,
            "stargazers": repo.stargazers_count,
            "watchers": repo.watchers_count,
            "forks": repo.forks_count,
            "network": repo.network_count
        })


df = pd.DataFrame(data)
out_path = "data/repos.pkl"
print("Saving to {}...".format(out_path))
df.to_pickle(out_path)
