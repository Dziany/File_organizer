import pathlib
import shutil
import json
import sys


try:
    #Opening config.josn file (our extension dictionary) in read only 
    with open('config.json', 'r') as f:
        #extension_map is our dictionary now
        extension_map = json.load(f)
#in case the config.json file is missiong
except FileNotFoundError:
    print("ERROR: The config.json file was not found, make sure it is included")
    sys.exit(1)

#Directory to be organised (Make sure it is right for your setup!)
folder_to_organize = pathlib.Path("C:\Users\User\Downloads")

#Main Loop for organizing files in Downloads
for item in folder_to_organize.iterdir():
    #Skip over our script files
    if item.is_dir() or item.name in ['config.json', 'main.py']:
        continue
    
    #Get item extensions and change it to lowercase 
    file_ext = item.suffix.lower()
    #Create a flage to monitore if moved
    moved = False

    #check all category in dictionary
    for category, extensions in extension_map.items():
        if file_ext in extensions:
            #Create path to new directory
            target_dir = folder_to_organize / category
            #Create folder if not preexisting
            target_dir.mkdir(exist_ok = True)


            try:
                #Moving files part
                shutil.move(str(item), str(target_dir / item.name))
                #print success message if moved succesfully
                print(f"Success:  {item.name} -> {category}")
                #mark flag 
                moved = True
                break

            #handling errors:
            except PermissionError:
                print(f"Error: Is the {item.name} open?")
                moved = True
                break
            except FileExistsError:
                print(f"Warning!: File {item.name} is already in directory {category}")
                moved = True
                break
            except Exception as e:
                print(f"Unexpected error with file {item.name}: {e}")
                moved = True
                break

        #if extension not recognised
        if not moved:
            #Create others folder if not preexisting
            others_dir = folder_to_organize / "Others"
            others_dir.mkdir(exist_ok=True)
            
            try:
                #move file to others
                shutil.move(str(item), str(others_dir / item.name))
                #print message about succesfull moving file
                print(f"Inne: {item.name} -> Others")
            
            #handling errors:
            except PermissionError:
                print(f"Error: Is the {item.name} open?")
            except FileExistsError:
                print(f"Warning!: File {item.name} is already in directory {category}")
            except Exception as e:
                print(f"Unexpected error with file {item.name}: {e}")
    