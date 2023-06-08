import os
import getpass
import testSystem

def read_town_names(source):
    seen_towns= set() #set to keep track of already seen towns
    with open(source, "r") as f:
        town_list= list(seen_towns)
        for line in f:
            town_name=line.split(":")[0].strip()
            if town_name not in seen_towns: 
                seen_towns.add(town_name) #add the town to the set of seen towns 
                town_list.append(town_name) #add the town to the list of towns 
    return town_list

def load_population_data(source, town_popn): 
    # town_population= {}
    for town in town_popn:
        print(f"{town}:")
        town_exists= False
        with open(source, "r") as f: 
            for line in f: 
                existing_town= line.strip().split(": ")[0]
                if town == existing_town:
                    town_exists= True
                    file_path= line.strip().split(": ")[1]
                    with open(file_path, "r") as town_file: 
                        lines= town_file.readlines()
                        population= lines[3].strip()
                        date= lines[0].strip()
                        print(f"{date}: {population}\n")
                        # town_population[town_name]= population
        if (town_exists == False):
            print("Cannot find this town in the current records")

def main():
    my_user_name=(getpass.getuser())
    my_home= testSystem.switch_system()[1]
    source = os.path.join(my_home, my_user_name, "Python_Data", "townFileIndex.txt")
    info_file= os.path.join(my_home,my_user_name, "Python_Data", "filesToSort")

    print("List of towns")

    towns= read_town_names(source)
    for town in towns:
        print(town, end=" ")

    town_popn= input("Enter town name/s here, separated by commas: ").split(",")

    load_population_data(source, town_popn) 

if __name__ == "__main__":
    main()




