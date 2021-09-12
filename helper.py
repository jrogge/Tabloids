import itertools as it

letters = [0,1,2,3]
for perm in it.permutations(letters, 4):
    print("tabs.append(Tabloid( [1,1,1,1], [[%d], [%d], [%d], [%d]]))"%(perm[0],
        perm[1], perm[2], perm[3]))
