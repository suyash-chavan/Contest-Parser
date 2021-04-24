import os
import sys
import re
import filecmp
from termcolor import colored


files = [f for f in os.listdir('.') if os.path.isfile(f)]

i_files = []
o_files = []
code_file = ""

for file in files:
	if(re.search("^in[1-9].txt",file) or re.search("^in[1-9][1-9].txt",file)):
		i_files.append(file)

	if(re.search("^out[1-9].txt",file) or re.search("^out[1-9][1-9].txt",file)):
		o_files.append(file)

	if(re.search(".cpp$",file)):
		code_file = file

# Compile file
if(os.system("g++ "+code_file+" -o"+code_file[:-4])!=0):
	print("Found Error in the Code!")
	exit(0)

print(colored('\nTestcases may FAIL for Multiple Correct Answers!', 'red'))
print("------------------------------------------------\n")

# Sort files as per test cases
i_files.sort(key=lambda f: int(f[2:-4]))
o_files.sort(key=lambda f: int(f[3:-4]))
temp_out_files = []

for file_no in range(1,len(i_files)+1):

	# Temporary out file
	temp_out = "temp_out"+str(file_no)+".txt"

	temp_out_files.append(temp_out)

	# Run the input filr
	os.system("./"+code_file[:-4]+" < "+i_files[file_no-1]+" > "+temp_out)

# Check if Output is same as expected Output
for i in range(len(o_files)):

	if(filecmp.cmp(o_files[i],temp_out_files[i])):
		print("Test Case "+str(i+1)+": PASSED")
	else:
		print("Test Case "+str(i+1)+": FAILED")

	os.remove(temp_out_files[i])