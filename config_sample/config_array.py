import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

problemName = "array"
totalOfTests = 10
subtasks = [100]
minN = 1
maxN = [100000]

def genInputContent(testID, curSubtask):
    n = random.randint(minN, maxN[curSubtask-1])
    arr = genUltils.randomIntList(n, 1, 10**6)
    return genUltils.toStringLines([n, arr])