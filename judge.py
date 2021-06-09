import os
import sys
import re
import filecmp
from termcolor import colored

def check(program_out,expected_out):

	"""
		User can edit this function for check if the output is correct. By default this function will return
		"PASSED" if program output exactly matches to expected output.

		User needs to edit this function for problems where Multiple Correct Outputs are accepted.
	"""

	if(program_out==expected_out):
		return "PASSED"

	return "FAILED"

input_path = os.path.join(os.getcwd(),"Input/")
output_path = os.path.join(os.getcwd(),"Output/")

i_files = [f for f in os.listdir(input_path) if os.path.isfile(input_path+f)]
o_files = [f for f in os.listdir(output_path) if os.path.isfile(output_path+f)]
files = [f for f in os.listdir('./') if os.path.isfile(f)]

code_file = ""

for file in files:
	# Get code file
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

	tc_path = "'"+input_path+i_files[file_no-1]+"'"

	# Run the input filr
	os.system("./"+code_file[:-4]+" < "+tc_path+" > "+temp_out)

# Check if Output is same as expected Output
for i in range(len(o_files)):

	# Getting Program Output
	fname = open(temp_out_files[i],"r")
	output = fname.read().strip()
	fname.close()

	# Getting Expected Output
	fname = open(output_path+o_files[i],"r")
	expected_output = fname.read().strip()
	fname.close()

	print("Test Case "+str(i+1)+": ",end='')

	print(check(output,expected_output))

	os.remove(temp_out_files[i])

def main(command):
	if("".join(str(x) for x in command).count("-a")>0):
		"""
			Need to run against all testcases
		"""
	else:
		"""
			Need to run against some testcases
		"""

if __name__=="__main__":
	main(sys.argv[1:])