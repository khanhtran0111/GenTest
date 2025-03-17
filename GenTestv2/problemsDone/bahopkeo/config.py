import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

############## THAY THẾ CÁC THAM SỐ SAU ##############

problemName = "bahopkeo"
totalOfTests = 20
subtasks = [50, 50]  # Subtask 1: 50%, Subtask 2: 50%.
minN = 1
maxN = [1000, 1000000]
######################################################

############# SỬA HÀM ĐỂ SINH FILE INPUT #############

def genInputContent(testID, curSubtask):
    low = minN if curSubtask == 1 else maxN[curSubtask-2]
    up = maxN[curSubtask-1] 
    
    #TODO: Viết lệnh random các tham số của Input ở đây 
    inpContent = []
    while True:
        try:
            a = random.randint(low, up)
            b = random.randint(low, up)
            n = random.randint(2*a+b+1, up)
            if (3*n-2*a-b>0):
                inpContent.extend([n, a, b])
                break
        except ValueError:
            continue
    return genUltils.toStringLines(inpContent)

######################################################