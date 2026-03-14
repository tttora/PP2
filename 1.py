import json
import re

a = json.loads(input())

for user in a:
    email = user["email"]
    userid= user["user_id"]
    pattern = r"[a-z]+@[a-z]+\.com"
    if re.fullmatch(pattern, email):
        print(userid)
