import json
import re

a = json.loads(input())
for post in a:
    postid = post["post_id"]
    tag = post["tag"]
    pattern = r"\#[a-z]+"
    if re.fullmatch(pattern, tag):
        print(postid)