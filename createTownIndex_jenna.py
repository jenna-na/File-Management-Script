import os
import getpass
import testSystem
import makeStructure_jenna

my_user_name=(getpass.getuser())
my_home= testSystem.switch_system()[1]
path= os.path.join(my_home,my_user_name, "Python_Data", "filesToSort")
output_path= os.path.join(my_home, my_user_name, "Python_Data", "townFileIndex.txt")

#create function that works like os.walk
def list_function(path):
    #create empty list for filenames to go in
    file_list= []
    for file in os.listdir(path): 
        filepath= os.path.join(path, file)
        if os.path.isdir(filepath):
            file_list.extend(list_function(filepath))
        else: 
            file_list.append(filepath)
    return file_list 

#Get first character of town name 
def get_first_char(town_file_tuple):
    return town_file_tuple[0]

#how to create file index
def create_file_index(path):
    with open(output_path, "w") as outfile:
        file_list = []
        for filepath in list_function(path):
            #get town name from each file
            with open(filepath, "r") as f:
                lines = f.readlines()
                if (lines != []):
                    town_name = lines[-2].strip()
                    if os.path.isfile(filepath):
                        #append town name and file path to file list 
                        file_list.append((town_name, filepath))
        sorted_file_list = sorted(file_list, key=get_first_char)
        #write town name and file path to outfile
        for town_name, filepath in sorted_file_list:
            outfile.write(f"{town_name}: {filepath}\n")

create_file_index(path)
