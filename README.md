# Contest Parser (Need to change the name)

### Required Python Libraries
* os
* sys
* time
* re
* bs4
* termcolor

### Usage
* Create a Folder for all Codeforces contests and just copy app.py, checker.py and template.cpp in it (You can replace it with your template).
* If live contest has started just run app.py in terminal and enter the contest id.
* Contest Folder/Problem Folder/Test Cases will be fetched and saved is hierarchical manner.
* You can solve the problem in the cpp file in problem folder and then run checker in the problem folder which will get all the input from input files and will check program output and expected output. 
* You can create and add your test cases in the problem folder. Only to take care is let the input file be in5.txt and output file be out5.txt where the testcase number can be from 1 to 99 (in in5.txt and out5.txt it is 5).
* Standard checker may not give correct Verdict if there are multiple aswers to a problem, but you can change checker.py to check the output of such problems.
