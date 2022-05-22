from typing import Dict
import json as _json

def get_all_posts() -> Dict:

    with open('posts.json') as posts_file:
        data=_json.load(posts_file)

    return data

