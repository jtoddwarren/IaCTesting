# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 23:29:10 2020
ADDING A COMMENT TO THE TOP
2 - added another line
3 - added a 3rd line to main.py
4 - added another useless comment to main.py
5 - adding another useless comment to main.py
@author: mehedi.md.hasan
"""
from util import Util
from iac_testing_antipatterns import IaCTestingAntipatterns

def main():
    
    
    
    base_dir= input("Please enter the directory: ")
    print("\n")
    
    
    project_name = input ("Please enter the project name: ")
    print(project_name)
    
    print("Testing branch")
    
    files = Util().get_files(base_dir)
#    print(files)
    
#    quit()
    
    iac_testing_antipatterns = IaCTestingAntipatterns(files, project_name)
#    
    iac_testing_antipatterns.get_anti_pattern_list()
#    
if __name__ == "__main__":
    main()