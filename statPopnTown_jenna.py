import os
import getPopTown_jenna
import getpass
import testSystem

my_user_name=(getpass.getuser())
my_home= testSystem.switch_system()[1]
source = os.path.join(my_home, my_user_name, "Python_Data", "townFileIndex.txt")

print("List of towns: ")
towns= getPopTown_jenna.read_town_names(source)
for town in towns: 
    print(town, end=" ")

town_exists= False
while not town_exists:
    chosen_town= input("\nPlease pick a town from the list below: ")

    with open(source, "r") as text_file:
        print(f"{chosen_town}:")
        populations= []
        for line in text_file:
            existing_town= line.strip().split(": ")[0]
            if chosen_town == existing_town:
                town_exists= True
                file_path= line.strip().split(": ")[1]
                with open(file_path, "r") as data_file:
                    line= data_file.readlines()
                    population= int(line[3].strip())
                    # print(f"{population}")
                    populations.append(population)
        if (town_exists == True):
            total= sum(populations)
            count= len(populations)
            avg= total/count
            maximum= max(populations)
            minimum= min(populations)
            print(f"The total population is {total}.")
            print(f"The average population is {avg}.")
            print(f"The minimum population is {minimum}.")
            print(f"The maximum population is {maximum}.")
        else:
            print("Town not found. Please try again.")


