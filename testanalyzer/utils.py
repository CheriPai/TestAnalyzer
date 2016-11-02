import os


def get_name_from_url(url):
    return os.path.basename(url).split(".")[0]
