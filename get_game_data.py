#!/usr/bin/env python3

import os 
import json 
import shutil # For copy and overwrite operations 
from subprocess import PIPE, run 
import sys

"""
SAMUEL ALBERSHTEIN - COPY PROCESSS AND JSON CREATION

This script prompts the user for a file path for a directory which has games and other files.
The script will find the directories in that directory that have 'game' in their name and extract a new name without the 'game' element.
The target directory will be created if it's not there yet(or overwritten) and a new directory with the game name will be created in the
target directory (without the 'game' in the dir's name) with all of it's contents
+
Writing a JSON file that has metadata about the games. (What the game directories are and how many of them exist)
+
Compiling the code inside of a directory and running it using a subprocess
"""

GAME_DIR_PATTERN = 'game'

def find_all_game_paths(source):
    game_paths = []

    for root, dirs, files in os.walk(source): # Walks recursively through all the directories and files in them and moves to next directory 

        for directory in dirs: # gives only the name of the directory and not the full path 

            if GAME_DIR_PATTERN in directory.lower(): # String is basically a list

                path = os.path.join(source, directory) # Saving the path of the directory with game in it's name 

                game_paths.append(path)

        break 
    # Breaking now because we don't want to run over the files in a directory, we want to move to the next directory (One iteration of walk is enough!)

    return game_paths



def create_dir(path):

    if not os.path.exists(path):
        os.mkdir(path)



def get_name_from_paths(paths, to_strip):
    new_names = []
    
    for path in paths:
        
        _, dir_name = os.path.split(path) # Splits path into head- parent catalog and tail- file itself and saves as tuple. 

        new_dir_name = dir_name.replace(to_strip, "") # .replace "deletes" the element to_strip that we declared from the dir_name in this iteration. 

        new_names.append(new_dir_name) # Adding to list 
    
    return new_names



def copy_and_overwrite(source, dest): # If the directory already exists we will want to overwrite it. (+Recursive copy / regular copy doesn't do that)

    if os.path.exists(dest): # Removing destination folder 
        shutil.rmtree(dest)

    shutil.copytree(source, dest)



def make_json_metadata_file(path, game_dirs):
    data = {          # The data we want to write into JSON
        "gameNames": game_dirs,
        "numberOfGames": len(game_dirs)
    }
    
    with open(path, "w") as f: 
        json.dump(data, f) 



"""
Second Step
|
v
"""

def main(source, target):

    cwd = os.getcwd()

    source_path = os.path.join(cwd, source)
    target_path = os.path.join(cwd, target)

    #TEST(In order):

    game_paths = find_all_game_paths(source_path) # Getting the full paths of the directories with the game string element in them

    new_game_dirs = get_name_from_paths(game_paths, "_game") # Extracting the names of the directories without the game element

    create_dir(target_path) # Creating or overwriting a directory into which we'll want to put the new directory after removing game from it's name

    for src, dest in zip(game_paths, new_game_dirs): # Grouping full path and the new directory name that we will create without the game element.

        dest_path = os.path.join(target_path, dest) 
        # Getting the new destination so we will not only copy the internal files of the source but create a directory inside the target so there will be a separated directory with the copied stuff

        copy_and_overwrite(src, dest_path) # Actually copying\

    json_path = os.path.join(target_path, "metadata.json") # The second value is a name that we'll give to the JSON that we came up with
    make_json_metadata_file(json_path, new_game_dirs)


"""
FIRST STEP
| 
v
"""

if __name__ == "__main__": # Executing the main script only if we run the script directly and not via import to other script (we would be able to import functions and classes only)

    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.") 
    
    # This time we will not use try: except: because we want to raise an error and stop instead of trying to continue the code.
    
    source, target = args[1:] #sys.argv returns a list and we want to pick only the arguments to be attached to the variables 

    main(source, target)