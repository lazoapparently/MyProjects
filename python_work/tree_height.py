#!/usr/bin/env python3
"""Get number of rows for the tree"""

tree_height = input("How tall is the tree?: ")

"""Convert to int"""

tree_height = int(tree_height)

"""Get Spaces"""

spaces = tree_height - 1

hashes = 1

stump_spaces = tree_height - 1

while tree_height != 0:
    for i in range(spaces):
        print(' ', end="")
	

    for i in range(hashes):
        print('#', end="")

    print()

    spaces -= 1

    hashes += 2

    tree_height -= 1

for i in range(stump_spaces):
    print(' ', end="")

print("#")
