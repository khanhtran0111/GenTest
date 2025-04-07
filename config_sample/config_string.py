import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

problemName = "string"
totalOfTests = 10
subtasks = [100]
minN = 1
maxN = [1000]

def genInputContent(testID, curSubtask):
    length = random.randint(minN, maxN[curSubtask-1])
    s = genUltils.randomString(length, useSpace=False)
    return s