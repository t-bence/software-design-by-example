import sys
from hashlib import sha256
import matplotlib.pyplot as plt

def find_groups(filename):
    return [
        int(sha256(row.encode()).hexdigest(), 16) % 1_000_000
        for row in open(filename, "r")
        if row.strip()
    ]

numbers = find_groups(sys.argv[1])
plt.hist(numbers, bins=20)
plt.show()
