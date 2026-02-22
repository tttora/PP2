import json

def tojson(v):
    return json.dumps(v, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
def diff(a, b, path, out):
    if isinstance(a, dict) and isinstance(b, dict):
        keys = set(a.keys()) | set(b.keys())
        for k in keys:
            new_path = k if path == "" else path + "." + k
            if k not in a:
                out.append((new_path, "<missing>", tojson(b[k])))
            elif k not in b:
                out.append((new_path, tojson(a[k]), "<missing>"))
            else:
                diff(a[k], b[k], new_path, out)
        return
    if a != b:
        out.append((path, tojson(a), tojson(b)))

A = json.loads(input().strip())
B = json.loads(input().strip())

changes = []
diff(A, B, "", changes)

if not changes:
    print("No differences")
else:
    changes.sort(key = lambda x: x[0])
    for p, oldv, newv in changes:
        print(f"{p} : {oldv} -> {newv}")