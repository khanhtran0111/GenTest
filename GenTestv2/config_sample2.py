"""
 CONFIG CHO TEST:
- Dòng 1 chứa số nguyên N
- Dòng 2 chứa số N số nguyên A[i]
"""
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

############## THAY THẾ CÁC THAM SỐ SAU ##############

problemName = "bahopkeo"
totalOfTests = 20
subtasks = [10, 40, 50]  # Subtask 1: 10%, Subtask 2: 40%, Subtask 3: 50%.

#minN >=0 nếu số đó là không âm/nguyên dương
#nminN < 0 sẽ lấy khoảng trị tuyệt đối của maxN cho mỗi subtask
minN = 1
maxN = [10, 1000, 10**5]

#minA >= 0 nếu số đó là không âm/nguyên dương
#minA < 0 sẽ lấy khoảng trị tuyệt đối của maxA cho mỗi subtask
minA = -1
maxA = [100, 10**5, 10**9]

######################################################

############# SỬA HÀM ĐỂ SINH FILE INPUT #############
############# XEM genUltils DE LAY CAC HAM RANDOM #############

def genInputContent(testID, curSubtask):
    lowN = - maxN[curSubtask-1]
    if minN >= 0:
        lowN = minN if curSubtask == 1 else maxN[curSubtask-2]
    upN = maxN[curSubtask-1]  

    lowA = - maxA[curSubtask-1]
    if minA >= 0:
        lowA = minA if curSubtask == 1 else maxA[curSubtask-2]
    upA = maxA[curSubtask-1] 
    
    #TODO: Viết lệnh random các tham số của Input ở đây 
    inpContent = []
    n = random.randint(lowN, upN)
    lst = genUltils.randomIntList(n, lowA, upA)
    inpContent.extend([n, lst])
    return genUltils.toStringLines(inpContent)

######################################################