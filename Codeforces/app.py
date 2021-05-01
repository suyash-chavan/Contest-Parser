import os
import sys
import requests
import time
import re
from bs4 import BeautifulSoup
from termcolor import colored

parent_path = os.getcwd()
illegal = ["<", ">", "[", "]",  "?", ":", "*" , "|"]

contest_url = 'https://codeforces.com/contest/'

# Ask for Contest ID
contest_id =  input('Enter the contest id: ')

# Template Extension
extension = ".cpp"

contest_url = contest_url + contest_id

page = requests.get(contest_url, verify = True)

if(page.status_code != 200):
    print("Failed to retrive contest {}!!!".format(contest_id))
    exit(1)

# Get Contest Page
soup = BeautifulSoup(page.text, 'html.parser')

# Problem URL for contest
contest_problem_url = 'https://codeforces.com/contest/{}/problem/'.format(contest_id)

# Extract i/o statements for the problem
def get_contest_io(contest_problem_url,prob_folder_name,prob_no,prob_name,contest_id):

    url = 'https://codeforces.com/contest/{}/problem/{}'.format(contest_id,prob_no)
    page = requests.get(url, verify = True)
    soup = BeautifulSoup(page.text, 'html.parser')

    inp = soup.findAll('div', attrs={"class" : "input"})
    out = soup.findAll('div', attrs={"class" : "output"})

    input_folder_name = os.path.join(prob_folder_name, "Input")
    output_folder_name = os.path.join(prob_folder_name, "Output")

    # Creating Input and Output folder
    os.mkdir(input_folder_name)
    os.mkdir(output_folder_name)

    #Input in Input folder and Output in Output folder
    for i in range(len(inp)):
        i_file = "in"+str(i+1)+".txt"
        o_file = "out"+str(i+1)+".txt"
        i_file = os.path.join(input_folder_name,i_file)
        o_file = os.path.join(output_folder_name,o_file)
        test_in = open(i_file, "a")
        test_out = open(o_file,"a")

        test_in.write(inp[i].text[6:])
        test_out.write(out[i].text[7:])

        test_in.close()
        test_out.close()


# Create Problem folders
def create_problem_folder(prob_no, prob_name,contest_problem_url,folder_name,extension,template_txt,contest_id,checker):
    print("Problem: "+prob_no+". "+prob_name)
    contest_problem_url = contest_problem_url +  prob_no

    # Problem Folder
    prob_folder_name = prob_no + " " + prob_name

    for str_char in illegal:
        prob_folder_name = prob_folder_name.replace(str_char," ")

    prob_folder_name = os.path.join(folder_name, prob_folder_name)
    
    os.mkdir(prob_folder_name)

    file1 = prob_no + extension
    file1 = os.path.join(prob_folder_name,file1)
    fname = open(file1,"a")
    fname.write(template_txt)
    fname.close()


    file1 = os.path.join(prob_folder_name,"checker.py")
    fname = open(file1,"a")
    fname.write(checker)
    fname.close()

    print("Problem Extraction - ",end='')
    print(colored('DONE', 'green'))

    get_contest_io(contest_problem_url,prob_folder_name,prob_no,prob_name,contest_id)
    print("Problem IO Extraction - ",end='')
    print(colored('DONE', 'green'))

    #create the input.txt file for personal input output
    file3 = "input.txt"
    file3 = os.path.join(prob_folder_name,file3)
    fname = open(file3,"a")
    fname.close()

    file3 = "output.txt"
    file3 = os.path.join(prob_folder_name,file3)
    fname = open(file3,"a")
    fname.close()

    print("\n------------------------------------------------\n")
    time.sleep(2)

#f Function to get the folder_name
def get_folder_name(contest_name):
    folder_name = os.path.join(parent_path,contest_name)
    for str_char in illegal:
        folder_name = folder_name[0:10] + folder_name[10:].replace(str_char," ")
    return folder_name

#---------------------------------MAIN---------------------------------------------#
#Extract the contest-details
tables = soup.findAll('table')
contest_name = tables[0].find('a').text.strip()
print("\n------------------------------------------------")
print("\nContest Name: "+contest_name)
print("\nContest Link: "+contest_url+"\n")
print("------------------------------------------------\n")

# Contest Folder
folder_name = get_folder_name(contest_name)

# Extract the Datatable
problems = soup.find('div', attrs={"class":"datatable"}).find('table').findAll('a')

# Parse the Template
fname = open('template.cpp', "r")
template_txt = fname.read().strip()
fname.close()

# Parse the testcase checker
fname = open('checker.py',"r")
checker = fname.read().strip()
fname.close()

# Create Contest Folder
os.mkdir(folder_name)

time.sleep(2)

# List of Problems
prob_x = []

for i in range(len(problems)):
    #For every contest
    if i%4 !=0 : 
        continue

    txt = problems[i].text.strip()
    prob_no = problems[i].text.strip()
    
    prob_name = problems[i+1].text.strip()
    prob_x.append(prob_no)

    prob_folder_name = prob_name

    for str_char in illegal:
        prob_folder_name = prob_folder_name.replace(str_char," ")

    create_problem_folder(prob_no,prob_folder_name,contest_problem_url,folder_name,extension,template_txt,contest_id,checker)
