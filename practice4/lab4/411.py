import json

def patchjson(source, patch):
    for key in patch: #patch is dict
        patch_val = patch[key]

        if patch_val is None:
            if key in source:
                del source[key]
        
        elif key in source and isinstance(source[key], dict) and isinstance(patch_val, dict):
            patchjson(source[key], patch_val)

        else:
            source[key] = patch_val

    return source

source = json.loads(input().strip())
patch = json.loads(input().strip())

res = patchjson(source, patch)

print(json.dumps(res, sort_keys=True, separators=(",", ":")))