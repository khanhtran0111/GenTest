import sys
import os
import shutil
import traceback
import re


class TestGenApp:
    def __init__(self):
        """Initialize the command-line test generator"""
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        self.setup_project_structure()

    def setup_project_structure(self):
        """Create necessary directories if they don't exist"""
        for directory in ["problems", "solutions", "config_sample"]:
            dir_path = os.path.join(self.base_dir, directory)
            os.makedirs(dir_path, exist_ok=True)
        
        config_sample = os.path.join(self.base_dir, "config_sample.py")
        if not os.path.exists(config_sample):
            with open(config_sample, 'w', encoding='utf-8') as f:
                f.write("""# Sample configuration template
problemName = "bonghong"
numSamples = 5
numTests = 10
timeLimit = 1
memoryLimit = 512

def generate():
    # Your test generation logic here
    pass
""")

    def read_problem_names(self):
        """Read problem names from name.txt file"""
        name_file = os.path.join(self.base_dir, "name.txt")
        if not os.path.exists(name_file):
            print(f"Error: {name_file} not found!")
            return []
        
        try:
            with open(name_file, 'r', encoding='utf-8') as f:
                names = [line.strip() for line in f.readlines() if line.strip()]
            return names
        except Exception as e:
            print(f"Error reading {name_file}: {str(e)}")
            return []

    def create_problem(self, problem_name, create_cpp=True, create_python=True):
        """Create a problem with given name - equivalent to old create_problem function"""
        try:
            if not problem_name:
                print("Warning: Empty problem name, skipping...")
                return False
            
            problems_dir = os.path.join(self.base_dir, "problems")
            solutions_dir = os.path.join(self.base_dir, "solutions")
            os.makedirs(problems_dir, exist_ok=True)
            os.makedirs(solutions_dir, exist_ok=True)
            
            problem_dir = os.path.join(problems_dir, problem_name)
            if os.path.exists(problem_dir):
                print(f"Problem '{problem_name}' already exists. Overwriting...")
                    
            os.makedirs(problem_dir, exist_ok=True)
            
            # Create config.py file
            config_file = os.path.join(problem_dir, "config.py")
            config_content = f'''# Config for {problem_name}
problemName = "{problem_name}"  # Ensure this matches EXACTLY
numSamples = 5
numTests = 10
timeLimit = 1
memoryLimit = 512

def generate():
    # Your test generation logic here
    pass
'''
                
            with open(config_file, 'w', encoding='utf-8') as dst_file:
                dst_file.write(config_content)
            
            # Create solution files based on parameters
            if create_cpp:
                solution_file = os.path.join(solutions_dir, f"{problem_name}.cpp")
                with open(solution_file, 'w', encoding='utf-8') as f:
                    f.write(f'''// Solution for {problem_name}
#include <bits/stdc++.h>
using namespace std;

int main() {{
    // Your code here
    return 0;
}}
''')
            
            if create_python:
                solution_file = os.path.join(solutions_dir, f"{problem_name}.py")
                with open(solution_file, 'w', encoding='utf-8') as f:
                    f.write(f'''# Solution for {problem_name}

# Your code here
''')
            
            # Auto apply template (equivalent to use_selected_template)
            self.apply_template_to_config(config_file, problem_name)
            
            print(f"✓ Problem '{problem_name}' created successfully!")
            return True
            
        except Exception as e:
            print(f"✗ Failed to create problem '{problem_name}': {str(e)}")
            print("Error details:", traceback.format_exc())
            return False

    def apply_template_to_config(self, config_file_path, problem_name):
        """Apply config_sample.py template to the config file - equivalent to use_selected_template"""
        try:
            template_path = os.path.join(self.base_dir, "config_sample.py")
            
            if not os.path.exists(template_path):
                print(f"Warning: Template not found: {template_path}")
                return False
            
            # Read template content
            with open(template_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace problemName in template with actual problem name
            pattern = r'problemName\s*=\s*[\'"]([^\'"]*)[\'"]'
            content = re.sub(pattern, f'problemName = "{problem_name}"', content)
            
            # Write to config file
            with open(config_file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"  ✓ Template applied to {os.path.basename(config_file_path)}")
            return True
                    
        except Exception as e:
            print(f"  ✗ Failed to apply template: {str(e)}")
            return False

    def process_all_problems(self):
        """Main function to process all problems from name.txt"""
        print("=" * 60)
        print("GenTest - Automatic Test Generation Tool")
        print("=" * 60)
        
        # Read problem names
        problem_names = self.read_problem_names()
        if not problem_names:
            print("No problem names found in name.txt or file doesn't exist.")
            return
        
        print(f"Found {len(problem_names)} problems to create:")
        for i, name in enumerate(problem_names, 1):
            print(f"  {i}. {name}")
        
        print("\nCreating problems...")
        print("-" * 40)
        
        success_count = 0
        total_count = len(problem_names)
        
        for problem_name in problem_names:
            if self.create_problem(problem_name, create_cpp=True, create_python=True):
                success_count += 1
        
        print("-" * 40)
        print(f"Summary: {success_count}/{total_count} problems created successfully!")
        
        if success_count < total_count:
            print("Some problems failed to create. Check the error messages above.")
        else:
            print("All problems created successfully! 🎉")
        
        print("\nNext steps:")
        print("1. Edit the config.py files in each problem folder")
        print("2. Edit the solution files in the solutions folder")
        print("3. Run genTest.py to generate test cases")


def main():
    """Main entry point"""
    try:
        app = TestGenApp()
        app.process_all_problems()
    except Exception as e:
        print("CRITICAL ERROR:", str(e))
        print(traceback.format_exc())


if __name__ == "__main__":
    main() 