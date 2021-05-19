import sys
import os
"""
    Should be called to manipulate files. 
"""

def add_testcase(problem_path):
    """
        I have problem path here. Create a new testcase.
    """
    return None

def view_testcase(problem_path, number):
    """
        Just print testcase and expected output.
    """
    return None

def run_testcase(problem_path, number):
    """
        Just run test case of perticular number 
    """
    return None

def add_template(template_path, problem_path, line_no):
    """
        Add template at line_no in problem code at problem_path
    """
    return None

def backup_current(problem_path):
    """
        Create Backup of current Code.
    """
    return None

def get_backup(problem_path):
    """
        Show backups and user should be able to retrive previous backup.
    """
    return None

def handle_tc(command):
    return None

def handle_template(command):
    return None

def handle_backup(command):
    return None

def main(command):
    if(command[0]=="tc"):
        handle_tc(command[1:])
    elif(command[0]=="temp"):
        handle_template(command[1:])
    elif(command[0]=="save"):
        handle_backup(command[1:])

if __name__=="__main__":
    main(sys.argv[1:])