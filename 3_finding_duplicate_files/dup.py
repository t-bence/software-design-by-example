import sys
from hashlib import sha256

def find_groups(filenames):
    groups = {}
    for fn in filenames:
        hash = sha256()
        for b in open(fn, "rb"):
            hash.update(b)
        hash_code = hash.hexdigest()
        if hash_code not in groups:
            groups[hash_code] = set()
        groups[hash_code].add(fn)
    return groups


if __name__ == "__main__":
    groups = find_groups(sys.argv[1:])
    for filenames in groups.values():
        print(", ".join(sorted(filenames)))
