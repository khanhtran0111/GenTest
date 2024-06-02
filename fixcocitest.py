import os, sys
import shutil
import random
import subprocess

def getTestNameOut(fileName):
    pos = fileName.find('.in')
    return fileName[:pos]+'.out'+fileName[pos+3:]
def getTestDir(problemsDir, countingTest):
    testDir = problemsDir + "\\"+"Test"
    if countingTest < 10:
        testDir += "00"+str(countingTest)
    elif countingTest < 100:
        testDir += "0"+str(countingTest)
    else:
        testDir += str(countingTest)
    return testDir

rootFolderSrc = "C:\\ đường dẫn file"
rootFolderDest = "C:\\ đường dẫn file" #dòng này sẽ là path của file để lưu test fixed.
#Tao thu muc chua test sau khi sua
if not os.path.isdir(rootFolderDest) : os.mkdir(rootFolderDest)

currentDirectory = os.path.dirname(os.path.realpath(rootFolderSrc))
for path in os.listdir(rootFolderSrc):
    print("Subdirectory name:", os.path.basename(path))
    #print("Files in subdirectory:", ', '.join(files))
    problemsName = os.path.basename(path)
    problemsDirSrc = rootFolderSrc+"\\"+ problemsName
    problemsDirDest = rootFolderDest+"\\"+ problemsName
    #Tao thu muc chua test cua tung bai tap sau khi sua
    if not os.path.isdir(problemsDirDest) : os.mkdir(problemsDirDest)
    if(os.path.isdir(problemsDirSrc)):
        countingTest = 0
        for testNameInSrc in os.listdir(problemsDirSrc):
            if testNameInSrc.find('.in') != -1:
                testNameOutSrc = getTestNameOut(testNameInSrc)
                testPathInSrc = problemsDirSrc + "\\"+ testNameInSrc
                testPathOutSrc = problemsDirSrc + "\\"+ testNameOutSrc
                # if problemsName == "labirint":
                #     print(testPathInSrc, testPathOutSrc)
                if(os.path.isfile(testPathInSrc) and os.path.isfile(testPathOutSrc)):
                    countingTest+=1
                    testDirDest = getTestDir(problemsDirDest, countingTest)
                    #Tao thu muc chua cac test con sau khi sua
                    if not os.path.isdir(testDirDest) : os.mkdir(testDirDest)
                    #Copy, rename 2 file in out vao thu muc moi
                    testPathInDest = testDirDest + "\\" + problemsName + ".inp"
                    testPathOutDest = testDirDest + "\\" + problemsName + ".out"
                    try:
                        shutil.copyfile(testPathInSrc, testPathInDest)
                        shutil.copyfile(testPathOutSrc, testPathOutDest)
                    except:
                        print ("fail copy and rename test:  "+ testNameInSrc)
        print(problemsName + " co " + str(countingTest))