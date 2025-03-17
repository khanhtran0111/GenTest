import os
import subprocess
import shutil
import importlib.util
import stat


############ CODE SINH TEST ############

def createTestFolder(rootFolder, problemName):
    # ✅ Tạo thư mục chứa test case
    problemFolder = os.path.join(rootFolder, problemName)
    os.makedirs(problemFolder, exist_ok=True)

def genInput(rootFolder, problemName, totalOfTests, subtasks, config):
    problemFolder = os.path.join(rootFolder, problemName)

    # Subtask của Test hiện tại
    curSubtask = 1
    # ✅ Tạo thư mục con Test001, Test002,... và file input/output
    for i in range(1, totalOfTests + 1):
        test_folder = os.path.join(problemFolder, f"Test{i:03d}")
        os.makedirs(test_folder, exist_ok=True)

        input_file = os.path.join(test_folder, f"{problemName}.inp")
        # ✅ Sinh input mẫu (tuỳ chỉnh theo bài toán)
        if (curSubtask<len(subtasks) and i > totalOfTests*sum(subtasks[:curSubtask])//100): curSubtask += 1
        
        with open(input_file, "w") as f:
            f.write(config.genInputContent(i, curSubtask))

        print(f"Generate Input for Test{i:03d} - Subtask{curSubtask}: DONE")

def genOutputCPP(rootFolder, problemName, totalOfTests):
    problemFolder = os.path.join(rootFolder, problemName)

    # ✅ Biên dịch chương trình C++
    cpp_source = os.path.join(rootFolder, f"{problemName}.cpp")
    compiled_exe = os.path.join(rootFolder, problemName)
    subprocess.run(["g++", cpp_source, "-o", compiled_exe], check=True)

    # ✅ Chạy chương trình với từng test case và ghi output
    for i in range(1, totalOfTests + 1):
        test_folder = os.path.join(problemFolder, f"Test{i:03d}")
        input_file = os.path.join(test_folder, f"{problemName}.inp")
        output_file = os.path.join(test_folder, f"{problemName}.out")

        with open(input_file, "r") as fin, open(output_file, "w") as fout:
            subprocess.run(f'"{compiled_exe}"',shell=True, stdin=fin, stdout=fout)

        print(f"Generate Output for Test{i:03d}: DONE")

    # Nén lại thư mục thành file zip
    shutil.make_archive(problemFolder, 'zip', problemFolder)

def genOutputPY(rootFolder, problemName, totalOfTests):
    problemFolder = os.path.join(rootFolder, problemName)

    # ✅ Chạy chương trình Python với từng test case và ghi output
    for i in range(1, totalOfTests + 1):
        test_folder = os.path.join(problemFolder, f"Test{i:03d}")
        input_file = os.path.join(test_folder, f"{problemName}.inp")
        output_file = os.path.join(test_folder, f"{problemName}.out")

        with open(input_file, "r") as fin, open(output_file, "w") as fout:
            subprocess.run(["python", os.path.join(rootFolder, f"{problemName}.py")], stdin=fin, stdout=fout)

        print(f"Generate Output for Test{i:03d}: DONE")

    # ✅ Nén lại thư mục thành file zip
    shutil.make_archive(problemFolder, 'zip', problemFolder)

##### MAIN #####
def load_module_from_path(module_name, module_path):
    """Tải module Python từ đường dẫn file cụ thể."""
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def process_problem(problemFolder):

    """Xử lý từng bài toán trong thư mục `problems/`."""
    config_path = os.path.join(problemFolder, "config.py")

    if not os.path.exists(config_path):
        print(f"⚠️  Bỏ qua {problemFolder}: Không tìm thấy config.py")
        return

    # 🔹 Tải config.py
    config = load_module_from_path("config", config_path)

    # 🔹 Trích xuất biến
    problemName = getattr(config, "problemName", None)
    totalOfTests = getattr(config, "totalOfTests", None)
    subtasks = getattr(config, "subtasks", None)

    if not problemName or totalOfTests is None or not subtasks:
        print(f"⚠️  Bỏ qua {problemFolder}: Thiếu biến trong config.py")
        return

    if not hasattr(config, "genInputContent"):
        print(f"⚠️  Không tìm thấy hàm genInputContent trong {problemFolder}")
        return
    
    # 🔹 Kiểm tra file code
    pythonFile = os.path.join(problemFolder, f"{problemName}.py")
    cppFile = os.path.join(problemFolder, f"{problemName}.cpp")

    if not(os.path.exists(pythonFile) or os.path.exists(cppFile)):
        print(f"⚠️ Không tìm thấy file code {problemName}.py hoặc {problemName}.cpp trong thư mục {problemFolder}" )
        return

    print(f"🔹 Đang xử lý {problemName}: {totalOfTests} tests, subtasks {subtasks}")

    createTestFolder(problemFolder, problemName)
    genInput(problemFolder, problemName, totalOfTests, subtasks, config)
    if os.path.exists(pythonFile):
        genOutputPY(problemFolder, problemName, totalOfTests)
    else:
        genOutputCPP(problemFolder, problemName, totalOfTests)



BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Lấy thư mục chứa file genTest.py hiện tại
PROBLEMS_DIR = os.path.join(BASE_DIR, "problems") 

for problem in os.listdir(PROBLEMS_DIR):
        problemFolder = os.path.join(PROBLEMS_DIR, problem)
        if os.path.isdir(problemFolder):
            print(problemFolder)
            process_problem(problemFolder)