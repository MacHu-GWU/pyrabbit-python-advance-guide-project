#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys
import os

        
def detect_python_in_windows(version=[]):
    """
    
    :param version: major version list, accept: 26, 27, 32, 33, 34, 35
    :type version: list of integer
    """
    # define the Python version you want to use
    _valid_version = [26, 27, 32, 33, 34, 35]
    python_pattern = list()
    
    if len(version):
        for v in version:
            if v in _valid_version:
                python_pattern.append("Python%s" % v)
    else:
        for v in _valid_version:
            python_pattern.append("Python%s" % v)
            
    
    # find all installed Python
    _win_root = r"C:\\"

    installed_python = list()
    for dirname in os.listdir(_win_root):
        for pattern in python_pattern:
            if dirname in python_pattern:
                installed_python.append(dirname)
                break
    
    # find all Python interpreter's absolute path
    installed_interpreter = list()
            
    _valid_exe = [
        "python.exe", "python2.exe", "python3.exe",
        "python26.exe", "python27.exe",
        "python32.exe", "python33.exe", "python34.exe", "python35.exe",    
    ]
    
    for dirname in installed_python:
        for basename in os.listdir(os.path.join(_win_root, dirname)):
            if basename in _valid_exe:
                installed_interpreter.append(os.path.join(_win_root, dirname, basename))
        
    return installed_interpreter

class MainTestCase(object):
    def __init__(self, root, version=[], keyword=[]):
        if os.path.exists(root):
            self.root = os.path.abspath(root)
        else:
            raise FileNotFoundError(root)
        self.version = version
        self.keyword = keyword
    
    def run(self):
        if sys.platform == "win32":
            self._run_in_windows()
    
    def _run_in_windows(self):
        installed_interpreter = detect_python_in_windows(self.version)
        
        todo = list()
        for current_dir, folderlist, fnamelist in os.walk(self.root):
            for basename in fnamelist:
                abspath = os.path.abspath(os.path.join(current_dir, basename))
                relpath = os.path.relpath(abspath, self.root)
                fname, ext = os.path.splitext(basename)
                
                if ext.lower() == ".py" and fname != "__init__":
                    if len(self.keyword):
                        fname, _ = os.path.splitext(relpath)
                        for key in self.keyword:
                            if key in relpath:
                                todo.append(abspath)
                                break
                    else:
                        todo.append(abspath)

        bat_file_content = list()
        for abspath in todo:
            for interpreter in installed_interpreter:
                cmd = "%s %s" % (interpreter, abspath)
                bat_file_content.append(cmd)
        bat_file_content.append("pause")
        
        with open("RunPythonMainTest.bat", "wb") as f:
            f.write("\n".join(bat_file_content).encode("utf-8"))
                
if __name__ == "__main__":
    root = r"C:\Users\shu\Documents\PythonWorkSpace\py3\py33_projects\pyrabbit-python-advance-guide-project\pyguide\p3_stdlib\c19_internet_data_handling"
    version = [27, 33]
    keyword = []
    testcase = MainTestCase(root, version, keyword)
    testcase.run()
#     print(detect_python_in_windows(version=[27, 33]))