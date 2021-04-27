import os
import sys
import json
import re
from termcolor import colored

current_working_workspace = None

def list_workspaces():
	
	try:
		settings_file = open("settings.json","r")
	except Exception:
		print("Missing settings.json")
		return 

	settings = json.load(settings_file)

	settings_file.close()

	workspace_no = 1
	workspace_list = []

	workspace_list.append(["ID","Workspace Name","Path"])

	for workspace in settings["workspaces"]:
		workspace_list.append([str(workspace_no),workspace["name"],workspace["path"]])
		workspace_no+=1

	if(len(workspace_list)==1):
		print("No Workspace Created!")
		return

	col_width = [0 for _ in range(len(workspace_list[0]))]

	for row in workspace_list:
		for col in range(len(row)):
			col_width[col] = max(col_width[col],len(row[col]))

	workspace_list.insert(1,["".join("-" for _ in range(dashes)) for dashes in col_width])

	print()

	for row in workspace_list:
		for col in range(len(row)):
			print(row[col].ljust(col_width[col]+2),end='')
		print()

def create_workspace():
	
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
		return 
		# Ask if you want yo create directory and if want create directory else return

def start_cmd():

	print()
	print(">> ",end='')

	command = input()

	if(command=="list workspaces"):
		list_workspaces()
	elif(command=="create workspace"):
		create_workspace()
	else:
		print("Invalid Command!")


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