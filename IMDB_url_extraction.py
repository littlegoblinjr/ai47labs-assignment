import re

def extract_imdb_id(url):

    imdb_pattern = r"(tt\d+)"
    match = re.search(imdb_pattern, url)
    if match:
        return match.group(1)
    else:
        return None


    