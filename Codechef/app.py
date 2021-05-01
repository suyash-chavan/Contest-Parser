import os
import sys
import requests
import time
import re
from bs4 import BeautifulSoup
from termcolor import colored
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import urllib
import re
import json
import validators

parent_path = os.getcwd()
illegal = ["<", ">", "[", "]",  "?", ":", "*" , "|"]

contest_url = 'https://www.codechef.com/'

# Ask for Contest ID
contest_id =  input('Enter the contest id: ')

# Template Extension
extension = ".cpp"

contest_url = contest_url + contest_id

page = requests.get(contest_url, verify = True)

if(page.status_code != 200):
    print("Failed to retrive contest {}!!!".format(contest_id))
    exit(1)


browser= webdriver.Chrome('/usr/bin/chromedriver')
browser.get(contest_url)
sleep(1)

contestPage = browser.page_source

#<a id="ember359" class="ember-view" href="/SALC2021/problems/ALGOCUP2" title="Check The Constraints">Check The Constraints</a>


# Get Contest Page
lstOfProblemLinks = re.findall(r"class\=\"ember\-view\" href\=\"\/.*\<\/a\>", contestPage)

# 'class="ember-view" href="/SALC2021/problems/ALGOCUP4" title="Save Sattu">Save Sattu</a>'
problemNames = []
for i in range(1, len(lstOfProblemLinks)):
    problemNames.append(lstOfProblemLinks[i].split("\"")[5])
    
# ignore 1st instance

theProblemURLs = []

for i in range(1, len(lstOfProblemLinks)):
    theProblemURLs.append("https://www.codechef.com"+lstOfProblemLinks[i].split("\"")[3])

#<a href="/contests/">Compete</a>&nbsp;»&nbsp;Spider AlgoCup</aside>
contest_name = re.findall(r"\/contests\/\"\>Compete\<\/a.*?\<\/aside\>", contestPage, re.DOTALL)[0]
contest_name = contest_name.split(";")[2].split("<")[0]

# # Extract i/o statements for the problem
def get_contest_io(contest_problem_url,prob_folder_name,prob_no,prob_name,contest_id):

#https://codeforces.com/contest/1508/problem/F /home/devz/Desktop/Programs/Contest-Parser/Codeforces/Codeforces Round #715 (Div. 1)/F Optimal Encoding F Optimal Encoding 1508
#https://www.codechef.com/SALC2021/problems/ALGOCUP4 /home/devz/Desktop/Programs/Contest-Parser/Codechef/Spider AlgoCup/6 Save Sattu 6 Save Sattu SALC2021
    
    url = contest_problem_url
    
    browser.get(url)
    sleep(1)

    problemPage = browser.page_source
    
    # <code class=" mathjax-support">5 3
    #     1 5 3 9 4 
    #     0 1
    #     1 2
    #     3 4
    # </code>
    
    #contest_name = re.findall(r"\/contests\/\"\>Compete\<\/a.*?\<\/aside\>", contestPage, re.DOTALL)[0]
    
    allCodes2 = re.findall(r"\<code class\=\" mathjax\-support.*?\<\/code\>", problemPage, re.DOTALL)
    
    allCodes = []
    
    for a in allCodes2:
        temp = a.split(">")[1].split("<")[0]
        allCodes.append(temp)
    
    inp = []
    out = []
    
    for code in range(len(allCodes)):
        if code%2 == 0:
            inp.append(allCodes[code])
        else:
            out.append(allCodes[code])

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

        test_in.write(inp[i])
        test_out.write(out[i])

        test_in.close()
        test_out.close()


# Create Problem folders
def create_problem_folder(prob_no, prob_name,contest_problem_url,folder_name,extension,template_txt,contest_id,checker):
    prob_no = str(prob_no)
    print("Problem: "+str(prob_no)+". "+prob_name)

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
print("\n------------------------------------------------")
print("\nContest Name: "+contest_name)
print("\nContest Link: "+contest_url+"\n")
print("------------------------------------------------\n")

# Contest Folder
folder_name = get_folder_name(contest_name)

# Extract the Datatable
problems = theProblemURLs

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
    prob_no = i+1
    prob_folder_name = problemNames[i]
    contest_problem_url = problems[i]
    create_problem_folder(prob_no,prob_folder_name,contest_problem_url,folder_name,extension,template_txt,contest_id,checker)

browser.quit()