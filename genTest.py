import os
import subprocess
import shutil
import importlib.util

############ CODE SINH TEST ############

def createTestFolder(rootFolder, problemName):
    problemFolder = os.path.join(rootFolder, problemName)
    os.makedirs(problemFolder, exist_ok=True)

def genInput(rootFolder, problemName, totalOfTests, subtasks, config):
    problemFolder = os.path.join(rootFolder, problemName)
    curSubtask = 1

    for i in range(1, totalOfTests + 1):
        test_folder = os.path.join(problemFolder, f"Test{i:03d}")
        os.makedirs(test_folder, exist_ok=True)

        input_file = os.path.join(test_folder, f"{problemName}.inp")
        if curSubtask < len(subtasks) and i > totalOfTests * sum(subtasks[:curSubtask]) // 100:
            curSubtask += 1

        with open(input_file, "w") as f:
            f.write(config.genInputContent(i, curSubtask))

        print(f"Generated Input for Test{i:03d} - Subtask{curSubtask}")

def genOutput(rootFolder, solutionsFolder, problemName, totalOfTests):
    problemFolder = os.path.join(rootFolder, problemName)

    py_solution = os.path.join(solutionsFolder, f"{problemName}.py")
    cpp_solution = os.path.join(solutionsFolder, f"{problemName}.cpp")

    if os.path.exists(py_solution):
        for i in range(1, totalOfTests + 1):
            test_folder = os.path.join(problemFolder, f"Test{i:03d}")
            input_file = os.path.join(test_folder, f"{problemName}.inp")
            output_file = os.path.join(test_folder, f"{problemName}.out")

            with open(input_file, "r") as fin, open(output_file, "w") as fout:
                subprocess.run(["python", py_solution], stdin=fin, stdout=fout)

            print(f"Generated Output for Test{i:03d} (Python)")

    elif os.path.exists(cpp_solution):
        compiled_exe = os.path.join(solutionsFolder, problemName)
        subprocess.run(["g++", cpp_solution, "-o", compiled_exe], check=True)

        for i in range(1, totalOfTests + 1):
            test_folder = os.path.join(problemFolder, f"Test{i:03d}")
            input_file = os.path.join(test_folder, f"{problemName}.inp")
            output_file = os.path.join(test_folder, f"{problemName}.out")

            with open(input_file, "r") as fin, open(output_file, "w") as fout:
                subprocess.run(compiled_exe, stdin=fin, stdout=fout)

            print(f"Generated Output for Test{i:03d} (C++)")

    else:
        print(f"No solution file (.py or .cpp) found for problem '{problemName}' in solutions folder.")
        return

    shutil.make_archive(problemFolder, 'zip', problemFolder)

##### MAIN #####

def load_module_from_path(module_name, module_path):
    spec = importlib.util.spec_from_file_location(module_name, module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def process_problem(problemsFolder, solutionsFolder, problemFolder):
    config_path = os.path.join(problemFolder, "config.py")

    if not os.path.exists(config_path):
        print(f"Skipped {problemFolder}: config.py not found.")
        return

    config = load_module_from_path("config", config_path)

    problemName = getattr(config, "problemName", None)
    totalOfTests = getattr(config, "totalOfTests", None)
    subtasks = getattr(config, "subtasks", None)

    if not problemName or totalOfTests is None or not subtasks:
        print(f"Skipped {problemFolder}: Missing parameters in config.py.")
        return

    if not hasattr(config, "genInputContent"):
        print(f"No genInputContent function found in {problemFolder}")
        return

    print(f"Processing {problemName}: {totalOfTests} tests, subtasks {subtasks}")

    createTestFolder(problemFolder, problemName)
    genInput(problemFolder, problemName, totalOfTests, subtasks, config)
    genOutput(problemFolder, solutionsFolder, problemName, totalOfTests)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROBLEMS_DIR = os.path.join(BASE_DIR, "problems")
SOLUTIONS_DIR = os.path.join(BASE_DIR, "solutions")

for problem in os.listdir(PROBLEMS_DIR):
    problemFolder = os.path.join(PROBLEMS_DIR, problem)
    if os.path.isdir(problemFolder):
        process_problem(PROBLEMS_DIR, SOLUTIONS_DIR, problemFolder)
