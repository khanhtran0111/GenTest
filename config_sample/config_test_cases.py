import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

problemName = "test_cases"
totalOfTests = 10
subtasks = [100]
minN = 1
maxN = [1000]

def genInputContent(testID, curSubtask):
    t = random.randint(1, 10)
    inpContent = [t]
    for _ in range(t):
        n = random.randint(minN, maxN[curSubtask-1])
        m = random.randint(minN, maxN[curSubtask-1])
        arr = genUltils.randomIntList(n, 1, 10**6)
        inpContent.append([f"{n} {m}", arr])
    return genUltils.toStringLinesAll(inpContent)