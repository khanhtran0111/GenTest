import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

############## THAY THẾ CÁC THAM SỐ SAU ##############

problemName = "pnmonth1"
totalOfTests = 20
subtasks = [12]  # Subtask 1: 50%, Subtask 2: 50%.
minN = 1
maxN = [12]
######################################################

############# SỬA HÀM ĐỂ SINH FILE INPUT #############
############# XEM genUltils DE LAY CAC HAM RANDOM #############

def genInputContent(testID, curSubtask):
    low = minN if curSubtask == 1 else maxN[curSubtask-2]
    up = maxN[curSubtask-1] 
    
    #TODO: Viết lệnh random các tham số của Input ở đây 
    inpContent = []
    d = random.randint(low, up)
    inpContent.extend([d])
    return genUltils.toStringLines(inpContent)

######################################################