from Tabloid import Tabloid

tabs = []
# (3)
tab = Tabloid([3], [[0,1,2]])
tabs.append(tab)

# (2,1)
tabs.append(Tabloid([2,1], [[0,1],[2]]))
tabs.append(Tabloid([2,1], [[0,2],[1]]))
tabs.append(Tabloid([2,1], [[1,2],[0]]))

# (1,1,1)
tabs.append(Tabloid([1,1,1], [[0],[1],[2]]))
tabs.append(Tabloid([1,1,1], [[0],[2],[1]]))
tabs.append(Tabloid([1,1,1], [[1],[0],[2]]))
tabs.append(Tabloid([1,1,1], [[1],[2],[0]]))
tabs.append(Tabloid([1,1,1], [[2],[0],[1]]))
tabs.append(Tabloid([1,1,1], [[2],[1],[0]]))
