import json
import re

a = json.loads(input())
for user in a:
    userid = user["user_id"]
    handle = user["handle"]
    pattern = r"@[a-z]*_[a-z_]+"
    if re.fullmatch(pattern, handle):
        print(userid)