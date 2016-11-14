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

    shutil.rmtree(project_name)
    return jsonify(
        code_lines=code_counts["line_count"],
        code_classes=code_counts["class_count"],
        code_functions=code_counts["function_count"],
        test_lines=test_counts["line_count"],
        test_classes=test_counts["class_count"],
        test_functions=test_counts["function_count"])


if __name__ == "__main__":
    print("==> running server")
    app.run(debug=True, use_reloader=False)
