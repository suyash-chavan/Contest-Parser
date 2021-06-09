from manager import write_json
import sys
import os
import datetime
import json
"""
    Should be called to manipulate files. 
"""

def add_testcase(problem_path):

    print("Enter TestCase Input: (Press Enter at Blank Line to Complete it)")
    testcase_input = ""
    number_of_empty_responses = 0

    while(True):
        line = input()

        if line=="":
            number_of_empty_responses+=1
            if number_of_empty_responses == 2:
                break
        else:
            testcase_input = testcase_input+"\n"+line
            number_of_empty_responses=0

    print("Enter TestCase Output: (Press Enter at Blank Line to Complete it)")
    testcase_output = ""
    number_of_empty_responses = 0

    while(True):
        line = input()

        if line=="":
            number_of_empty_responses+=1
            if number_of_empty_responses == 2:
                break
        else:
            testcase_output = testcase_output+"\n"+line
            number_of_empty_responses=0
    
    testcase_no = len([name for name in os.listdir(problem_path+"/Input") if os.path.isfile(os.path.join(problem_path+"/Input", name))])

    print("Creating Testcase...")

    testcase_in = open(problem_path+"/Input/"+"in"+str(testcase_no)+".txt","w+")
    testcase_out = open(problem_path+"/Output/"+"out"+str(testcase_no)+".txt","w+")

    testcase_in.write(testcase_input)
    testcase_out.write(testcase_output)

    testcase_in.close()
    testcase_out.close()

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

def backup_current(problem_path,problem_file_path):
    
    if(problem_path[-1]!="/"):
        problem_path = problem_path+"/"

    backup_folder_path = problem_path+"Backup/"

    if(not os.path.exists(backup_folder_path)):
        os.mkdir(backup_folder_path)

    title = input("Title of Backup: ")
    comments = input("Comments: ")

    backup_no = (len([name for name in os.listdir(backup_folder_path) if os.path.isfile(name)])/2)+1

    file_name = backup_folder_path+"backup"+str(backup_no)
    detail_name = backup_folder_path+"details"+str(backup_no)+".json"

    code = open(problem_file_path,"r")
    backup_code = open(file_name,"a")

    code_txt = code.read().strip()

    code.close()

    backup_code.write(code_txt)

    backup_code.close()

    details = {"title": title,
               "comments": comments,
               "timestamp": str(datetime.datetime.now())}
    
    write_json(details,detail_name)

    print("\nBackup Created!")

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