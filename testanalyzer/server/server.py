import shutil
import utils as u
import validators
from analyzer import Analyzer
from flask import Flask, jsonify, render_template, request
from git import Repo


app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/analyze")
def analyze():
    project_url = request.args["URL"]

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
    return None

if __name__ == "__main__":
    print("==> running server")
    app.run(debug=True, use_reloader=False)
