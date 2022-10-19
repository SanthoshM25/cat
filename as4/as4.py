class Territory:
    def __init__(self, name, neighbors, color=None):
        self.name = name
        self.neighbors = neighbors
        self.color = color

map = {"A1": Territory("A1", ["A2", "H"]),
    "A2": Territory("A2", ["A3", "H","A1"]),
    "A3": Territory("A3", ["A4", "H", "A2"]),
    "A4": Territory("A4", ["H", "A3"]),
    "H": Territory("H", ["T", "A1", "A2", "A3", "A4"]),
    "T": Territory("T", ["F1", "F2"]),
    "F1": Territory("F1", ["T"]),
    "F2": Territory("F2", ["T"])
}

def isConsistent(x, c):
    node=map[list(map.keys())[x]]
    for i in node.neighbors:
        r=list(map.keys()).index(i)
        if color[r] == c:
            return False
    return True

color=[0]*len(map)
domain = ["R","B","G"]

def solve(color,v):
    if len(map)==v:
        sol = {}
        idx = 0
        for i in map.keys():
            sol[i] = color[idx]
            idx += 1
        print(sol)
        return
    elif v>len(map):
        print("Not possible to solve")
        return
    for c in domain:
        if(isConsistent(v,c)):
            color[v] = c
            solve(color,v+1)
            color[v]=0

solve(color,0)

