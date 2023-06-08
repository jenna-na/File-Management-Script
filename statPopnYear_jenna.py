import os
import getpass
import testSystem

my_user_name=(getpass.getuser())
my_home= testSystem.switch_system()[1]
path= os.path.join(my_home,my_user_name, "Python_Data", "filesToSort")

#all values in populations will be in a list 
populations= []
year_folder= input("Pick a year: ")
print("Populations from", year_folder, ":")
for year, month, day in os.walk(os.path.join(path, year_folder)):
    for file in day: 
        file_path = os.path.join(year, file)
        with open(file_path, "r") as f:
            line= f.readlines()
            first_line=f.readline().strip()
            last_line= line[-1].strip()
            print(last_line)
            try:
                population= int(last_line)
            except ValueError: 
                pass 
            #appending value of population variable to the list populations
            populations.append(population)
            if not first_line.startswith(year_folder):
                continue
        
#checking to see if populations list is empty/ no valid population number found in that year
if len(populations) == 0:
    print("No valid population found in", year_folder, ".")
else:
    Value= input("Maximum/ Minimum/ Average/ Sum?: " )
    if Value.upper() == "SUM":
        print(sum(populations))
    elif Value.upper() == "AVERAGE":
        total= sum(populations) 
        count= len(populations)
        if count>0: 
            average=total/count
        else: 
            average=0
        print(average)
    elif Value.upper() == "MAXIMUM": 
        print(max(populations))
    elif Value.upper() == "MINIMUM": 
        print(min(populations))
    else: print("Keyword not one of those listed, please try again")


        
        

