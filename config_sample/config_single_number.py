import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

problemName = "single_number"
totalOfTests = 10
subtasks = [100]
minN = 1
maxN = [1000000]

def genInputContent(testID, curSubtask):
    num = random.randint(minN, maxN[curSubtask-1])
    return str(num)