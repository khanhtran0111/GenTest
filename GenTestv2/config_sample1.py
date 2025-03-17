"""
 CONFIG CHO TEST CHỈ CHỨA 1 SỐ NGUYÊN
"""
import random
import sys
import os
sys.path.append(os.path.abspath(os.path.join(__file__, "../../..")))
import genUltils  

############## THAY THẾ CÁC THAM SỐ SAU ##############

problemName = "BAI1"
totalOfTests = 20
subtasks = [10, 40, 50]  # Subtask 1: 10%, Subtask 2: 40%, Subtask 3: 50%.

#minN >=0 nếu số đó là không âm/nguyên dương
#minN < 0 sẽ lấy khoảng trị tuyệt đối của maxN cho mỗi subtask
minN = 1
maxN = [20, 10**5, 10**9]
######################################################

############# SỬA HÀM ĐỂ SINH FILE INPUT #############
############# XEM genUltils DE LAY CAC HAM RANDOM #############

def genInputContent(testID, curSubtask):
    low = - maxN[curSubtask-1]
    if minN >= 0:
        low = minN if curSubtask == 1 else maxN[curSubtask-2]
    up = maxN[curSubtask-1] 
    
    #TODO: Viết lệnh random các tham số của Input ở đây 
    inpContent = []
    n = random.randint(low, up)
    inpContent.extend([n])
    return genUltils.toStringLines(inpContent)

######################################################