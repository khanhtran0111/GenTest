import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

problemName = "undirected_graph"
totalOfTests = 10
subtasks = [100]
minN = 2
maxN = [1000]

def genInputContent(testID, curSubtask):
    n = random.randint(minN, maxN[curSubtask-1])
    m = min(random.randint(n-1, n*(n-1)//2), maxN[curSubtask-1])
    edges = set()
    while len(edges) < m:
        u, v = sorted(random.sample(range(1, n+1), 2))
        edges.add((u, v))
    return genUltils.toStringLines([f"{n} {m}", list(edges)])