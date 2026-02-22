import json

def resolve(data, query):
    cur = data
    i = 0
    n = len(query)

    while i < n:
        # skip dot between keys
        if query[i] == ".":
            i += 1
            continue

        # key: read letters/digits/_ until '.' or '['
        if query[i].isalpha() or query[i] == "_":
            j = i
            while j < n and (query[j].isalnum() or query[j] == "_"):
                j += 1
            key = query[i:j]

            if not isinstance(cur, dict) or key not in cur:
                return None, False
            cur = cur[key]
            i = j
            continue

        # index: [number]
        if query[i] == "[":
            i += 1
            if i >= n or not query[i].isdigit():
                return None, False

            num = 0
            while i < n and query[i].isdigit():
                num = num * 10 + (ord(query[i]) - ord("0"))
                i += 1

            if i >= n or query[i] != "]":
                return None, False
            i += 1  # skip ']'

            if not isinstance(cur, list) or num >= len(cur):
                return None, False
            cur = cur[num]
            continue

        # any other character => invalid query
        return None, False

    return cur, True


J = json.loads(input().strip())
q = int(input().strip())

for _ in range(q):
    path = input().strip()
    val, ok = resolve(J, path)
    if not ok:
        print("NOT_FOUND")
    else:
        print(json.dumps(val, ensure_ascii=False, separators=(",", ":"), sort_keys=True))
