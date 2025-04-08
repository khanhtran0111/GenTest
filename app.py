import sys
import os
import shutil
import zipfile
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                            QLabel, QLineEdit, QCheckBox, QPushButton, QFileDialog,
                            QTabWidget, QSplitter, QTreeView, QMessageBox, QComboBox)
from PyQt5.QtCore import Qt, QDir, QModelIndex
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5.Qsci import QsciScintilla, QsciLexerPython, QsciLexerCPP
import importlib.util
import subprocess
import traceback

class TestGenApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GenTest - Test Generation Tool")
        self.setGeometry(50, 50, 1200, 800)
        main_layout = QHBoxLayout()
        self.sidebar = self.create_sidebar()
        main_layout.addWidget(self.sidebar, 1)
        self.editor_area = self.create_editor_area()
        main_layout.addWidget(self.editor_area, 4)
        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setup_project_structure()
        self.update_file_tree()

    def setup_project_structure(self):
        """Create necessary directories if they don't exist"""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        for directory in ["problems", "solutions", "config_sample"]:
            dir_path = os.path.join(base_dir, directory)
            os.makedirs(dir_path, exist_ok=True)
        config_sample = os.path.join(base_dir, "config_sample.py")
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

    def create_sidebar(self):
        sidebar = QWidget()
        sidebar_layout = QVBoxLayout(sidebar)
        problem_section = QWidget()
        problem_layout = QVBoxLayout(problem_section)
        
        problem_layout.addWidget(QLabel("Problem Name:"))
        self.problem_name_input = QLineEdit()
        problem_layout.addWidget(self.problem_name_input)
        
        language_layout = QHBoxLayout()
        self.cpp_checkbox = QCheckBox("C++")
        self.py_checkbox = QCheckBox("Python")
        self.cpp_checkbox.setChecked(True)
        language_layout.addWidget(self.cpp_checkbox)
        language_layout.addWidget(self.py_checkbox)
        problem_layout.addLayout(language_layout)
        
        self.create_problem_btn = QPushButton("Create Problem")
        self.create_problem_btn.clicked.connect(self.create_problem)
        problem_layout.addWidget(self.create_problem_btn)
        
        sidebar_layout.addWidget(problem_section)
        config_section = QWidget()
        config_layout = QVBoxLayout(config_section)
        config_layout.addWidget(QLabel("Config Template:"))
        
        self.template_combo = QComboBox()
        self.update_template_list()
        config_layout.addWidget(self.template_combo)
        
        self.use_template_btn = QPushButton("Use Template")
        self.use_template_btn.clicked.connect(self.use_selected_template)
        config_layout.addWidget(self.use_template_btn)
        
        sidebar_layout.addWidget(config_section)
        self.file_tree = QTreeView()
        self.file_model = QStandardItemModel()
        self.file_tree.setModel(self.file_model)
        self.file_tree.setHeaderHidden(True)
        self.file_tree.clicked.connect(self.file_clicked)
        
        sidebar_layout.addWidget(QLabel("Project Files:"))
        sidebar_layout.addWidget(self.file_tree)
        action_section = QWidget()
        action_layout = QVBoxLayout(action_section)
        self.gen_test_btn = QPushButton("Generate Tests")
        self.gen_test_btn.clicked.connect(self.generate_tests)
        action_layout.addWidget(self.gen_test_btn)
        self.export_btn = QPushButton("Export Tests as ZIP")
        self.export_btn.clicked.connect(self.export_tests)
        action_layout.addWidget(self.export_btn)
        self.clear_btn = QPushButton("Clear All Problems/Solutions")
        self.clear_btn.setStyleSheet("background-color: #ffdddd;")
        self.clear_btn.clicked.connect(self.clear_all)
        action_layout.addWidget(self.clear_btn)
        
        sidebar_layout.addWidget(action_section)
        
        return sidebar

    def create_editor_area(self):
        editor_widget = QWidget()
        editor_layout = QVBoxLayout(editor_widget)
        
        # Tabs for open files
        self.tab_widget = QTabWidget()
        self.tab_widget.setTabsClosable(True)
        self.tab_widget.tabCloseRequested.connect(self.close_tab)
        
        editor_layout.addWidget(self.tab_widget)
        
        return editor_widget

    def create_editor(self, file_path):
        editor = QsciScintilla()
        
        # Set up editor properties
        editor.setUtf8(True)
        editor.setMarginType(0, QsciScintilla.NumberMargin)
        editor.setMarginWidth(0, "0000")
        editor.setMarginsForegroundColor(Qt.darkGray)
        
        # Set font
        font = QFont("Consolas", 10)
        editor.setFont(font)
        
        # Set lexer based on file extension
        if file_path.endswith('.py'):
            lexer = QsciLexerPython()
            lexer.setFont(font)
            editor.setLexer(lexer)
        elif file_path.endswith('.cpp'):
            lexer = QsciLexerCPP()
            lexer.setFont(font)
            editor.setLexer(lexer)
        
        # Enable auto-indentation
        editor.setAutoIndent(True)
        editor.setIndentationWidth(4)
        
        # Load file content
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                editor.setText(f.read())
        except Exception as e:
            print(f"Error loading file: {e}")
        
        editor.setProperty("file_path", file_path)
        return editor

    def update_file_tree(self):
        self.file_model.clear()
        self.file_model.setHorizontalHeaderLabels(["Project Files"])
        
        base_dir = os.path.dirname(os.path.abspath(__file__))
        root = self.file_model.invisibleRootItem()
        
        # Add problems folder
        problems_dir = os.path.join(base_dir, "problems")
        problems_item = QStandardItem("problems")
        problems_item.setData(problems_dir, Qt.UserRole)
        self.add_directory_items(problems_item, problems_dir)
        root.appendRow(problems_item)
        
        # Add solutions folder
        solutions_dir = os.path.join(base_dir, "solutions")
        solutions_item = QStandardItem("solutions")
        solutions_item.setData(solutions_dir, Qt.UserRole)
        self.add_directory_items(solutions_item, solutions_dir)
        root.appendRow(solutions_item)
        
        # Add config_samples folder
        config_dir = os.path.join(base_dir, "config_sample")
        config_item = QStandardItem("config_sample")
        config_item.setData(config_dir, Qt.UserRole)
        self.add_directory_items(config_item, config_dir)
        root.appendRow(config_item)
        
        self.file_tree.expandAll()

    def add_directory_items(self, parent_item, directory):
        if not os.path.exists(directory):
            return
            
        for item in sorted(os.listdir(directory)):
            path = os.path.join(directory, item)
            child = QStandardItem(item)
            child.setData(path, Qt.UserRole)
            parent_item.appendRow(child)
            
            if os.path.isdir(path):
                self.add_directory_items(child, path)

    def update_template_list(self):
        self.template_combo.clear()
        base_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Add the default template first
        self.template_combo.addItem("config_sample.py")
        
        # Add templates from config_sample directory
        config_dir = os.path.join(base_dir, "config_sample")
        if os.path.exists(config_dir):
            for file in sorted(os.listdir(config_dir)):
                if file.endswith('.py'):
                    self.template_combo.addItem(file)

    def file_clicked(self, index):
        item = self.file_model.itemFromIndex(index)
        if item:
            file_path = item.data(Qt.UserRole)
            if file_path and os.path.isfile(file_path):
                self.open_file(file_path)
            elif file_path and os.path.isdir(file_path):
                # It's a directory, we might want to expand/collapse it
                pass

    def open_file(self, file_path):
        if not os.path.exists(file_path):
            QMessageBox.warning(self, "File Not Found", f"Cannot find file: {file_path}")
            return
            
        # Check if file is already open
        for i in range(self.tab_widget.count()):
            editor = self.tab_widget.widget(i)
            if editor.property("file_path") == file_path:
                self.tab_widget.setCurrentIndex(i)
                return
        
        # Create new editor and tab
        editor = self.create_editor(file_path)
        file_name = os.path.basename(file_path)
        index = self.tab_widget.addTab(editor, file_name)
        self.tab_widget.setCurrentIndex(index)

    def close_tab(self, index):
        editor = self.tab_widget.widget(index)
        file_path = editor.property("file_path")
        
        # Ask to save changes if modified
        if editor.isModified():
            response = QMessageBox.question(self, "Save Changes?", 
                f"Save changes to {os.path.basename(file_path)}?",
                QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
            
            if response == QMessageBox.Save:
                self.save_file(editor, file_path)
            elif response == QMessageBox.Cancel:
                return
        
        self.tab_widget.removeTab(index)

    def save_file(self, editor, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(editor.text())
            editor.setModified(False)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Could not save file: {str(e)}")

    def save_current_file(self):
        index = self.tab_widget.currentIndex()
        if index >= 0:
            editor = self.tab_widget.widget(index)
            file_path = editor.property("file_path")
            self.save_file(editor, file_path)

    def create_problem(self):
        try:
            problem_name = self.problem_name_input.text().strip()
            if not problem_name:
                QMessageBox.warning(self, "Warning", "Please enter a problem name.")
                return
            
            base_dir = os.path.dirname(os.path.abspath(__file__))
            problems_dir = os.path.join(base_dir, "problems")
            solutions_dir = os.path.join(base_dir, "solutions")
            
            # Ensure directories exist
            os.makedirs(problems_dir, exist_ok=True)
            os.makedirs(solutions_dir, exist_ok=True)
            
            # Create problem folder
            problem_dir = os.path.join(problems_dir, problem_name)
            if os.path.exists(problem_dir):
                response = QMessageBox.question(self, "Problem exists", 
                    f"Problem '{problem_name}' already exists. Overwrite?",
                    QMessageBox.Yes | QMessageBox.No)
                if response == QMessageBox.No:
                    return
                    
            os.makedirs(problem_dir, exist_ok=True)
            
            # Create config.py file
            config_file = os.path.join(problem_dir, "config.py")
            
            # Get template content
            template_path = os.path.join(base_dir, "config_sample.py")
            try:
                with open(template_path, 'r', encoding='utf-8') as src_file:
                    content = src_file.read()
                    if "bonghong" in content:
                        content = content.replace("bonghong", problem_name)
                    else:
                        # Update the problem name
                        content = f'problemName = "{problem_name}"\n' + ''.join(
                            line for line in content.splitlines(True) 
                            if not line.strip().startswith('problemName')
                        )
            except Exception as e:
                content = f'''# Config for {problem_name}
                problemName = "{problem_name}"
                numSamples = 5
                numTests = 10
                timeLimit = 1
                memoryLimit = 512

                def generate():
                    # Your test generation logic here
                    pass
                '''
                print(f"Error reading template: {e}")
                
            with open(config_file, 'w', encoding='utf-8') as dst_file:
                dst_file.write(content)
            
            # Create solution files based on checkboxes
            if self.cpp_checkbox.isChecked():
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
            
            if self.py_checkbox.isChecked():
                solution_file = os.path.join(solutions_dir, f"{problem_name}.py")
                with open(solution_file, 'w', encoding='utf-8') as f:
                    f.write(f'''# Solution for {problem_name}

                    # Your code here
                    ''')
            self.update_file_tree()
            self.open_file(config_file)
            
            QMessageBox.information(self, "Success", f"Problem '{problem_name}' created successfully!")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to create problem: {str(e)}\n{traceback.format_exc()}")
            print("Error details:", traceback.format_exc())

    def use_selected_template(self):
        try:
            template_name = self.template_combo.currentText()
            if not template_name:
                return
                
            base_dir = os.path.dirname(os.path.abspath(__file__))
            if template_name == "config_sample.py":
                template_path = os.path.join(base_dir, template_name)
            else:
                template_path = os.path.join(base_dir, "config_sample", template_name)
            
            if not os.path.exists(template_path):
                QMessageBox.warning(self, "Template Not Found", f"Cannot find template: {template_path}")
                return
            index = self.tab_widget.currentIndex()
            if index < 0:
                QMessageBox.warning(self, "Warning", "No file open to apply template.")
                return
            editor = self.tab_widget.widget(index)
            file_path = editor.property("file_path")
            if not file_path.endswith('config.py'):
                QMessageBox.warning(self, "Warning", "Templates can only be applied to config.py files.")
                return
            try:
                with open(template_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                problem_dir = os.path.dirname(file_path)
                problem_name = os.path.basename(problem_dir)
                if problem_name:
                    import re
                    pattern = r'problemName\s*=\s*[\'"]([^\'"]*)[\'"]'
                    content = re.sub(pattern, f'problemName = "{problem_name}"', content)
                editor.setText(content)
                editor.setModified(True)
                QMessageBox.information(self, "Success", f"Template '{template_name}' applied.")
                    
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to apply template: {str(e)}")
                print("Template error details:", traceback.format_exc())
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to use template: {str(e)}\n{traceback.format_exc()}")
            print("Error details:", traceback.format_exc())

    def clear_all(self):
        """Clear all problems and solutions after confirmation"""
        try:
            response = QMessageBox.question(
                self, 
                "Confirm Clear", 
                "Are you sure you want to delete ALL problems and solutions?\n\nThis action cannot be undone!",
                QMessageBox.Yes | QMessageBox.No, 
                QMessageBox.No
            )
            
            if response != QMessageBox.Yes:
                return
            
            base_dir = os.path.dirname(os.path.abspath(__file__))
            problems_dir = os.path.join(base_dir, "problems")
            solutions_dir = os.path.join(base_dir, "solutions")
            for i in range(self.tab_widget.count()-1, -1, -1):
                self.tab_widget.removeTab(i)
            if os.path.exists(problems_dir):
                for item in os.listdir(problems_dir):
                    item_path = os.path.join(problems_dir, item)
                    if os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                    else:
                        os.remove(item_path)
            if os.path.exists(solutions_dir):
                for item in os.listdir(solutions_dir):
                    item_path = os.path.join(solutions_dir, item)
                    if os.path.isfile(item_path): 
                        os.remove(item_path)
            self.update_file_tree()
            
            QMessageBox.information(self, "Success", "All problems and solutions have been deleted.")
            
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to clear directories: {str(e)}")
            print("Error details:", traceback.format_exc())

    def export_tests(self):
        """Export all tests as a zip file"""
        try:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            problems_dir = os.path.join(base_dir, "problems")
            solutions_dir = os.path.join(base_dir, "solutions")
            if not os.path.exists(problems_dir) or not os.listdir(problems_dir):
                QMessageBox.warning(self, "No Tests", "There are no tests to export.")
                return
            file_dialog = QFileDialog()
            file_dialog.setAcceptMode(QFileDialog.AcceptSave)
            file_dialog.setNameFilter("Zip files (*.zip)")
            file_dialog.setDefaultSuffix("zip")
            file_dialog.setWindowTitle("Export Tests")
            file_dialog.setDirectory(os.path.expanduser("~"))
            file_dialog.selectFile("GenTest_export.zip")
            
            if file_dialog.exec_():
                save_path = file_dialog.selectedFiles()[0]
                with zipfile.ZipFile(save_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
                    for root, dirs, files in os.walk(problems_dir):
                        for file in files:
                            file_path = os.path.join(root, file)
                            arcname = os.path.relpath(file_path, base_dir)
                            zipf.write(file_path, arcname)
                    if os.path.exists(solutions_dir):
                        for file in os.listdir(solutions_dir):
                            file_path = os.path.join(solutions_dir, file)
                            if os.path.isfile(file_path):
                                arcname = os.path.join("solutions", file)
                                zipf.write(file_path, arcname)
                
                QMessageBox.information(self, "Export Successful", 
                    f"Tests successfully exported to:\n{save_path}")
        
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to export tests: {str(e)}")
            print("Export error details:", traceback.format_exc())

    def generate_tests(self):
        for i in range(self.tab_widget.count()):
            editor = self.tab_widget.widget(i)
            if editor.isModified():
                file_path = editor.property("file_path")
                self.save_file(editor, file_path)
        base_dir = os.path.dirname(os.path.abspath(__file__))
        gen_test_path = os.path.join(base_dir, "genTest.py")
        
        try:
            result = subprocess.run([sys.executable, gen_test_path], 
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                  text=True)
            
            if result.returncode == 0:
                QMessageBox.information(self, "Success", "Test generation completed successfully!")
                self.update_file_tree()
            else:
                QMessageBox.critical(self, "Error", f"Test generation failed:\n{result.stderr}")
                
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to run test generation: {str(e)}")

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = TestGenApp()
        window.showMaximized()
        sys.exit(app.exec_())
    except Exception as e:
        print("CRITICAL ERROR:", str(e))
        print(traceback.format_exc())
        if 'app' in locals():
            QMessageBox.critical(None, "Critical Error", 
                f"Application crashed: {str(e)}\n\nSee console for details.")