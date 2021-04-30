import os
import sys
import json
import re
from prettytable import PrettyTable
from termcolor import colored

current_working_workspace = None

def list_workspaces(para,need_data):
	
	try:
		settings_file = open("settings.json","r")
	except Exception:
		print("Missing settings.json")
		return None

	settings = json.load(settings_file)

	settings_file.close()

	workspace_no = 1
	workspace_list = []

	workspaces_table = PrettyTable()

	workspaces_table.field_names = ["ID","Workspace Name","Path"]

	for workspace in settings["workspaces"]:
		workspace_list.append([str(workspace_no),workspace["name"],workspace["path"]])
		workspaces_table.add_row([str(workspace_no),workspace["name"],workspace["path"]])
		workspace_no+=1

	if(len(workspace_list)==0):
		print("No Workspace Created!")
		return None

	print()

	print(workspaces_table)

	if(need_data):
		return workspace_list

	return None

def create_workspace(para):
	
	try:
		settings_file = open("settings.json","r")
	except Exception:
		print("Missing settings.json")
		return 

	settings = json.load(settings_file)
	print()

	workspace_name = input("Enter Workspace Name: ")

	workspace_name.rstrip()

	for workspace in settings["workspaces"]:
		if(workspace["name"]==workspace_name):
			print("Workspace {} already exists!".format(workspace_name))
			return 

	workspace_path = input("Enter Workspace Directory Path: ")

	if(os.path.isfile(workspace_path)):
		print("Invalid Path!")
		return 

	if(not os.path.isdir(workspace_path)):
		return None
		# Ask if you want yo create directory and if want create directory else return

def set_workspace(para):
	workspace_list = list_workspaces({},True)

	if(workspace_list==None):
		print("Cannot set Workspace!")
		return None

	print()

	try:
		workspace_id = int(input("Enter Workspace ID: "))
	except Exception:
		print("Invalid Workspace ID!")
		return None

	max_id = len(workspace_list)

	if(workspace_id<1 or workspace_id>max_id):
		print("Invalid Workspace ID!")
		return None

	global current_working_workspace

	current_working_workspace = workspace_list[workspace_id-1]

	print()
	print("Workspace Set Successfully!")

	return None

def current_workspace(para):

	if(current_working_workspace==None):
		print("Workspace Not Set!")
		return None

	print()

	print("Workspace ID: {}, Name: {}, Path: '{}'".format(current_working_workspace[0],current_working_workspace[1],current_working_workspace[2]))


def check_flags(user_flags, valid_flags):

	for flag in user_flags:
		if(flag not in valid_flags):
			print("Invalid Command!")
			return False
		elif((user_flags[flag]==None and valid_flags[flag]!=None) or (user_flags[flag]!=None and valid_flags[flag]==None)):
			print("Invalid Command!")
			return False

	return True

def verify_and_execute(main_command,flag_parametres):

	# Hardcoded valid main commands list
	# Dictionary of Main Command and valid flags
	valid_main_commands = {"list workspaces":{},
						   "set workspace":{},
						   "current workspace":{},
						   "create workspace":{}}

	if(main_command not in valid_main_commands):
		print("Invalid Command!")
		return None

	# Now we need to handle both 
	if(main_command=="list workspaces"):

		# Flag validity and type checking
		if(check_flags(flag_parametres,valid_main_commands["list workspaces"])):
			list_workspaces(flag_parametres,False)
		else:
			return None

	elif(main_command=="set workspace"):

		# Flag validity and type checking
		if(check_flags(flag_parametres,valid_main_commands["set workspace"])):
			set_workspace(flag_parametres)
		else:
			return None

	elif(main_command=="current workspace"):

		# Flag validity and type checking
		if(check_flags(flag_parametres,valid_main_commands["current workspace"])):
			current_workspace(flag_parametres)
		else:
			return None

	elif(main_command=="create workspace"):

		# Flag validity and type checking
		if(check_flags(flag_parametres,valid_main_commands["create workspace"])):
			create_workspace(flag_parametres)
		else:
			return None


def parse_command(command):

	if(len(command)==0):
		return None

	main_command = []

	for word in command:
		if(word[0]!='-'):
			main_command.append(word)
		else:
			break

	if(len(main_command)==0 or main_command[-1][0]=="-"):
		print("Invalid Command!")
		return None

	flag_parametres = {}

	for idx in range(0,len(command)):
		if(command[idx][0]=='-'):
			try:
				if(command[idx+1][0]=='-'):
					flag_parametres[command[idx]] = None
				else:
					if(command[idx] not in flag_parametres):
						flag_parametres[command[idx]] = command[idx+1]
					else:
						print("Invalid Command!")
						return None
			except Exception:
				flag_parametres[command[idx]]=None

	verify_and_execute(" ".join(main_command),flag_parametres)

def start_cmd():

	print()

	if(current_working_workspace==None):
		print(colored("┌──(",'green')+colored('\033[1m'+"!"+'\033[0m','blue')+colored(")-[",'green')+'\033[1m'+"!"+'\033[0m'+colored("]",'green'))
		print(colored("└─$ ",'green'),end='')
	else:
		print(colored("┌──(",'green')+colored('\033[1m'+current_working_workspace[1]+'\033[0m','blue')+colored(")-[",'green')+'\033[1m'+current_working_workspace[2]+'\033[0m'+colored("]",'green'))
		print(colored("└─$ ",'green'),end='')

	command = input()

	command.rstrip()
	command.lstrip()

	command = command.split()

	parse_command(command)

if __name__=="__main__":

	print()
	print(" ___________________________________________________________________________________________________________")
	print("|                                                                                                           |")
	print("|     $$$$$$\\  $$$$$$$\\        $$\\      $$\\                                                                 |")
	print("|    $$  __$$\\ $$  __$$\\       $$$\\    $$$ |                                                                |")
	print("|    $$ /  \\__|$$ |  $$ |      $$$$\\  $$$$ | $$$$$$\\  $$$$$$$\\   $$$$$$\\   $$$$$$\\   $$$$$$\\   $$$$$$\\      |")
	print("|    $$ |      $$$$$$$  |      $$\\$$\\$$ $$ | \\____$$\\ $$  __$$\\  \\____$$\\ $$  __$$\\ $$  __$$\\ $$  __$$\\     |")
	print("|    $$ |      $$  ____/       $$ \\$$$  $$ | $$$$$$$ |$$ |  $$ | $$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ |  \\__|    |")
	print("|    $$ |  $$\\ $$ |            $$ |\\$  /$$ |$$  __$$ |$$ |  $$ |$$  __$$ |$$ |  $$ |$$   ____|$$ |          |")
	print("|    \\$$$$$$  |$$ |            $$ | \\_/ $$ |\\$$$$$$$ |$$ |  $$ |\\$$$$$$$ |\\$$$$$$$ |\\$$$$$$$\\ $$ |          |")
	print("|     \\______/ \\__|            \\__|     \\__| \\_______|\\__|  \\__| \\_______| \\____$$ | \\_______|\\__|          |")
	print("|                                                                         $$\\   $$ |                        |")
	print("|                                                                         \\$$$$$$  |                        |")
	print("|                                                                          \\______/                         |")
	print("|                                                                                                           |")
	print("|                                               Version 1.0                                                 |")
	print("|___________________________________________________________________________________________________________|")

	while(True):
		start_cmd()